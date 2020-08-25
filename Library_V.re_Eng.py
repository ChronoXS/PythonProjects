import os
import time

abooklist=list()

menu = """
 Welcome to the Library
 1-List of Books
 2-Donate a Book to Library
 3-Take a Book from Library
 4-Exit
 """

def listofbooks(booklist:list):
    num=len(booklist)
    if num==0:
        print("There is no book in the library.\n Please donate a book.")
        print("Please press Enter to return main menu")
        input()
    else:
        counter=0
        for i in booklist:
            counter+=1
            print(counter,".Book=" ,i)
        print("Please press Enter to return main menu")
        input()

def donatebook(bookname:str,booklist:list):
    booklist.append(bookname)
    print("The book you entered is adding to the library")
    time.sleep(1)
    print("-\-")
    time.sleep(1)
    print("-/-")
    time.sleep(1)
    print("The book you entered has been added to library")
    print("Please press Enter to return main menu")
    input()

def takebook(bookname:str,booklist:list):
    counter=0
    for i in booklist:
        if i==bookname:
            counter+=1
    if counter>0:
        booklist.remove(bookname)
        print("The book you entered is removing from library")
        time.sleep(1)
        print("-\-")
        time.sleep(1)
        print("-/-")
        time.sleep(1)
        print("The book you entered has been removed from library")
        print("Please press Enter to return main menu")
        input()
    else:
        print("The book you entered was not found!")
        print("Please press Enter to return main menu")
        input()
while True:
    print("\n"*100)
    print(menu)
    choice=input("Your choice=")
    if choice=="1":
        listofbooks(abooklist)
    if choice=="2":
        book=input("Please write book's name which is donating")
        donatebook(book,abooklist)
    if choice=="3":
        book=input("Please write book's name that you want")
        takebook(book,abooklist)
    if choice=="4":
        print("Exitting")
        time.sleep(1)
        print("Exited!\nHave a good day")
        break
    else:
        print("You entered a wrong value, please try again.")