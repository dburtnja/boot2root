from turtle import Turtle, done
from sys import argv


COMMANDS = {
    "Recule": "backward",
    "droite": "right",
    "gauche": "left",
    "Avance": "forward"
}


def parse_line(line):
    operation = None
    value = None

    for word in line.split():
        if operation and value:
            break
        if word in COMMANDS:
            operation = COMMANDS[word]
        if word.isdigit():
            value = int(word)
    return operation, value


def drow(file_name):
    turtle = Turtle()

    # turtle.speed(1)
    with open(file_name, "r") as file:
        for line in file.readlines():
            operation, value = parse_line(line)
            if operation and value:
                getattr(turtle, operation)(value)
    done()


if __name__ == '__main__':
    try:
        if len(argv) == 2:
            drow(argv[1])
        else:
            print("File not specified")
    except Exception as e:
        print(e)

