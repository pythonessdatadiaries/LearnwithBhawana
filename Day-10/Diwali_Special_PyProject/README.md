# 🪔 PyWali Diwali – A Flask Web App to Celebrate Diwali with Code 🎇

A fun Python Flask project to celebrate Diwali!  
This web app includes Diya designs, festive recipes, and an email-based wish sender.

---

## 🌟 Features
- 🪔 **Diyas Page:** Displays a beautiful diya image.
- 🍬 **Recipes Page:** Lists Diwali sweets & snacks.
- 💌 **Wishes Page:** Lets users send Diwali wishes (with email feature).

---

## 🧩 Project Structure

| File / Folder | Description |
|----------------|-------------|
| `app.py` | Main Flask application file handling routes and logic. |
| `templates/` | Contains HTML templates (`index.html`, `diyas.html`, `recipes.html`, `wishes.html`, `base.html`). |
| `static/` | Folder for images like `diya.jpg` and other static assets. |
| `wishes.html` | Form page where users send wishes via email. |
| `recipes.html` | Shows list of traditional Diwali recipes. |
| `diyas.html` | Displays diya artwork/image to add festive touch. |
| `base.html` | Template base for consistent styling and navigation. |
| `README.md` | This file — explains project setup and structure. |

---

## 🚀 How to Run Locally
```bash
pip install flask
python app.py(for windows)
python3 app.py(for Mac/Linux)
```
---

## Steps to download and run the project:

- Clone the repo (HTTPS — no SSH setup needed) git clone https://github.com/pythonessdatadiaries/LearnwithBhawana.git cd LearnwithBhawana

- (Optional) Switch to the branch used in the repo git fetch origin git checkout Python-Projects

- Create and activate a Python virtual environment python3 -m venv .venv source .venv/bin/activate

- Install dependencies (if present) pip install flask

- Run the project (pick the appropriate command)

- Flask: export FLASK_APP=app.py # macOS/Linux flask run

- Basic workflow to make & push changes : 
  - git checkout -b my-change
  - git add -A
  - git commit -m "Describe change"
  - git push -u origin my-change
(If git asks for credentials, use gh auth login or create a fine‑grained Personal Access Token with Repository > Contents: Read & write and use it as the password.)


