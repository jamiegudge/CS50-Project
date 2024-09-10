import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime, date
from math import ceil
from random import randint, choice
from copy import deepcopy

# a function to get the digits of a number
def getDigit(number, n):
    return number // 10**n % 10

# a function to create a blank sudoku
def blankSudoku():
    sudoku = []
    for i in range(9):
        lista = []
        for j in range(9):
            lista.append(0)
        sudoku.append(lista)
    return sudoku

# a function to find the next empty position
def emptyCell(sudoku):
    for x in range(0,9):
        for y in range(0,9):
            if sudoku[x][y] == 0:
                return x,y
    return -1,-1

# check whether a given entry, n, is legal in a given position, i,j
def validEntry(sudoku, i, j, n):
    # check legality in row
    for k in range(0,9):
        if sudoku[i][k] == n:
            return False
    # check legality in column
    for k in range(0,9):
        if sudoku[k][j] == n:
            return False
    # check legality in box
    for k in range((3 * (i//3)),(3 * (i//3) + 3)):
        for l in range((3 * (j//3)),(3 * (j//3) + 3)):
            if sudoku[k][l] == n:
                return False
    return True


# sudoku creator
def createFullSudoku(sudoku):
    l = list(range(1,10))
    for i in range(3):
        for j in range(3):
            num = choice(l)
            sudoku[i][j] = num
            l.remove(num)
    l = list(range(1,10))
    for i in range(3,6):
        for j in range(3,6):
            num = choice(l)
            sudoku[i][j] = num
            l.remove(num)
    l = list(range(1,10))
    for i in range(6,9):
        for j in range(6,9):
            num = choice(l)
            sudoku[i][j] = num
            l.remove(num)
    i,j = emptyCell(sudoku)
    if i == -1:
        return True
    for n in range(1,10):
        if validEntry(sudoku, i, j, n):
            sudoku[i][j] = n
            if solveSudoku(sudoku):
                return True
            sudoku[i][j] = 0
    return False

# solve the sudoku
def solveSudoku(sudoku):
    i,j = emptyCell(sudoku)
    if i == -1:
        return True
    for n in range(1,10):
        if validEntry(sudoku, i, j, n):
            sudoku[i][j] = n
            if solveSudoku(sudoku):
                return True
            sudoku[i][j] = 0
    return False

# solve the board recursively to check whether
def solveForNumberOfSolutions(sudoku, i, j):
    for n in range(1,10):
        if validEntry(sudoku, i, j, n):
            sudoku[i][j] = n
            if solveSudoku(sudoku):
                return sudoku
            sudoku[i][j] = 0
    return False

# find the a-th empty cell in a sudoku
def emptyCellsForNumberOfSolutions(sudoku, a):
    order = 1
    for x in range(0,9):
        for y in range(0,9):
            if sudoku[x][y] == 0:
                if order == a:
                    return x,y
                order += 1
    return False

# find the number of possible solutions to a given sudoku
def numberOfSolutions(sudoku):
    emptyCells = 0
    solutions = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                emptyCells += 1
    for k in range(1, (emptyCells + 1)):
        sudokuCopy = deepcopy(sudoku)
        i, j = emptyCellsForNumberOfSolutions(sudokuCopy, k)
        solution = solveForNumberOfSolutions(sudokuCopy, i, j)
        solution = "".join([str(i) for j in solution for i in j])
        solutions.append(solution)
    return list(set(solutions))

# take numbers out of the full sudoku to generate the puzzle, based on the difficulty
def createPuzzleSudoku(sudoku, diff):
    puzzle = deepcopy(sudoku)
    k = 0
    while k < 4:
        i = randint(0, 2)
        j = randint(0, 2)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            k +=1
    k = 0
    while k < 4:
        i = randint(3,5)
        j = randint(3,5)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            k +=1
    k = 0
    while k < 4:
        i = randint(6,8)
        j = randint(6,8)
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            k +=1
    if diff == 0:
        removal = 30
    elif diff == 1:
        removal = 34
    elif diff == 2:
        removal = 38
    elif diff == 3:
        removal = 42
    k = 0
    while k < removal:
        i = randint(0,8)
        j = randint(0,8)
        if puzzle[i][j] != 0:
            n = puzzle[i][j]
            puzzle[i][j] = 0
            if len(numberOfSolutions(puzzle)) != 1:
                puzzle[i][j] = n
                continue
            k += 1
    return sudoku, puzzle













# a function to check whether there are multiple of the same number in a box, column, or row of a sudoku
def legal_sudoku(sudoku):
    # go through each element in the sudoku, and record the current position in the sudoku
    for horiz, i in enumerate(sudoku):
        for vert, j in enumerate(i):
            # check the number is between 0 and 9
            if j < 0 or j > 9:
                return False
            if j != 0:
                count = 0
                # check whether the 3x3 box already contains that number
                for k in range(3*(ceil((horiz+1)/3))-3,3*(ceil((horiz+1)/3))):
                    for l in range(3*(ceil((vert+1)/3))-3,3*(ceil((vert+1)/3))):
                        if j == sudoku[k][l]:
                            count += 1
                if count == 0:
                    raise ValueError("legal sudoku check broken")
                if count > 1:
                    return False
                # check wether the row already contains that number
                count2 = 0
                for k in range(9):
                    if j == sudoku[k][vert]:
                        count2 += 1
                if count2 == 0:
                    raise ValueError("legal sudoku check broken")
                if count2 > 1:
                    return False
                # check wether the column already contains that number
                count3 = 0
                for k in range(9):
                    if j == sudoku[horiz][k]:
                        count3 += 1
                if count3 == 0:
                    raise ValueError("legal sudoku check broken")
                if count3 > 1:
                    return False
    return True