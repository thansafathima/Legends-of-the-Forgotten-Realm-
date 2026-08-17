

class Player:

    def __init__(self, name, player_class):

        self.name = name
        self.player_class = player_class

        self.level = 1
        self.exp = 0
        self.gold = 200

        self.weapon = None
        self.armor = None

        self.inventory = []
        self.potions = {}

        self.enemies_defeated = 0
        self.bosses_defeated = 0

        self.crit_chance = 0

        if player_class == "Warrior":
            self.max_hp = 150
            self.max_mana = 50
            self.attack = 20
            self.defense = 15
            self.crit_chance = 10

            self.skills = [
                ("Slash", 10, 20),
                ("Shield Bash", 15, 30),
                ("Rage", 20, 40),
                ("Earthquake", 30, 55)
            ]

        elif player_class == "Mage":
            self.max_hp = 100
            self.max_mana = 150
            self.attack = 25
            self.defense = 8
            self.crit_chance = 15

            self.skills = [
                ("Fireball", 10, 25),
                ("Ice Blast", 15, 35),
                ("Thunder Strike", 20, 45),
                ("Meteor", 35, 65)
            ]

        elif player_class == "Archer":
            self.max_hp = 110
            self.max_mana = 80
            self.attack = 18
            self.defense = 10
            self.crit_chance = 25

            self.skills = [
                ("Multi Shot", 10, 25),
                ("Poison Arrow", 15, 35),
                ("Explosive Arrow", 25, 50),
                ("Sniper Shot", 35, 70)
            ]

        else:
            self.max_hp = 90
            self.max_mana = 80
            self.attack = 25
            self.defense = 7
            self.crit_chance = 30

            self.skills = [
                ("Backstab", 10, 30),
                ("Smoke Bomb", 15, 40),
                ("Shadow Strike", 25, 55),
                ("Instant Kill", 40, 100)
            ]

        self.hp = self.max_hp
        self.mana = self.max_mana

    def show_stats(self):

        print("\n========== PLAYER STATS ==========")
        print("Name:", self.name)
        print("Class:", self.player_class)
        print("Level:", self.level)
        print("EXP:", self.exp)
        print("HP:", self.hp, "/", self.max_hp)
        print("Mana:", self.mana, "/", self.max_mana)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Gold:", self.gold)
        print("Critical Chance:", self.crit_chance, "%")

        if self.weapon:
            print("Weapon:", self.weapon["name"])
        else:
            print("Weapon: None")

        if self.armor:
            print("Armor:", self.armor["name"])
        else:
            print("Armor: None")

        print("Enemies Defeated:", self.enemies_defeated)
        print("Bosses Defeated:", self.bosses_defeated)

    def gain_exp(self, amount):

        self.exp += amount

        needed = self.level * 100

        while self.exp >= needed and self.level < 100:

            self.exp -= needed
            self.level_up()

            needed = self.level * 100

    def level_up(self):

        self.level += 1

        self.max_hp += 20
        self.max_mana += 10
        self.attack += 5
        self.defense += 3

        self.hp = self.max_hp
        self.mana = self.max_mana

        print("\n*** LEVEL UP! ***")
        print("You reached Level", self.level)

    def use_potion(self, potion):

        if potion["type"] == "health":

            old_hp = self.hp
            self.hp = min(self.max_hp, self.hp + potion["value"])
            print("HP restored:", self.hp - old_hp)

        elif potion["type"] == "mana":

            old_mana = self.mana
            self.mana = min(self.max_mana, self.mana + potion["value"])
            print("Mana restored:", self.mana - old_mana)

        elif potion["type"] == "mixed":

            self.hp = min(self.max_hp, self.hp + potion["value"])
            self.mana = min(self.max_mana, self.mana + potion["value"])

            print("HP and Mana restored.")

        elif potion["type"] == "attack":

            self.attack += potion["value"]
            print("Attack increased!")

        elif potion["type"] == "defense":

            self.defense += potion["value"]
            print("Defense increased!")

        elif potion["type"] == "crit":

            self.crit_chance += potion["value"]
            print("Critical chance increased!")