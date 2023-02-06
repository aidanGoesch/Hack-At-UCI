
MOODS = ["Happy", "Sad", "Chill", "Hype", "Angry"]
COLORS = ["#DFDF00", "#3154FF", "#8A2BE2", "#11FF44", "#880000"]

function change_button() {
    let mood = document.getElementById("moodButton").value
    let index = MOODS.indexOf(mood)
    index++
    if (index >= MOODS.length) {
        index-= MOODS.length
    }
    document.getElementById("moodButton").value = MOODS[index]
    document.getElementsByTagName("body")[0].style.backgroundColor = COLORS[index]
    document.getElementById("moodInput").value = MOODS[index]
}

function start_loading() {
    document.getElementById("loadingBar").hidden = false
    document.getElementById("artistInput").value = document.getElementById("artistField").value

    disable_inputs()
}

function disable_inputs() {
    document.getElementById("moodButton").disabled = true
    document.getElementById("artistField").disabled = true
}

function load_webpage() {
    let mood = document.getElementById("mood").innerHTML
    let artist = document.getElementById("artist").innerHTML
    let songs = string_to_list(document.getElementById("songs").innerHTML)
    let artists = string_to_list(document.getElementById("artists").innerHTML)

    if (mood !== "") {
        // on the second time the page has been loaded

        disable_inputs()

        // update text and background color
        document.getElementById("artistField").value = artist
        document.getElementById("moodButton").value = mood
        document.getElementsByTagName("body")[0].style.backgroundColor = COLORS[MOODS.indexOf(mood)]

        for (let i = 0; i < document.getElementsByClassName("inputs").length; i++) {
            let input = document.getElementsByClassName("inputs")[i]

            // add animation to mood input to look like its scrolled up
            input.style.animationName = "inputRise"
            input.style.animationDuration = "2s"
            input.style.animationFillMode = "forwards"
            input.style.animationDelay = "0.25s"
        }

        // add animation to songs output for similar effect
        let output = document.getElementById("songTable")
        output.style.animationName = "outputRise"
        output.style.animationDuration = "4s"
        output.style.animationFillMode = "forwards"
        output.style.animationDelay = "0"

        // create table
        let table = document.getElementById("songTable")
        table.hidden = false
        table.innerHTML = "<tr><th>Artist</th><th>Song</th></tr>"

        for (let i = 0; i < songs.length; i++) {
            table.innerHTML+= "<tr><td>" + artists[i] + "</td><td>" + songs[i] + "</td></tr>"
        }
    }
}

function string_to_list(songs) {
    let doubleQuotedSongs = songs.replace(/'/g, '"');
    return JSON.parse(doubleQuotedSongs)
}

