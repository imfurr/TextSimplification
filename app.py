from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

simplifier = pipeline("text2text-generation", model="t5-base")

@app.route("/", methods=["GET", "POST"])
def index():
    simplified_text = ""
    if request.method == "POST":
        text = request.form["text"]
        simplified_text = simplifier(text)[0]["generated_text"]
    return render_template("index.html", simplified_text=simplified_text)

if __name__ == "__main__":
    app.run(debug=True)