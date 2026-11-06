from graphics import *
from graphics import Line
import os


def getFrequencies(folder):
    counts = [0] * 256

    for filename in os.listdir(folder):

        if filename.endswith(".py"):

            filepath = os.path.join(folder, filename)

            with open(filepath, "r", encoding="utf-8",
                      errors="replace") as infile:

                text = infile.read().upper()

                for char in text:
                    value = ord(char)

                    if value < 256:
                        counts[value] += 1

    total = sum(counts[ord("A"):ord("Z") + 1])

    frequencies = []

    for letter in range(ord("A"), ord("Z") + 1):

        if total > 0:
            ratio = counts[letter] / total
        else:
            ratio = 0

        frequencies.append(ratio)

    return frequencies


def drawGraph(frequencies):
    win = GraphWin("Python Code Frequency", 800, 600)

    win.setBackground("white")

    highest = max(frequencies)

    if highest == 0:
        highest = 1

    title = Text(Point(400, 25),
                 "Python Program Letter Frequency")
    title.setSize(18)
    title.draw(win)

    Line(Point(60, 520), Point(760, 520)).draw(win)
    Line(Point(60, 60), Point(60, 520)).draw(win)

    bar_width = 22
    gap = 4

    for i in range(26):
        x = 75 + i * (bar_width + gap)

        bar_height = (frequencies[i] / highest) * 400

        bar = Rectangle(
            Point(x, 520 - bar_height),
            Point(x + bar_width, 520)
        )

        bar.setFill("green")
        bar.draw(win)

        letter = chr(ord("A") + i)

        Text(Point(x + bar_width / 2, 540), letter).draw(win)

    win.getMouse()
    win.close()


def main():
    folder = input("Enter the directory containing Python files: ")

    frequencies = getFrequencies(folder)

    print("\nPython Code Frequency Analysis")

    for i in range(26):
        letter = chr(ord("A") + i)

        print("{}: {:.4f}".format(letter, frequencies[i]))

    drawGraph(frequencies)


if __name__ == "__main__":
    main()
