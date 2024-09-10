import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime, date
from checker import createFullSudoku, createPuzzleSudoku, blankSudoku, getDigit
import random

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/easy", methods=["GET", "POST"])
def easy():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        # create a blank sudoku
        sudoku = blankSudoku()

        # create the full sudoku
        createFullSudoku(sudoku)

        # generate the sudoku puzzle and solution
        global solution
        global puzzle
        global error
        solution, puzzle = createPuzzleSudoku(sudoku, 0)
        error = 0

        return render_template("easy.html", sudoku = puzzle, error = error)


    elif request.method == "POST":
        # take entry box
        global row
        global col
        box = request.form.get("box")
        row = getDigit(int(box),1)
        col = getDigit(int(box),0)
        # reset error
        error = 0


        return render_template("eButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    else:
        return render_template("index.html")

@app.route("/eButtons", methods=["GET", "POST"])
def eButtons():
    if request.method == "GET":

        return render_template("eButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    elif request.method == "POST":

        error = 0

        #check whether the given input matches the solution
        entry = request.form.get("entry")
        if solution[row][col] == int(entry):
            puzzle[row][col] = int(entry)
        else:
            error = "That is not correct!"
        # check whether the soduko is solved
        if puzzle == solution:
            error = "Congratulations, you solved the puzzle!"

        return render_template("easy.html", sudoku = puzzle, error = error, entry = entry)

@app.route("/medium", methods=["GET", "POST"])
def medium():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        # create a blank sudoku
        sudoku = blankSudoku()

        # create the full sudoku
        createFullSudoku(sudoku)

        # generate the sudoku puzzle and solution
        global solution
        global puzzle
        global error
        solution, puzzle = createPuzzleSudoku(sudoku, 1)
        error = 0

        return render_template("medium.html", sudoku = puzzle, error = error)


    elif request.method == "POST":
        # take entry box
        global row
        global col
        box = request.form.get("box")
        row = getDigit(int(box),1)
        col = getDigit(int(box),0)
        # reset error
        error = 0


        return render_template("mButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    else:
        return render_template("index.html")

@app.route("/mButtons", methods=["GET", "POST"])
def mButtons():
    if request.method == "GET":

        return render_template("mButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    elif request.method == "POST":

        error = 0

        #check whether the given input matches the solution
        entry = request.form.get("entry")
        if solution[row][col] == int(entry):
            puzzle[row][col] = int(entry)
        else:
            error = "That is not correct!"
        # check whether the soduko is solved
        if puzzle == solution:
            error = "Congratulations, you solved the puzzle!"

        return render_template("medium.html", sudoku = puzzle, error = error, entry = entry)

@app.route("/hard", methods=["GET", "POST"])
def hard():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        # create a blank sudoku
        sudoku = blankSudoku()

        # create the full sudoku
        createFullSudoku(sudoku)

        # generate the sudoku puzzle and solution
        global solution
        global puzzle
        global error
        solution, puzzle = createPuzzleSudoku(sudoku, 2)
        error = 0

        return render_template("hard.html", sudoku = puzzle, error = error)


    elif request.method == "POST":
        # take entry box
        global row
        global col
        box = request.form.get("box")
        row = getDigit(int(box),1)
        col = getDigit(int(box),0)
        # reset error
        error = 0


        return render_template("hButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    else:
        return render_template("index.html")

@app.route("/hButtons", methods=["GET", "POST"])
def hButtons():
    if request.method == "GET":

        return render_template("hButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    elif request.method == "POST":

        error = 0

        #check whether the given input matches the solution
        entry = request.form.get("entry")
        if solution[row][col] == int(entry):
            puzzle[row][col] = int(entry)
        else:
            error = "That is not correct!"
        # check whether the soduko is solved
        if puzzle == solution:
            error = "Congratulations, you solved the puzzle!"

        return render_template("hard.html", sudoku = puzzle, error = error, entry = entry)

@app.route("/extreme", methods=["GET", "POST"])
def extreme():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":
        # create a blank sudoku
        sudoku = blankSudoku()

        # create the full sudoku
        createFullSudoku(sudoku)

        # generate the sudoku puzzle and solution
        global solution
        global puzzle
        global error
        solution, puzzle = createPuzzleSudoku(sudoku, 3)
        error = 0

        return render_template("extreme.html", sudoku = puzzle, error = error)


    elif request.method == "POST":
        # take entry box
        global row
        global col
        box = request.form.get("box")
        row = getDigit(int(box),1)
        col = getDigit(int(box),0)
        # reset error
        error = 0


        return render_template("xButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    else:
        return render_template("index.html")

@app.route("/xButtons", methods=["GET", "POST"])
def xButtons():
    if request.method == "GET":

        return render_template("xButtons.html", sudoku = puzzle, error = error, row = row, col = col)

    elif request.method == "POST":

        error = 0

        #check whether the given input matches the solution
        entry = request.form.get("entry")
        if solution[row][col] == int(entry):
            puzzle[row][col] = int(entry)
        else:
            error = "That is not correct!"
        # check whether the soduko is solved
        if puzzle == solution:
            error = "Congratulations, you solved the puzzle!"

        return render_template("extreme.html", sudoku = puzzle, error = error, entry = entry)

