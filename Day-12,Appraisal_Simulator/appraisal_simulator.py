import tkinter as tk
from PIL import Image, ImageTk

def appraisal():
    # Inputs
    self_rating = int(self_entry.get())
    vibe = vibe_var.get()
    revenue = revenue_var.get()

    # Logic
    if (
        (self_rating >= 4 and vibe in ["Good", "Okay"] and revenue == "Yes")
        or
        (self_rating >= 4 and revenue == "No")
        or
        (vibe == "Good" and revenue == "Yes")
    ):
        result = "🎉 Lollipop 🍭\nManager: You're a Rockstar! (hike is decent 😄)"
        img_label.config(image=lollipop_img)
    else:
        result = "🥜 Peanut\nManager: Efforts were good… but budget is tight this year 🙂"
        img_label.config(image=peanut_img)

    result_label.config(text=result)


# UI Setup
root = tk.Tk()
root.title("Appraisal Simulator 😅")
root.geometry("350x450")

# Load Images
peanut_img = ImageTk.PhotoImage(Image.open("peanut.png").resize((150,150)))
lollipop_img = ImageTk.PhotoImage(Image.open("lollipop.png").resize((150,150)))

# Inputs
tk.Label(root, text="Self Appraisal (1-5):").pack()
self_entry = tk.Entry(root)
self_entry.pack()

tk.Label(root, text="Manager Vibe All Year:").pack()
vibe_var = tk.StringVar(value="Okay")
tk.OptionMenu(root, vibe_var, "Good", "Okay", "Bad").pack()

tk.Label(root, text="Company Revenue Better Than Last Year?").pack()
revenue_var = tk.StringVar(value="No")
tk.OptionMenu(root, revenue_var, "Yes", "No").pack()

# Button
tk.Button(root, text="Check Appraisal", command=appraisal,
          bg="white", fg="black").pack(pady=15)

# Image Display
img_label = tk.Label(root)
img_label.pack()

# Result Text
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()