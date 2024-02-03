from flask import Flask, render_template

lista = ["Giovanni", "Maria", "Giuseppe", "Anna", "Luca", "Sofia", "Marco", "Giulia", "Alessandro", "Martina"]

app = Flask(__name__)

@app.route('/')
def index():
    nome = "auridebson"
    idade = 39
    return render_template('index.html', nome=nome, idade=idade, lista=lista)

if __name__ == "__main__":
    app.run(debug=True)