import random


class Sprite:

    def __init__(self, name, hp, credits):
        self.hp = hp
        self.name = name
        self.credits = credits
        self.status = "Alive"
        self.powers = {
            "Slash - Reduce 20 HP of opponent": 0,
            "Bomb - Reduce 50 HP of opponent": 20,
            "Heal - Increase 20 HP": 10,
        }

    def Display(self):
        if self.hp <= 0:
            self.status = "Dead"
            print(f"{self.name} died")
            return None
        print("========================")
        print(f"Name: {self.name}")
        print(f"Health: {self.hp}")
        print(f"Credits: {self.credits}")
        for power, cost in self.powers.items():
            print(f"{power}\tCost: {cost}")
        return None

    def Slash(self, opponent):
        opponent.hp -= 20
        self.Display()
        return None

    def Heal(self):
        if self.credits >= 10:
            self.hp += 20
            self.credits -= 10
            self.Display()
            return None
        else:
            print("Not enough credits")
            return None

    def Bomb(self, opponent):
        if self.credits >= 20:
            opponent.hp -= 50
            self.credits -= 20
            self.Display()
            return None
        else:
            print("Not Enough Credits")
            return None


enemy = Sprite("Boss", 500, 30)
player = Sprite(input("Enter your name: "), 100, 100)

enemy.Display()
player.Display()

# Fixed: Wraps moves in functions so they execute during the loop, not on setup
attacks = {
    "slash": lambda: player.Slash(enemy),
    "bomb": lambda: player.Bomb(enemy),
    "heal": lambda: player.Heal(),
}

# Fixed: Target changed from enemy to player
enemy_attacks = {
    "slash": lambda: enemy.Slash(player),
    "bomb": lambda: enemy.Bomb(player),
    "heal": lambda: enemy.Heal(),
}

while True:
    attack = input("Enter attack: ").lower().strip()
    if attack in attacks:
        attacks[attack]()  # Fixed: Called as a function ()

    # Fixed: Checked credits instead of HP, and replaced invalid popitem() with del
    if enemy.credits < 20 and "bomb" in enemy_attacks:
        del enemy_attacks["bomb"]
    if enemy.credits < 10 and "heal" in enemy_attacks:
        del enemy_attacks["heal"]

    # Fixed: Selected and executed enemy move properly
    enemy_move = random.choice(list(enemy_attacks.keys()))
    enemy_attacks[enemy_move]()

    if player.status == "Dead" or enemy.status == "Dead":
        break