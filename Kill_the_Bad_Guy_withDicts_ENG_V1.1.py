import time
from random import randint
n_name = str(input("Enter your nickname:"))
char = {                    #Our char's stats.
    "name":n_name,
    "health": 50,
    "attack": 12,
    "heal_point":8
    }

enemy = {                   #Enemy's stats.
    "name": "Bad Guy",
    "health": 40,
    "attack": 11,
    "heal_point":18
    }
#menu variable looks mixed, but i did it for the terminate output.
menu="""
1-     Attack {attack}         -----  Name   ==    {char_name}  --  {enemy_name}
2-     Heal {heal_point}            -----  Health ==    {char_health}    --  {enemy_health} 
Enter- Pass              -----
"""

def attack(attacker:dict ,defencer:dict):
    print(attacker["name"], "is attacking to",defencer["name"])
    time.sleep(0.5)
    damage=attacker["attack"]
    health=defencer["health"]
    health=health-damage
    defencer["health"]=health
    print(defencer["name"],"'s health is ",defencer["health"])
    time.sleep(1)
    print("\n"*2)
def heal(char:dict):
    print(char["name"],"is healing himself")
    time.sleep(0.5)
    heal_point=char["heal_point"]
    char["health"]= char["health"]+heal_point
    print(char["name"],"'s health is",char["health"])
    time.sleep(1)

while True:

    print(char)
    print(enemy)
    print("-"*10)
    print(menu.format(attack=char["attack"],heal_point=char["heal_point"],char_name=char["name"],enemy_name=enemy["name"],char_health=char["health"],enemy_health=enemy["health"]))
    print("-"*10)
    choice = input("Enter your choice=")
    value=randint(1,5)  #Getting random numbers for enemy's decision

    if choice == "1":
        attack(char,enemy) # Our char is attacker.

        if enemy["health"] <1: # Health is under zero
            print("Bad guy is dead.\nEmre won.")
            print("Game Over\nPress Enter for exit.")
            input()
            break
    if choice == "2":
        heal(char)

    if value <5 : # with %80 chance enemy choose to attack
        print("Bad Guy is choosing...")
        time.sleep(0.5)
        print("Bad guy choose to attack")
        attack(enemy,char)

        if char["health"] <1:
            print(enemy["name"],"is won, you lose!")
            print("Game Over\n Press Enter for exit.")
            input()
            break

    if value > 4: # with %20 chance enemy choose to heal himself
        print("Bad Guy is choosing...")
        time.sleep(0.5)
        print("Bad guy choose to heal himself")
        heal(enemy)


