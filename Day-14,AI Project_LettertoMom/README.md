# 🌸 AI Mother's Day Letter Generator 🌸 

A beautiful beginner-friendly Python AI project that generates emotional Mother's Day letters using **Google Gemini AI** and a **Tkinter GUI**.

Perfect for:
- Python beginners
- AI beginners
- Portfolio projects
- YouTube/Instagram coding content

---

# Features ✨ 

✅ Beautiful Tkinter UI  
✅ Flower-themed interface 🌸  
✅ AI-generated emotional letters  
✅ Beginner-friendly code  
✅ Uses Google Gemini API  
✅ Real-world AI integration

---

# Demo

The app asks for:
- Your Name
- Mom's Name
- Favorite Memory

And AI generates a heartfelt personalized letter ❤️

---

#Project Setup (Beginner Friendly)

---

# 1. Clone This Project

Open terminal and run:

```bash
git clone YOUR_GITHUB_REPO_LINK
```
---
Go inside the project folder:

```bash
cd PROJECT_FOLDER_NAME
```
---

# 2. Create Virtual Environment:

```bash
python -m venv .venv
cd .venv\Scripts\activate
```
---

# 3. Install Required Libraries:
(Tkinter usually comes preinstalled with Python.)
```bash
pip install google-genai
```
---

# 4. Generate Free Gemini API Key

Go to:
https://aistudio.google.com/apikey

Steps:
Login with Google account
Click Create API Key
Copy your API key
---

# 5.Add Your API Key

Open: letter_to_mom.py

Find this line:
client = genai.Client(api_key="YOUR_API_KEY")

Replace:
YOUR_API_KEY
with your real Gemini API key.

Example:
client = genai.Client(api_key="AIzaSyXXXXXXX")

---

# 6. Which Gemini Model To Use?

Use:
model="gemini-1.5-flash" or model="gemini-flash-latest"

Why?

- Works well on free tier
- Fast responses
- Beginner friendly
- Good for text generation

Avoid preview/research models because they may require billing.

---

# 7.Run The Project
```bash
python letter_to_mom.py
```

---

## What You Can Learn From This Project

- Python basics
- Tkinter GUI development
- API integration
- Prompt engineering
- AI application development
- User input handling
- Real-world mini AI projects

## Tech Stack
- Python
- Tkinter
- Google Gemini API
- google-genai SDK

  ---
### 🌸 Made With Love 🌸 
Built using Python + AI ❤️
