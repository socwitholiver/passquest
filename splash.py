import tkinter as tk
from PIL import Image, ImageTk
import time
import subprocess

def show_splash():
    root = tk.Tk()
    root.overrideredirect(True)  # remove window borders
    root.configure(bg="black")

    # Load splash image
    img = Image.open("static/images/splash.png")
    splash_img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=splash_img, bg="black")
    label.pack()

    # Center window
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = (img.width, img.height)
    x = (w // 2) - (size[0] // 2)
    y = (h // 2) - (size[1] // 2)
    root.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

    # Show for 3 seconds
    root.after(3000, root.destroy)
    root.mainloop()

    # Launch main app after splash
    subprocess.Popen(["python", "app.py"])

if __name__ == "__main__":
    show_splash()
