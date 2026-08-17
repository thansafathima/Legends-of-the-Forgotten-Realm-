

import random

from player import Player
from enemies import (
    create_enemy,
    create_boss,
    is_boss_level
)

from combat import battle
from shop import shop
from save_load import (
    save_game,
    load_game
)


# =========================
# CHARACTER CREATION
# =========================

def create_character():

    print("\n================================")
    print("       CHARACTER CREATION")
    print("================================")

    name = input(
        "Enter Player Name: "
    ).strip()

    while not name:

        print(
            "Name cannot be empty."
        )

        name = input(
            "Enter Player Name: "
        ).strip()

    print("\nChoose Your Class")

    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Assassin")

    classes = {
        1: "Warrior",
        2: "Mage",
        3: "Archer",
        4: "Assassin"
    }

    while True:

        try:

            choice = int(
                input("Choose class: ")
            )

            if choice in classes:

                return Player(
                    name,
                    classes[choice]
                )

            print(
                "Please choose 1-4."
            )

        except ValueError:

            print(
                "Enter a number."
            )




def give_starting_items(player):

    player.potions[
        "Small Health Potion"
    ] = {

        "name":
            "Small Health Potion",

        "type":
            "health",

        "value":
            50,

        "price":
            30,

        "count":
            3
    }

    player.potions[
        "Small Mana Potion"
    ] = {

        "name":
            "Small Mana Potion",

        "type":
            "mana",

        "value":
            30,

        "price":
            30,

        "count":
            2
    }


def get_loot(player):

    from items import (
        weapons,
        armors,
        potions
    )

    chance = random.randint(
        1,
        100
    )

    if chance <= 50:

        gold = random.randint(
            20,
            100
        )

        player.gold += gold

        print(
            "You found",
            gold,
            "gold!"
        )

    elif chance <= 70:

        available = [
            w for w in weapons
            if w["level"] <= player.level
        ]

        weapon = random.choice(
            available
        )

        player.inventory.append(
            weapon.copy()
        )

        print(
            "You found:",
            weapon["name"]
        )

    elif chance <= 90:

        available = [
            a for a in armors
            if a["level"] <= player.level
        ]

        armor = random.choice(
            available
        )

        player.inventory.append(
            armor.copy()
        )

        print(
            "You found:",
            armor["name"]
        )

    else:

        potion = random.choice(
            potions
        )

        name = potion["name"]

        if name not in player.potions:

            player.potions[name] = (
                potion.copy()
            )

            player.potions[name][
                "count"
            ] = 0

        player.potions[name][
            "count"
        ] += 1

        print(
            "You found:",
            name
        )



def equipment(player):

    while True:

        print("\n========== EQUIPMENT ==========")

        print("1. Equip Weapon")
        print("2. Equip Armor")
        print("3. Unequip Weapon")
        print("4. Unequip Armor")
        print("5. Exit")

        try:

            choice = int(
                input("Choose: ")
            )

        except ValueError:

            print("Enter a number.")
            continue

        if choice == 1:

            equip_weapon(player)

        elif choice == 2:

            equip_armor(player)

        elif choice == 3:

            player.weapon = None

            print(
                "Weapon unequipped."
            )

        elif choice == 4:

            player.armor = None

            print(
                "Armor unequipped."
            )

        elif choice == 5:

            break

        else:

            print("Invalid choice.")


def equip_weapon(player):

    available = []

    for item in player.inventory:

        if "damage" in item:

            available.append(item)

    if not available:

        print(
            "You have no weapons."
        )

        return

    print("\nWeapons:")

    for i, weapon in enumerate(
        available,
        1
    ):

        print(
            i,
            weapon["name"]
        )

    try:

        choice = int(
            input("Choose: ")
        )

        player.weapon = available[
            choice - 1
        ]

        print(
            player.weapon["name"],
            "equipped!"
        )

    except (ValueError, IndexError):

        print("Invalid choice.")


def equip_armor(player):

    available = []

    for item in player.inventory:

        if "defense" in item:

            available.append(item)

    if not available:

        print(
            "You have no armor."
        )

        return

    print("\nArmor:")

    for i, armor in enumerate(
        available,
        1
    ):

        print(
            i,
            armor["name"]
        )

    try:

        choice = int(
            input("Choose: ")
        )

        player.armor = available[
            choice - 1
        ]

        print(
            player.armor["name"],
            "equipped!"
        )

    except (ValueError, IndexError):

        print("Invalid choice.")




