import tkinter as tk
import math

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.draw_tomato()

    def draw_tomato(self):
        # Tomato body
        self.canvas.create_oval(50, 50, 350, 350, fill="red", outline="red")

        # Green stem
        self.canvas.create_polygon(200, 10, 180, 30, 220, 30, 200, 10, fill="green", outline="green")

if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()

# Source: Gemini