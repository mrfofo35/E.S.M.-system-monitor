import psutil
import tkinter as tk

root = tk.Tk()
root.geometry("250x340")
root.title("E.S.M.")
root.config(bg="#415e4d")

cpu_frame = tk.LabelFrame(root, relief="ridge", pady=1, padx=1, bg="gray")
cpu_frame.place(height=60, width=240, x=5, y=10)

cpu = tk.Label(cpu_frame, text="CPU=%0.0", font=("Times new roman", 10, "bold"), bg="gray")
cpu.place(x=0, y=0)

ram_frame = tk.LabelFrame(root, relief="ridge", pady=1, padx=1, bg="gray")
ram_frame.place(height=60, width=240, x=5, y=80)

ram = tk.Label(ram_frame, text="RAM=%0.0", font=("Times new roman", 10, "bold"), bg="gray")
ram.place(x=0, y=0)

disk_frame = tk.LabelFrame(root, relief="ridge", pady=1, padx=1, bg="gray")
disk_frame.place(height=60, width=240, x=5, y=150)

disk = tk.Label(disk_frame, text="DISK=%0.0", font=("Times new roman", 10, "bold"), bg="gray")
disk.place(x=0, y=0)


def update_stats():
    cpu_val = psutil.cpu_percent(interval=None)
    ram_val = psutil.virtual_memory().percent
    disk_val = psutil.disk_usage('/').percent
    
    cpu.config(text=f"CPU=%{cpu_val}")
    ram.config(text=f"RAM=%{ram_val}")
    disk.config(text=f"DISK=%{disk_val}")
    root.after(1000, update_stats)
update_stats()


root.mainloop()