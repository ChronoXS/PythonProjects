import math


def converter(x, y):
    z = math.sqrt((x * x) + (y * y))
    return z / 2.54


def main():
    while True:
        x = float(input("Please enter your screen length in cm.\nYou can easily measure your screen bottom one end to "
                        "other end.\n"))
        y = float(input("Please enter your screen width in cm.\nYou can easily measure your screen one side, "
                        "one end to "
                        "other end.\n"))
        print("Your screen is {} inç".format(converter(x, y)))
        input("Press enter for try again.")


main()
