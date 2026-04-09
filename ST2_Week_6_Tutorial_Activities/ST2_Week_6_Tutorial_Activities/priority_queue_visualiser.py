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
        self.root.title("Queue Visualiser (FIFO)")

        self.queue = []

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack(pady=20)

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Label(control_frame, text="Enqueue Value:").grid(row=0, column=0)
        self.enqueue_entry = tk.Entry(control_frame, width=10)
        self.enqueue_entry.grid(row=0, column=1)

        enqueue_btn = tk.Button(control_frame, text="Enqueue", command=self.enqueue)
        enqueue_btn.grid(row=0, column=2, padx=10)

        dequeue_btn = tk.Button(control_frame, text="Dequeue", command=self.dequeue)
        dequeue_btn.grid(row=1, column=2, pady=10)

        self.status_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.status_label.pack(pady=5)

        self.draw_queue()

    def draw_node(self, x, y, value):
        self.canvas.create_rectangle(
            x, y, x + NODE_WIDTH, y + NODE_HEIGHT,
            fill="lightblue", outline="black", width=2
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
            self.canvas.create_text(20, 30, text="Front", font=("Arial", 12))
            self.canvas.create_text(x - NODE_WIDTH - HORIZONTAL_GAP + 40, 30, text="Rear", font=("Arial", 12))

    def enqueue(self):
        try:
            val = int(self.enqueue_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Enter a valid integer.")
            return

        self.queue.append(val)
        self.enqueue_entry.delete(0, tk.END)
        self.status_label.config(text=f"Enqueued {val}")
        self.draw_queue()

    def dequeue(self):
        if not self.queue:
            messagebox.showinfo("Empty Queue", "Queue is empty.")
            return

        val = self.queue.pop(0)
        self.status_label.config(text=f"Dequeued {val}")
        self.draw_queue()

if __name__ == "__main__":
    root = tk.Tk()
    app = QueueVisualizer(root)

    # Optional: Preload test data
    # for v in [10,20,30,40,50]:
    #     app.queue.append(v)
    # app.draw_queue()

    root.mainloop()