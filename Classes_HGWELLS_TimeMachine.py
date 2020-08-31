import time
import os
class Eloi():
    def __init__(self,name,age,color,place_to_live):
        self.name = name
        self.age = age
        self.color = color
        self.place_to_live = place_to_live
    def escape(self, status):
        if status == 0:
            print("{} has frightened and going to sleep with other elois".format(self.name))
        else:
            print("Every eloi wondering around. Taking flowers, smiling eachother")


class Marlock(Eloi):
    def __init__(self, name, age, color, place_to_live, eye_color):
        super().__init__(name, age, color, place_to_live)
        self.eye_color = eye_color
    def escape(self,status):
        if status == 1:
            print("{} has frightened and escape to underground".format(self.name))
        else:
            print("Every Marlock searching for food at the outside.")

def wrap(text):
    try:
        text = str(text)
    except ValueError:
        text = str(text)
    text_len = len(text)
    print("+"*text_len)
    print(text)
    print("+"*text_len,"\n")

weena = Eloi("Weena", 20,"pink", "capital")
grey = Marlock("Grey", 183, "grey-white", "underground", "black")
n_status = 1
while True:
    os.system("CLS")
    if n_status == 1:
        print("It is morning, sun is at the top.\n")
    if n_status == 0:
        print("Twilight, kind of strange sounds coming all over the forest.\n")
    time.sleep(3)
    status = n_status
    weena.escape(n_status)
    wrap(weena.name)
    wrap(weena.age)
    wrap(weena.color)
    wrap(weena.place_to_live)
    grey.escape(n_status)
    status += 1
    n_status = status%2
    print("day faze over, press enter to pass ")
    input()

