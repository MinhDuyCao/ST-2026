import tkinter as tk
import math

def draw_koch(canvas, x1, y1, x2, y2, order):
    if order == 0:
        canvas.create_line(x1, y1, x2, y2)
    else:
        # Divide the segment into 3 parts
        dx = (x2 - x1) / 3
        dy = (y2 - y1) / 3

        xA = x1 + dx
        yA = y1 + dy

        xB = x1 + 2 * dx
        yB = y1 + 2 * dy

        # Create the peak of the equilateral triangle
        angle = math.radians(60)
        xPeak = xA + (dx * math.cos(angle) - dy * math.sin(angle))
        yPeak = yA + (dx * math.sin(angle) + dy * math.cos(angle))

        # Recursively draw 4 segments
        draw_koch(canvas, x1, y1, xA, yA, order - 1)
        draw_koch(canvas, xA, yA, xPeak, yPeak, order - 1)
        draw_koch(canvas, xPeak, yPeak, xB, yB, order - 1)
        draw_koch(canvas, xB, yB, x2, y2, order - 1)

def draw_snowflake(canvas, order):
    canvas.delete("all")

    width = 500
    height = 500

    # Coordinates of an equilateral triangle
    x1, y1 = 150, 350
    x2, y2 = 350, 350
    x3, y3 = 250, 350 - (math.sqrt(3) * 100)

    draw_koch(canvas, x1, y1, x2, y2, order)
    draw_koch(canvas, x2, y2, x3, y3, order)
    draw_koch(canvas, x3, y3, x1, y1, order)

def main():
    window = tk.Tk()
    window.title("Koch Snowflake")

    canvas = tk.Canvas(window, width=500, height=500, bg="white")
    canvas.pack()

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(frame, text="Enter an order:").pack(side=tk.LEFT)
    order_entry = tk.Entry(frame, width=5)
    order_entry.pack(side=tk.LEFT)

    def display():
        try:
            order = int(order_entry.get())
            draw_snowflake(canvas, order)
        except ValueError:
            pass

    tk.Button(frame, text="Display", command=display).pack(side=tk.LEFT)

    window.mainloop()

if __name__ == "__main__":
    main()