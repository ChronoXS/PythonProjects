class Math:
    @staticmethod
    def power(base: int, top: int):
        final = 1
        for _ in range(top):
            final = final * base
        return final
    @staticmethod
    def length(value: int):
        flag = 1
        while True:
            n_value = value / 10
            value = n_value
            flag += 1
            if value <= 10:
                break
        print("Your number is {} digit".format(flag))

def main():
    while True:
        base = int(input("Enter the base number:"))
        top = int(input("Enter the top number:"))
        number = Math.power(base, top)
        print("Power", number)
        Math.length(number)
        input("For new number press Enter.")

main()