def game_over(player):

    print("\n==============================")
    print("          GAME OVER")
    print("==============================")

    print("1. Retry")
    print("2. Load Save")
    print("3. Exit")

    try:

        choice = int(
            input("Choose: ")
        )

        if choice == 1:

            player.hp = player.max_hp

            play_game(player)

        elif choice == 2:

            new_player = load_game()

            if new_player:

                play_game(
                    new_player
                )

        else:

            print(
                "Goodbye!"
            )

    except ValueError:

        print(
            "Invalid choice."
        )


def victory(player):

    print("\n")
    print(
        "========================================"
    )
    print(
        "       YOU SAVED THE KINGDOM!"
    )
    print(
        "========================================"
    )

    print(
        "Player:",
        player.name
    )

    print(
        "Final Level:",
        player.level
    )

    print(
        "Total Gold:",
        player.gold
    )

    print(
        "Bosses Defeated:",
        player.bosses_defeated
    )

    print(
        "Enemies Defeated:",
        player.enemies_defeated
    )

    print(
        "========================================"
    )

def play_game(player):

    give_starting_items(player)

    while (
        player.level <= 100
        and player.hp > 0
    ):

        print("\n================================")
        print(
            "LEGENDS OF THE FORGOTTEN REALM"
        )
        print("================================")

        print(
            "Level:",
            player.level
        )

        print(
            "HP:",
            player.hp,
            "/",
            player.max_hp
        )

        print(
            "Gold:",
            player.gold
        )

        
        if is_boss_level(
            player.level
        ):

            print("\n")
            print(
                "!!! BOSS BATTLE !!!"
            )

            boss = create_boss(
                player.level
            )

            result = battle(
                player,
                boss
            )

            if not result:

                game_over(player)
                return

            player.bosses_defeated += 1

            print(
                "\nBoss defeated!"
            )

            if player.level == 100:

                victory(player)
                return

        else:

            enemy = create_enemy(
                player.level
            )

            result = battle(
                player,
                enemy
            )

            if not result:

                game_over(player)
                return

            get_loot(player)

        print("\nWhat next?")

        print(
            "1. Continue"
        )

        print(
            "2. Shop"
        )

        print(
            "3. Equipment"
        )

        print(
            "4. View Stats"
        )

        print(
            "5. Save Game"
        )

        print(
            "6. Exit"
        )

        try:

            choice = int(
                input("Choose: ")
            )

        except ValueError:

            print(
                "Enter a number."
            )

            continue

        if choice == 2:

            shop(player)

        elif choice == 3:

            equipment(player)

        elif choice == 4:

            player.show_stats()

        elif choice == 5:

            save_game(player)

        elif choice == 6:

            save_game(player)

            print(
                "Game saved. Goodbye!"
            )

            return




def main():

    while True:

        print("\n")
        print(
            "========================================"
        )

        print(
            "    LEGENDS OF THE FORGOTTEN REALM"
        )

        print(
            "========================================"
        )

        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        try:

            choice = int(
                input("Choose: ")
            )

        except ValueError:

            print(
                "Enter a number."
            )

            continue

        if choice == 1:

            player = create_character()

            play_game(player)

        elif choice == 2:

            player = load_game()

            if player:

                play_game(player)

        elif choice == 3:

            print("\n========== INSTRUCTIONS ==========")

            print(
                "Create your character and choose a class."
            )

            print(
                "Defeat enemies to gain EXP and gold."
            )

            print(
                "Use attacks, skills and potions."
            )

            print(
                "Defend to reduce incoming damage."
            )

            print(
                "Buy equipment from the shop."
            )

            print(
                "Every 10 levels has a boss."
            )

            print(
                "Reach Level 100."
            )

            print(
                "Defeat the Ancient Demon King."
            )

        elif choice == 4:

            print(
                "Thank you for playing!"
            )

            break

        else:

            print(
                "Invalid choice."
            )


if __name__ == "__main__":

    main()