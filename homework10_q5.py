
from graphics import *
from urllib.request import urlopen


def getFrequencies(url):
    counts = [0] * 256

    response = urlopen(url)

    text = response.read().decode("utf-8", errors="replace")

    text = text.upper()

    for char in text:
        value = ord(char)

        if value < 256:
            counts[value] += 1

    return counts


def drawGraph(counts):
    total = sum(counts[ord("A"):ord("Z") + 1])

    frequencies = []

    for letter in range(ord("A"), ord("Z") + 1):

        if total > 0:
            ratio = counts[letter] / total
        else:
            ratio = 0

        frequencies.append(ratio)

    win = GraphWin("Online Book Frequency Analysis", 800, 600)

    win.setBackground("white")

    highest = max(frequencies)

    if highest == 0:
        highest = 1

    title = Text(
        Point(400, 25),
        "Project Gutenberg Letter Frequency"
    )

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

        bar.setFill("red")
        bar.draw(win)

        letter = chr(ord("A") + i)

        Text(Point(x + bar_width / 2, 540), letter).draw(win)

    win.getMouse()
    win.close()


def saveFrequencies(counts, filename):
    with open(filename, "w") as outfile:

        outfile.write("Letter,Count\n")

        for letter in range(ord("A"), ord("Z") + 1):

            character = chr(letter)

            outfile.write(
                "{},{}\n".format(character, counts[letter])
            )

    print("Frequency data saved to", filename)


def main():
    print("Online Book Frequency Analysis")

    print("\nAvailable Project Gutenberg books:")
    print("1. Complete Works of William Shakespeare")
    print("2. King James Version of the Bible")

    choice = input("Select a book (1 or 2): ")

    if choice == "1":
        url = "https://gutenberg.org/cache/epub/100/pg100.txt"

    elif choice == "2":
        url = "https://gutenberg.org/cache/epub/10/pg10.txt"

    else:
        print("Invalid selection.")
        return

    try:
        counts = getFrequencies(url)

        print("\nFrequency Analysis Complete!")

        filename = input(
            "Enter a file name to save the frequency data: "
        )

        saveFrequencies(counts, filename)

        drawGraph(counts)

    except Exception as error:
        print("An error occurred:", error)


if __name__ == "__main__":
    main()
