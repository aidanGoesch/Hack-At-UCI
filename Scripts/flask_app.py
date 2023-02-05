from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder='static')

def do_something(text1, text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine

@app.route('/')
def process():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5001)