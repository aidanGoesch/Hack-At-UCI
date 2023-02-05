
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

function load_webpage() {
    let mood = document.getElementById("mood").innerHTML
    let artist = document.getElementById("artist").innerHTML

    if (mood !== "") {
        // on the second time it's been reloaded

        document.getElementById("artistInput").value = artist
        document.getElementById("moodButton").value = mood
        document.getElementsByTagName("body")[0].style.backgroundColor = COLORS[MOODS.indexOf(mood)]


        for (let i = 0; i < 2; i++) {
            let input = document.getElementsByClassName("inputs")[i]

            input.style.animationName = "inputRise"

            // add animation to mood input to look like its scrolled up
            input.style.animationName = "inputRise"
            input.style.animationDuration = "2s"
            input.style.animationFillMode = "forwards"
            input.style.animationDelay = "0.5s"
        }


    }

}