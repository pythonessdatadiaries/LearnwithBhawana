from flask import Flask,render_template,request,redirect

app = Flask(__name__)
print("Flask app created")

#Store wishes temporarily
wishes = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diyas')
def diyas():
    return render_template('diyas.html')

@app.route('/recipes')
def recipes():
    recipe_list = [
        {"name":"Laddoo","recipe": "Mix gram flour, sugar, and ghee, "
        "shape into balls, and decorate with nuts."},
        {"name":"Kaju Katli","recipe": "Blend cashews, sugar, "
         "and water into a smooth paste, cook until thick, and cut into diamond shapes."},
         {"name":"Gulab Jamun","recipe":"Fry milk-solid dumplings in oil, "
          "soak in sweet syrup flavored with rosewater and cardamom."}
    ]

    return render_template('recipes.html',recipes = recipe_list)

@app.route('/wishes',methods=['GET','POST'])
def wishes_page():
    if request.method == "POST":
        name = request.form.get('name')
        message = request.form.get('message')
        if name and message:
            wishes.append({'name':name,'message':message})
        return redirect('/wishes')
    return render_template('wishes.html',wishes=wishes)


if __name__ == '__main__':
    app.run(debug=True)

