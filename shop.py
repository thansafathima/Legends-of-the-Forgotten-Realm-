

from items import weapons, armors, potions


def shop(player):

    while True:

        print("\n========== SHOP ==========")

        print("Gold:", player.gold)

        print("1. Buy Weapon")
        print("2. Buy Armor")
        print("3. Buy Potion")
        print("4. Sell Item")
        print("5. Exit")

        try:

            choice = int(input("Choose: "))

        except ValueError:

            print("Enter a number.")
            continue

        if choice == 1:

            buy_weapon(player)

        elif choice == 2:

            buy_armor(player)

        elif choice == 3:

            buy_potion(player)

        elif choice == 4:

            sell_item(player)

        elif choice == 5:

            break

        else:

            print("Invalid choice.")


def buy_weapon(player):

    available = [
        weapon for weapon in weapons
        if weapon["level"] <= player.level
    ]

    print("\n========== WEAPONS ==========")

    for i, weapon in enumerate(available, 1):

        print(
            i,
            weapon["name"],
            "-",
            weapon["price"],
            "gold",
            "- Level",
            weapon["level"]
        )

    try:

        choice = int(input("Choose weapon: "))

        weapon = available[choice - 1]

        if player.gold >= weapon["price"]:

            player.gold -= weapon["price"]

            player.inventory.append(
                weapon.copy()
            )

            print(
                weapon["name"],
                "purchased!"
            )

        else:

            print("Not enough gold.")

    except (ValueError, IndexError):

        print("Invalid choice.")


def buy_armor(player):

    available = [
        armor for armor in armors
        if armor["level"] <= player.level
    ]

    print("\n========== ARMOR ==========")

    for i, armor in enumerate(available, 1):

        print(
            i,
            armor["name"],
            "-",
            armor["price"],
            "gold"
        )

    try:

        choice = int(input("Choose armor: "))

        armor = available[choice - 1]

        if player.gold >= armor["price"]:

            player.gold -= armor["price"]

            player.inventory.append(
                armor.copy()
            )

            print(
                armor["name"],
                "purchased!"
            )

        else:

            print("Not enough gold.")

    except (ValueError, IndexError):

        print("Invalid choice.")


def buy_potion(player):

    print("\n========== POTIONS ==========")

    for i, potion in enumerate(potions, 1):

        print(
            i,
            potion["name"],
            "-",
            potion["price"],
            "gold"
        )

    try:

        choice = int(input("Choose potion: "))

        potion = potions[choice - 1]

        if player.gold >= potion["price"]:

            player.gold -= potion["price"]

            name = potion["name"]

            if name not in player.potions:

                player.potions[name] = potion.copy()
                player.potions[name]["count"] = 0

            player.potions[name]["count"] += 1

            print(
                potion["name"],
                "purchased!"
            )

        else:

            print("Not enough gold.")

    except (ValueError, IndexError):

        print("Invalid choice.")


def sell_item(player):

    if not player.inventory:

        print("Inventory is empty.")
        return

    print("\n========== SELL ITEMS ==========")

    for i, item in enumerate(
        player.inventory,
        1
    ):

        print(
            i,
            item["name"],
            "- Sell:",
            item["price"] // 2,
            "gold"
        )

    try:

        choice = int(
            input("Choose item: ")
        )

        item = player.inventory.pop(
            choice - 1
        )

        player.gold += item["price"] // 2

        print(
            item["name"],
            "sold!"
        )

    except (ValueError, IndexError):

        print("Invalid choice.")