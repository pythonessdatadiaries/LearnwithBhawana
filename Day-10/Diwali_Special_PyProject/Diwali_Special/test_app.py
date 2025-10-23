from flask import Flask

app = Flask(__name__)
print("app created")
@app.route('/')
def home():
    return "Hello,Flask working fine!"

if __name__ == '__main__':
    app.run(debug=True)