import random
import os

class Enemy():
    def __init__(self):
        self.alive = True
        self.health = random.randint(30,70)
        self.power = random.randint(5,30)
        self.shield = random.randint(1,10)
        self.sequence = 0

    def attack(self, player):
        damage = self.power - player.shield
        player.health -= damage
        if player.health <= 0:
            player.alive = False

class Player():
    def __init__(self):
        self.alive = True
        self.health = random.randint(50,70)
        self.power = random.randint(40,90)
        self.shield = random.randint(1,10)

    def attack(self, enemy):
        damage = self.power - enemy.shield
        enemy.health -= damage
        if enemy.health <= 0:
            enemy.alive = False

enemies = []
alive_enemies = []
enemynumber = 0
for i in range(5):
    enemy = Enemy()
    enemy.sequence = enemynumber + 1
    enemies.append(enemy)
    alive_enemies.append(enemy)
    enemynumber += 1
enemy_len=len(alive_enemies)
warrior = Player()
name = input("Tell me your name warrior\n")

while True:
    print("\033c")
    print("{}, your attributes are:\nHealth ---- {} Power ---- {} Armor {}.".format(name, warrior.health, warrior.power, warrior.shield))
    if not warrior.alive:
        print("""You are a dead man.
                GAME OVER""")
        quit()
    for i in enemies:
        if i.alive:
            print("{}.Enemy: Health {} ---- Power {} ---- Armor {}".format(i.sequence, i.health, i.power, i.shield))
        else:
            print("{}.Enemy: Dead".format(i.sequence))
    while True:
        try:
            selection = int(input("Now, choose the ENEMY."))
            break
        except ValueError:
            selection = input("There is no enemy such that. Enter the enemy number.")

    if selection >= 0 and selection < enemy_len+1:
        for i in alive_enemies:
            if i.sequence == selection:
                cenemy = i
                warrior.attack(cenemy)
                if not cenemy.alive:
                    print("Enemy {} is dead.".format(cenemy.sequence))
                    alive_enemies.remove(cenemy)
                if not alive_enemies:
                    print("\nGood fight warrior. You won.")
                    quit()
                attacker_number=random.randint(0,len(alive_enemies)-1)
                attacker_enemy = alive_enemies[attacker_number]
                attacker_enemy.attack(warrior)
    else:
        print("Invalid selection. Try again.")
