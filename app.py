import tkinter as tk
from tkinter import messagebox, scrolledtext
import time
import threading
from PIL import Image, ImageTk

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer with Markdown Editor")
        self.root.configure(bg="#2e2e2e")  # Dark background
        
        # Clock
        self.clock_label = tk.Label(root, font=("Helvetica", 48), bg="#2e2e2e", fg="#ff4500")
        self.clock_label.pack(pady=20)
        
        self.date_label = tk.Label(root, font=("Helvetica", 24), bg="#2e2e2e", fg="#ffffff")
        self.date_label.pack(pady=5)
        
        # 3D Pomodoro Apple Animation
        self.pomodoro_frame = tk.Frame(root, bg="#2e2e2e")
        self.pomodoro_frame.pack(pady=10)
        
        self.pomodoro_image = Image.open("pomodoro_apple.png")  # Load your 3D apple image
        self.pomodoro_image = self.pomodoro_image.resize((100, 100), Image.ANTIALIAS)
        self.pomodoro_photo = ImageTk.PhotoImage(self.pomodoro_image)
        
        self.pomodoro_label = tk.Label(self.pomodoro_frame, image=self.pomodoro_photo, bg="#2e2e2e")
        self.pomodoro_label.pack()
        
        # Markdown Editor
        self.md_frame = tk.Frame(root, bg="#2e2e2e")
        self.md_frame.pack(pady=20)
        
        self.md_label = tk.Label(self.md_frame, text="Markdown Task Editor", font=("Helvetica", 24), bg="#2e2e2e", fg="#ffffff")
        self.md_label.pack()
        
        self.md_text = scrolledtext.ScrolledText(self.md_frame, width=50, height=10, bg="#3e3e3e", fg="#ffffff", insertbackground='white')
        self.md_text.pack(pady=5)
        
        # Pomodoro Timer
        self.timer_label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 24), bg="#2e2e2e", fg="#ffffff")
        self.timer_label.pack(pady=20)
        
        self.timer_display = tk.Label(root, text="25:00", font=("Helvetica", 32), bg="#2e2e2e", fg="#ff4500")
        self.timer_display.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, bg="#ffa500", fg="white")
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, bg="#dc143c", fg="white")
        self.stop_button.pack(pady=5)
        
        self.time_left = 25 * 60  # 25 minutes in seconds
        self.timer_running = False
        
        self.update_clock()
        
        # Start the animation
        self.animate_pomodoro()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        
        current_date = time.strftime("%B %d %Y")
        self.date_label.config(text=current_date)
        
        self.clock_label.after(1000, self.update_clock)
        
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            threading.Thread(target=self.countdown).start()
        
    def stop_timer(self):
        self.timer_running = False
        
    def countdown(self):
        while self.time_left > 0 and self.timer_running:
            minutes, seconds = divmod(self.time_left, 60)
            self.timer_display.config(text=f"{minutes:02}:{seconds:02}")
            time.sleep(1)
            self.time_left -= 1
            
        if self.time_left == 0:
            messagebox.showinfo("Time's up!", "Take a short break!")
            self.time_left = 25 * 60  # Reset timer
            
    def animate_pomodoro(self):
        # Simple animation loop for the Pomodoro apple
        for _ in range(10):
            self.pomodoro_label.config(fg="#ff4500")
            self.root.update()
            time.sleep(0.5)
            self.pomodoro_label.config(fg="#ffffff")
            self.root.update()
            time.sleep(0.5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()