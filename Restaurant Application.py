import time

tables = dict()
for i in range(10):
    tables[i] = 0
def Addbill():
    tabno= int(input("Which table is that you want to add bill="))
    val= int(input("How many dollars do you want to add="))
    default= tables[tabno]
    sum= val+default

    tables[tabno] = sum
def Rbill():
    tabno = int(input("Which table is that you want to add bill="))
    val = int(input("How many dollars do you want to add="))
    default = tables[tabno]
    sum = default-val

    tables[tabno] = sum
def main():
    while True:
        print("""
            Welcome, please choose an option below
            1-Show tables
            2-Add bill
            3-Remove bill
            Q-Quit
        """)

        choice=input("Input your choice = ")

        if choice == "1":
            for i in range(10):
                print("Table {}'s bill is = {} ".format(i,tables[i]))
            print("Progress completed. Press Enter to return main menu.")
            input()
        if choice == "2":
            Addbill()
            print("Progress completed. Press Enter to return main menu.")
            input()
        if choice == "3":
            Rbill()
            print("Progress completed. Press Enter to return main menu.")
            input()
        if choice =="q":
            print("Saving...")
            time.sleep(1)
            print("Saved")
            break

main()