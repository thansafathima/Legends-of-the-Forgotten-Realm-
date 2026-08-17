import json


def save_game(player):

    data = {

        "name": player.name,

        "player_class":
            player.player_class,

        "level":
            player.level,

        "exp":
            player.exp,

        "gold":
            player.gold,

        "max_hp":
            player.max_hp,

        "hp":
            player.hp,

        "max_mana":
            player.max_mana,

        "mana":
            player.mana,

        "attack":
            player.attack,

        "defense":
            player.defense,

        "crit_chance":
            player.crit_chance,

        "weapon":
            player.weapon,

        "armor":
            player.armor,

        "inventory":
            player.inventory,

        "potions":
            player.potions,

        "enemies_defeated":
            player.enemies_defeated,

        "bosses_defeated":
            player.bosses_defeated,

        "skills":
            player.skills
    }

    with open(
        "savegame.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print("\nGame saved successfully!")


def load_game():

    try:

        with open(
            "savegame.json",
            "r"
        ) as file:

            data = json.load(file)

        from player import Player

        player = Player(
            data["name"],
            data["player_class"]
        )

        player.level = data["level"]
        player.exp = data["exp"]
        player.gold = data["gold"]

        player.max_hp = data["max_hp"]
        player.hp = data["hp"]

        player.max_mana = data["max_mana"]
        player.mana = data["mana"]

        player.attack = data["attack"]
        player.defense = data["defense"]

        player.crit_chance = data[
            "crit_chance"
        ]

        player.weapon = data["weapon"]
        player.armor = data["armor"]

        player.inventory = data[
            "inventory"
        ]

        player.potions = data[
            "potions"
        ]

        player.enemies_defeated = data[
            "enemies_defeated"
        ]

        player.bosses_defeated = data[
            "bosses_defeated"
        ]

        player.skills = [
            tuple(skill)
            for skill in data["skills"]
        ]

        print("\nGame loaded successfully!")

        return player

    except FileNotFoundError:

        print(
            "\nNo saved game found."
        )

        return None

    except (json.JSONDecodeError, KeyError):

        print(
            "\nSave file is corrupted."
        )

        return None