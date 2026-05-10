from tkinter import *
from tkinter import messagebox
from google import genai

# ---------------- AI SETUP ---------------- #

client = genai.Client(api_key="YOUR_API_KEY")

# ---------------- FUNCTION ---------------- #

def generate_letter():
    
    your_name = your_name_entry.get()
    mom_name = mom_name_entry.get()
    memory = memory_entry.get("1.0", END)

    if not your_name or not mom_name or not memory.strip():
        messagebox.showwarning("Missing Info", "Please fill all fields 🌸")
        return

    prompt = f"""
    Write a heartfelt Mother's Day letter
    from {your_name} to {mom_name}.

    Include this memory:
    "{memory}"

    Make it emotional, warm, and genuine.
    Write in 3 short paragraphs.

    Start with:
    Dear {mom_name},
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        output_text.delete("1.0", END)
        output_text.insert(END, response.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- UI ---------------- #

root = Tk()
root.title("🌸 Mother's Day AI Letter Generator")
root.geometry("700x750")
root.config(bg="#fff0f5")

# ---------------- TITLE ---------------- #

title = Label(
    root,
    text="🌸 AI Letter For Mom 🌸",
    font=("Helvetica", 24, "bold"),
    bg="#fff0f5",
    fg="#d63384"
)

title.pack(pady=20)

# ---------------- FLOWER DECORATION ---------------- #

flower = Label(
    root,
    text="🌷 🌸 🌹 🌺 🌼",
    font=("Helvetica", 22),
    bg="#fff0f5"
)

flower.pack()

# ---------------- NAME INPUT ---------------- #

Label(
    root,
    text="Your Name",
    font=("Helvetica", 14, "bold"),
    bg="#fff0f5"
).pack(pady=5)

your_name_entry = Entry(
    root,
    width=40,
    font=("Helvetica", 14)
)

your_name_entry.pack(pady=5)

# ---------------- MOM NAME ---------------- #

Label(
    root,
    text="Mom's Name",
    font=("Helvetica", 14, "bold"),
    bg="#fff0f5"
).pack(pady=5)

mom_name_entry = Entry(
    root,
    width=40,
    font=("Helvetica", 14)
)

mom_name_entry.pack(pady=5)

# ---------------- MEMORY INPUT ---------------- #

Label(
    root,
    text="Favorite Memory ❤️",
    font=("Helvetica", 14, "bold"),
    bg="#fff0f5"
).pack(pady=5)

memory_entry = Text(
    root,
    width=55,
    height=5,
    font=("Helvetica", 12),
    bd=2
)

memory_entry.pack(pady=10)

# ---------------- BUTTON ---------------- #

generate_btn = Button(
    root,
    text="✨ Generate Letter ✨",
    font=("Helvetica", 16, "bold"),
    bg="#ff69b4",
    fg="white",
    padx=15,
    pady=10,
    command=generate_letter
)

generate_btn.pack(pady=20)

# ---------------- OUTPUT ---------------- #

output_text = Text(
    root,
    width=70,
    height=15,
    font=("Georgia", 13),
    wrap=WORD,
    bg="#fffafc",
    fg="#444"
)

output_text.pack(pady=20)

# ---------------- FOOTER ---------------- #

footer = Label(
    root,
    text="Made with ❤️ using Python + AI",
    font=("Helvetica", 11),
    bg="#fff0f5",
    fg="gray"
)

footer.pack(pady=10)

root.mainloop()