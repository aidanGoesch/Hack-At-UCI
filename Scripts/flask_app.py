from flask import Flask, request, render_template
import os

port = os.environ.get("PORT", 5001)


app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        form_data = request.form
        return render_template("index.html", stage = form_data["artist"])
    return render_template("index.html", stage = "1")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = port)