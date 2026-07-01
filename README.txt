===========================================================================
NUMBER GUESSING GAME - FLASK WEB APPLICATION
===========================================================================

Hello there and welcome!
What we have here is a simple and fun number guessing game built with Python Flask. The game generates
a random number between 0 and 9, and the player guesses it through the URL.

===========================================================================
GAME DESCRIPTION
===========================================================================

This is a web-based number guessing game where:

 - A random number between 0 and 9 is generated when the server starts

 - Players guess the number by adding their guess to the URL

 - The game provides visual feedback

===========================================================================
HOW TO RUN THE PROGRAM
===========================================================================

PREREQUISITES:

Python 3.x installed on your system

Flask framework installed

INSTALLATION STEPS:

Install Flask:
pip install flask

Save the Code:

Copy the code into a file named "app.py" (or any name you prefer with .py extension)

Run the Application:
python app.py

Access the Game:

Open your web browser

Go to: http://127.0.0.1:5000

===========================================================================
HOW TO PLAY
===========================================================================


STEP 1: Start the Game

Navigate to http://127.0.0.1:5000

You'll see a welcome page with a GIF and instructions to guess a number between 0 and 9

STEP 2: Make a Guess

In your browser's address bar, add your number guess to the URL

Example: http://127.0.0.1:5000/5

STEP 3: Get Feedback
The game will display one of three responses:

Guess is TOO LOW: "Too low, try again!" with a sad GIF

Guess is TOO HIGH: "Too high, try again!" with a surprised GIF

Guess is CORRECT: "Congratulations! You guessed!" with a celebration GIF

IMPORTANT NOTE:
The random number is generated when the Flask server starts. The same number
persists until the server is restarted.

===========================================================================
TROUBLESHOOTING
===========================================================================

ISSUE: Flask not found
SOLUTION: Install Flask - pip install flask

ISSUE: Port already in use
SOLUTION: Change port - app.run(port=5001)

ISSUE: GIFs not loading
SOLUTION: Check internet connection (GIFs are external links)

ISSUE: Number guessing not working
SOLUTION: Ensure you're entering numbers only in the URL

===========================================================================
FILE STRUCTURE
===========================================================================


your-project/
├── app.py # Main application file
└── README.txt # This file

===========================================================================
CREDITS
===========================================================================

- Project: "100 Days of Code: The Complete Python Pro Bootcamp" - Day 55

===========================================================================
CONTRIBUTING
===========================================================================


Feel free to modify and enhance the game!

===========================================================================
HAVE FUN GUESSING! 🎯
===========================================================================
