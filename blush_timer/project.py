import tkinter as tk
from tkinter import PhotoImage
import time
import math

# ... (Previous functions: start_timer, start_pomodoro, format_time)

def update_timer_display(canvas, seconds, total_seconds):
    """Updates the radial countdown and timer text on the canvas."""
    canvas.delete("timer")  # Clear previous timer elements
    mins, secs = divmod(seconds, 60)
    timer_text = '{:02d}:{:02d}'.format(mins, secs)
    canvas.create_text(150, 180, text=timer_text, font=("Arial", 24), tags="timer")

    # Draw the radial countdown
    angle = 360 * (seconds / total_seconds)
    canvas.create_arc(20, 20, 280, 280, start=90, extent=-angle, style=tk.ARC, width=5, outline="red", tags="timer")

def pomodoro_gui(work_minutes=25, break_minutes=5):
    """GUI for the Pomodoro timer."""
    window = tk.Tk()
    window.title("Pomodoro Timer")

    # Load the tomato image
    tomato_img = PhotoImage(file="tomato.png")  # Replace with your image
    tomato_label = tk.Label(window, image=tomato_img)
    tomato_label.pack()

    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack()

    # Calculate total work time in seconds
    total_work_seconds = work_minutes * 60

    # Start the timer
    work_seconds = total_work_seconds
    while work_seconds:
        update_timer_display(canvas, work_seconds, total_work_seconds)
        window.update()  # Update the GUI
        time.sleep(1)
        work_seconds -= 1

    # ... (Add break timer logic here)

    window.mainloop()

def main():
    """Main function to start the Pomodoro timer GUI."""
    pomodoro_gui()

if __name__ == "__main__":
    main()