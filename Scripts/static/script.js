
MOODS = ["Happy", "Sad", "Chill", "Hype", "Angry"]
COLORS = ["#FFFF00", "#3154FF", "#8A2BE2", "#11FF44", "#880000"]

function change_button() {
    let mood = document.getElementById("moodButton").value
    let index = MOODS.indexOf(mood)
    index++
    if (index >= MOODS.length) {
        index-= MOODS.length
    }
    document.getElementById("moodButton").value = MOODS[index]
    document.getElementsByTagName("body")[0].style.backgroundColor = COLORS[index]
}

function load_webpage() {
    let stage = document.getElementById("stage").innerHTML

    if (stage !== "1") {
        // on the second time it's been reloaded

        for (let i = 0; i < 2; i++) {
            let input = document.getElementsByClassName("inputs")[i]

            input.value = stage
            input.style.animationName = "inputRise"

            // add animation to mood input to look like its scrolled up
            input.style.animationName = "inputRise"
            input.style.animationDuration = "2s"
            input.style.animationFillMode = "forwards"
        }


    }

}