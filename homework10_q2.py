
import ast


def readPath(filename):
    with open(filename, "r") as infile:
        rows, cols = map(int, infile.readline().split())

        path = []

        for line in infile:
            coordinate = ast.literal_eval(line.strip())
            path.append(coordinate)

    return rows, cols, path


def encrypt(message, rows, cols, path):
    message = message.upper().replace(" ", "")

    if len(message) > rows * cols:
        raise ValueError("Message is too long for the grid.")

    message = message.ljust(rows * cols, "X")

    grid = []
    index = 0

    for r in range(rows):
        row = []

        for c in range(cols):
            row.append(message[index])
            index += 1

        grid.append(row)

    encrypted = ""

    for r, c in path:
        encrypted += grid[r][c]

    return encrypted


def decrypt(ciphertext, rows, cols, path):
    if len(ciphertext) != rows * cols:
        raise ValueError("Ciphertext length does not match grid.")

    grid = [["" for c in range(cols)] for r in range(rows)]

    for i, (r, c) in enumerate(path):
        grid[r][c] = ciphertext[i]

    message = ""

    for r in range(rows):
        for c in range(cols):
            message += grid[r][c]

    return message.rstrip("X")


def main():
    filename = input("Enter the path file name: ")

    rows, cols, path = readPath(filename)

    message = input("Enter a message to encrypt: ")

    encrypted = encrypt(message, rows, cols, path)

    print("\nEncrypted message:", encrypted)

    decrypted = decrypt(encrypted, rows, cols, path)

    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
