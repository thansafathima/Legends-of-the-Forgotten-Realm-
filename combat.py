

import random


def attack(player, enemy):

    damage = player.attack

    if player.weapon:
        damage += player.weapon["damage"]

    damage -= enemy["defense"]

    if damage < 1:
        damage = 1

    critical = random.randint(1, 100) <= player.crit_chance

    if critical:

        damage *= 2

        print("\n*** CRITICAL HIT! ***")

    enemy["hp"] -= damage

    print("You dealt", damage, "damage.")


def skill_attack(player, enemy):

    print("\n========== SKILLS ==========")

    for i, skill in enumerate(player.skills, 1):

        print(
            i,
            skill[0],
            "- Mana:",
            skill[1],
            "- Damage:",
            skill[2]
        )

    try:
        choice = int(input("Choose skill: "))

        if choice < 1 or choice > len(player.skills):

            print("Invalid skill.")
            return

        skill = player.skills[choice - 1]

        name = skill[0]
        mana_cost = skill[1]
        skill_damage = skill[2]

        if player.mana < mana_cost:

            print("Not enough mana!")
            return

        player.mana -= mana_cost

        damage = player.attack + skill_damage
        damage -= enemy["defense"]

        if damage < 1:
            damage = 1

        # Assassin's Instant Kill
        if name == "Instant Kill":

            if random.randint(1, 100) <= 10:

                enemy["hp"] = 0

                print("\n*** INSTANT KILL! ***")
                return

        enemy["hp"] -= damage

        print(name, "dealt", damage, "damage.")

    except ValueError:

        print("Please enter a number.")


def use_potion(player):

    if not player.potions:

        print("You have no potions.")
        return

    print("\n========== POTIONS ==========")

    names = list(player.potions.keys())

    for i, name in enumerate(names, 1):

        print(
            i,
            name,
            "x",
            player.potions[name]["count"]
        )

    try:

        choice = int(input("Choose potion: "))

        if choice < 1 or choice > len(names):

            print("Invalid choice.")
            return

        name = names[choice - 1]

        potion = player.potions[name]

        player.use_potion(potion)

        potion["count"] -= 1

        if potion["count"] == 0:

            del player.potions[name]

    except ValueError:

        print("Enter a number.")


def enemy_attack(player, enemy, defending):

    damage = enemy["attack"] - player.defense

    if damage < 1:
        damage = 1

    if defending:

        damage = damage // 2

        print("Defend reduced the damage by 50%.")

    player.hp -= damage

    print(
        enemy["name"],
        "dealt",
        damage,
        "damage."
    )


def show_inventory(player):

    print("\n========== INVENTORY ==========")

    if not player.inventory:

        print("Inventory is empty.")

    else:

        for item in player.inventory:

            print("-", item["name"])


def battle(player, enemy):

    print("\n================================")
    print("BATTLE:", enemy["name"])
    print("================================")

    while player.hp > 0 and enemy["hp"] > 0:

        print("\n-------------------------------")

        print(
            "Your HP:",
            player.hp,
            "/",
            player.max_hp
        )

        print(
            "Enemy HP:",
            enemy["hp"],
            "/",
            enemy["max_hp"]
        )

        print("\nYOUR TURN")

        print("1. Attack")
        print("2. Skills")
        print("3. Heal")
        print("4. Use Potion")
        print("5. Defend")
        print("6. Inventory")
        print("7. View Stats")
        print("8. Run")

        try:

            choice = int(input("Choose action: "))

        except ValueError:

            print("Enter a number.")
            continue

        defending = False
        action_done = True

        if choice == 1:

            attack(player, enemy)

        elif choice == 2:

            skill_attack(player, enemy)

        elif choice == 3:

            old_hp = player.hp

            player.hp = min(
                player.max_hp,
                player.hp + 20
            )

            print(
                "You healed",
                player.hp - old_hp,
                "HP."
            )

        elif choice == 4:

            use_potion(player)

        elif choice == 5:

            defending = True

            print(
                "You are defending."
            )

        elif choice == 6:

            show_inventory(player)

            action_done = False

        elif choice == 7:

            player.show_stats()

            action_done = False

        elif choice == 8:

            if enemy["boss"]:

                print(
                    "You cannot run from a boss!"
                )

                action_done = False

            else:

                print("You escaped!")
                return False

        else:

            print("Invalid choice.")
            action_done = False

        if enemy["hp"] <= 0:

            break

        if action_done:

            enemy_attack(
                player,
                enemy,
                defending
            )

    if player.hp <= 0:

        print("\nYou were defeated!")
        return False

    print(
        "\nYou defeated",
        enemy["name"],
        "!"
    )

    player.enemies_defeated += 1

    player.gain_exp(enemy["exp"])

    player.gold += enemy["gold"]

    print(
        "EXP gained:",
        enemy["exp"]
    )

    print(
        "Gold gained:",
        enemy["gold"]
    )

    return True