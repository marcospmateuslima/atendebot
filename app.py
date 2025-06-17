from flask import Flask, render_template, request
from chatbot import responder

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        resposta = responder(pergunta)
    return render_template("index.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)
