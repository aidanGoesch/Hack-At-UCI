from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        form_data = request.form
        return render_template("index.html", stage = form_data["mood"])
    return render_template("index.html", stage = "1")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5001)