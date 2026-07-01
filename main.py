from flask import Flask
import random

app = Flask(__name__)

numbers_gif = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ZreWlqNnBwYmRlZ2I5NDgzbHpuN3owNW55M3U2Y2xxNzBob2JoOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif"
sad_gif = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGp6ZWYwYzdrOHh0cXRkYWhwajdhcDZ3Nmk2MG8wd2x1ZmUyMHA3YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4V3RuU0zSq1SC8Hh4x/giphy.gif"
too_high_gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGFmNGN6cWZjamluZ2JnMmVuaHZ3YTQyNHJicW1rczd6Z203cXN1ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2cei8MJiL2OWga5XoC/giphy.gif"
correct_answer_gif = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXVvanV1bHhkdWs0ampxZnBra2IxNTQ1ZHRwbjgzNTRmd2w1eHE4eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SSE36LAhb1m9dHz7HI/giphy.gif"

@app.route("/")
def opening_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
           "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ZreWlqNnBwYmRlZ2I5NDgzbHpuN3owNW55M3U2Y2xxNzBob2JoOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif'>")

correct_number = random.randint(0, 9)
print(correct_number)

@app.route("/<int:number>")
def guessing(number):
    if number < correct_number:
        return ("<h2>Too low, try again!</h2>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGp6ZWYwYzdrOHh0cXRkYWhwajdhcDZ3Nmk2MG8wd2x1ZmUyMHA3YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4V3RuU0zSq1SC8Hh4x/giphy.gif'>")

    elif number > correct_number:
        return ("<h2>Too high, try again!</h2>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGFmNGN6cWZjamluZ2JnMmVuaHZ3YTQyNHJicW1rczd6Z203cXN1ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2cei8MJiL2OWga5XoC/giphy.gif'>")

    else:
        return ("<h2>Congratulations!You guessed!<h2>"
                "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXVvanV1bHhkdWs0ampxZnBra2IxNTQ1ZHRwbjgzNTRmd2w1eHE4eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SSE36LAhb1m9dHz7HI/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)