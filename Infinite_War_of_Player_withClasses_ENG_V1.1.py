import random
import os
import time
class Enemy(): #I created a class for enemies and their attributes are random
    def __init__(self):
        self.health=random.randint(80,120)
        self.attack=random.randint(0,50)
        self.armor=random.randint(0,50)

    def hit(self,player):
        damage = self.attack - player.armor
        if damage<0:
            damage=0
        player.health -= damage
        if player.health<1:
            player.status=False


class Player():
    def __init__(self,enemycount:int):
        self.health=int(enemycount)*70 #For every enemy, player has 70 health
        self.attack=80
        self.armor=20
        self.status=True
    def hit(self,enemy):
        damage= self.attack-enemy.armor
        enemy.health -= damage
        if enemy.health<1:
            enemies.remove(enemy)

while True:
    enemycount=input("How many enemy do you want to fight against\nYour health will adjust by the enemy number, please enter:")
    if enemycount.isdigit():          #With that if, there is no error for types
        enemycount=int(enemycount)
        if enemycount>0:
            break
        else:
            print("Please Enter a number above 0")
    else:
        print("Please enter a number\n\n")
        continue
player = Player(enemycount)     #player created by number of enemy.
enemies=list()                   #enemies's list created
for i in range(enemycount):     #with this for loop, i create enemies and assign them to enemy's list.
    enemies.append(Enemy())
new_enemiescount=len(enemies)
while True:
    print("\n"*100)
    print("player ---->>  Health={}  ----  Attack={}  ----  Armor={}\n\n".format(player.health,player.attack,player.armor))
    if player.status==False:
        print("You're dead\nGAME OVER!")
        print("Press Enter for exit.")
        input()
        break
    for i in enemies:        #printed all enemies
        print("{}.Enemy ---->>  Health={}  ----  Attack={}  ----  Armor={}".format(enemies.index(i),i.health,i.attack,i.armor))

    c_enemy_num= int(input("Please Enter the enemy you want to attack (Please enter a number) ="))
    if c_enemy_num < 0 or c_enemy_num > new_enemiescount-1:
        print("You entered wrong number, try again.")
        time.sleep(2.5)
        continue

    c_enemy=enemies[c_enemy_num]        #choosen enemy
    player.hit(c_enemy)                 #hit to chosen enemy
    new_enemiescount=len(enemies)       #new enemy count refresh every loop
    if new_enemiescount<1:
        print("You WIN!!")
        print("Press Enter for exit.")
        input()
        break
    a_enemy=enemies[random.randint(0,new_enemiescount-1)]   # attacker enemy chosen by randomly
    a_enemy.hit(player)



















