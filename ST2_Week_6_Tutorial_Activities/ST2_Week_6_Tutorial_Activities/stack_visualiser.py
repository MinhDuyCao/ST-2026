import tkinter as tk
from tkinter import messagebox

NODE_WIDTH = 80
NODE_HEIGHT = 40
HORIZONTAL_GAP = 20
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 200

class QueueVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Visualizer (FIFO)")

        self.queue = []

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Label(control_frame, text="Push Value:").grid(row=0, column=0)
        self.push_entry = tk.Entry(control_frame, width=10)
        self.push_entry.grid(row=0, column=1)

        push_btn = tk.Button(control_frame, text="Push", command=self.push_value)
        push_btn.grid(row=0, column=2, padx=10)

        pop_btn = tk.Button(control_frame, text="Pop", command=self.pop_value)
        pop_btn.grid(row=1, column=2, pady=10)

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.draw_queue()

    def draw_node(self, x, y, value):
        self.canvas.create_rectangle(
            x, y, x + NODE_WIDTH, y + NODE_HEIGHT,
            fill="lightgreen", outline="black", width=2
        )
        self.canvas.create_text(
            x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2,
            text=str(value), font=("Arial", 14)
        )

    def draw_queue(self):
        self.canvas.delete("all")
        x = 20
        y = 60

        for value in self.queue:
            self.draw_node(x, y, value)
            x += NODE_WIDTH + HORIZONTAL_GAP

        if self.queue:
            self.canvas.create_text(20, 30, text="Front", font=("Arial", 12), fill="red")
            self.canvas.create_text(x - NODE_WIDTH - HORIZONTAL_GAP + 40, 30, text="Rear", font=("Arial", 12), fill="blue")

    def push_value(self):
        try:
            val = int(self.push_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter an integer value.")
            return

        self.queue.append(val)
        self.push_entry.delete(0, tk.END)
        self.status_label.config(text=f"Pushed {val} into queue")
        self.draw_queue()

    def pop_value(self):
        if not self.queue:
            messagebox.showinfo("Empty Queue", "Queue is empty. Cannot pop.")
            return

        val = self.queue.pop(0)
        self.status_label.config(text=f"Popped {val} from queue")
        self.draw_queue()

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueVisualizer(root)
    root.mainloop()