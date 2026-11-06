
import graphics


def getFrequencies(filename):
    counts = [0] * 256

    with open(filename, "r", encoding="utf-8") as infile:
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
    win = graphics.GraphWin("Letter Frequency Analysis", 800, 600)

    win.setBackground("white")

    highest = max(frequencies)

    if highest == 0:
        highest = 1

    # Draw the graph title
    title = graphics.Text(graphics.Point(400, 25), "Letter Frequency Analysis")
    title.setSize(18)
    title.draw(win)

    # Draw the axes
    graphics.Line(graphics.Point(60, 520), graphics.Point(760, 520)).draw(win)
    graphics.Line(graphics.Point(60, 60), graphics.Point(60, 520)).draw(win)

    bar_width = 22
    gap = 4

    for i in range(26):
        x = 75 + i * (bar_width + gap)

        bar_height = (frequencies[i] / highest) * 400

        bar = graphics.Rectangle(
            graphics.Point(x, 520 - bar_height),
            graphics.Point(x + bar_width, 520)
        )

        bar.setFill("blue")
        bar.draw(win)

        letter = chr(ord("A") + i)

        label = graphics.Text(graphics.Point(x + bar_width / 2, 540), letter)
        label.draw(win)

    # Display the maximum frequency
    max_label = graphics.Text(
        graphics.Point(400, 570),
        "Maximum frequency: {:.4f}".format(max(frequencies))
    )
    max_label.draw(win)

    win.getMouse()
    win.close()


def main():
    filename = input("Enter the name of the text file: ")

    frequencies = getFrequencies(filename)

    print("\nLetter Frequency Results")

    for i in range(26):
        letter = chr(ord("A") + i)

        print("{}: {:.4f}".format(letter, frequencies[i]))

    drawGraph(frequencies)


if __name__ == "__main__":
    main()
