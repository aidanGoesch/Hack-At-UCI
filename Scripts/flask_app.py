from flask import Flask, request, render_template
import os
from moods_from_artist import get_display_song_list
from song_id_to_name import song_id_list_to_song_name_list, song_id_list_to_song_artist_list

port = os.environ.get("PORT", 5001)

app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        form_data = request.form
        print(form_data)
        song_list = get_display_song_list(form_data["artist"], form_data["mood"])
        song_names = song_id_list_to_song_name_list(song_list)
        artist_names = song_id_list_to_song_artist_list(song_list)
        return render_template("index.html", mood = form_data["mood"],
            artist = form_data["artist"], songs = song_names, artists = artist_names)
    return render_template("index.html", mood = "", artist = "", songs = [], artists = [])

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = port)