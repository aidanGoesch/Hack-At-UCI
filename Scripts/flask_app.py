from flask import Flask, request, render_template
import os
from moods_from_artist import get_display_song_list

port = os.environ.get("PORT", 5001)

app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        form_data = request.form
        song_list = get_display_song_list(form_data["mood"], form_data["artist"])
        return render_template("index.html", mood = form_data["mood"], artist = form_data["artist"])
    return render_template("index.html", mood = "", artist = "")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = port)