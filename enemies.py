

enemy_names = [
    "Goblin",
    "Wolf",
    "Slime",
    "Zombie",
    "Skeleton",

    "Orc",
    "Bandit",
    "Troll",
    "Dark Archer",
    "Giant Spider",

    "Vampire",
    "Werewolf",
    "Necromancer",
    "Ice Golem",
    "Fire Demon",

    "Sand Beast",
    "Desert Raider",
    "Ancient Mummy",
    "Stone Warrior",
    "Dark Knight",

    "Flame Beast",
    "Volcano Dragon",
    "Frost Giant",
    "Sky Guardian",
    "Demon Warrior"
]


bosses = {
    10: "Goblin King",
    20: "Forest Guardian",
    30: "Ancient Golem",
    40: "Vampire Lord",
    50: "Dragon Rider",
    60: "Demon General",
    70: "Ice Titan",
    80: "Shadow Emperor",
    90: "Celestial Dragon",
    100: "Ancient Demon King"
}


def create_enemy(level):

    index = min((level - 1) // 4, len(enemy_names) - 1)

    name = enemy_names[index]

    hp = 50 + level * 15
    attack = 8 + level * 3
    defense = 3 + level * 2

    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "attack": attack,
        "defense": defense,
        "exp": level * 30,
        "gold": level * 15,
        "boss": False
    }


def create_boss(level):

    name = bosses[level]

    hp = level * 80
    attack = level * 6
    defense = level * 3

    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "attack": attack,
        "defense": defense,
        "exp": level * 100,
        "gold": level * 100,
        "boss": True
    }


def is_boss_level(level):

    return level in bosses