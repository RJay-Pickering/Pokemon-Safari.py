from dataclasses import dataclass
from typing import List, Dict
import random


@dataclass
class Pokemon:
    name: str
    types: str
    health: int
    health_cap: int
    exp: int
    fainted: bool
    moves: List[str]
    damage: List[int]


@dataclass
class Player:
    name: str
    party: List[Pokemon]
    money: int
    items: List[str]


@dataclass
class Area:
    name: str
    description: str
    connections: List[str]


@dataclass
class Trainer:
    name: str
    party: List[Pokemon]


AREA: Dict[str, Area] = {
    "Safari Counter": Area(
        "Safari Counter",
        "This the Safari Counter where you can buy items",
        ["Battle Counter", "Grasslands", "PC"],
    ),
    "Battle Counter": Area(
        "Battle Counter",
        "This is the Battle Counter where you can prove your strength against other trainers.",
        ["Safari Counter", "Grasslands", "PC"],
    ),
    "PC": Area(
        "PC",
        "This is the PC where you can store Pokemon so can catch them all and have a place to store them.",
        ["Safari Counter", "Grasslands", "Battle Counter"],
    ),
    "Grasslands": Area(
        "Grasslands",
        "A wide open spanse of grass and open fields lay before you",
        ["Safari Counter", "Prairie", "Pampas"],
    ),
    "Prairie": Area(
        "Prairie",
        "A wide open spanse of grass and open fields lay before you",
        ["Grasslands", "Pampas", "Savanna"],
    ),
    "Pampas": Area(
        "Pampas",
        "A wide open spanse of grass and open fields lay before you",
        ["Grasslands", "Prairie", "Savanna"],
    ),
    "Savanna": Area(
        "Savanna",
        "A wide open spanse of grass and open fields lay before you, you see trees close by",
        ["Pampas", "Prairie", "The Forest Opening"],
    ),
    "The Forest Opening": Area(
        "The Forest Opening",
        "The grass starts to become thin and the sun starts to be blocked out by some tree limbs.",
        ["Temperate", "Savanna"],
    ),
    "Temperate": Area(
        "Temperate",
        "This is an region with high levels of precipitation, humidity, and a variety of deciduous trees that lose their leaves during the cold winters.",
        ["The Forest Opening", "Boreal"],
    ),
    "Boreal": Area(
        "Boreal",
        "This part of the forest has very cold temperatures. It is mostly made up of cold tolerant coniferous species of Pokemon.",
        ["Temperate", "Tropical"],
    ),
    "Tropical": Area(
        "Tropical",
        "You feel the humidity rising and feel cool rain fall hitting you from the trees. The sound of an near by water fall is heard in the distance",
        ["Boreal", "Kyoger Falls"],
    ),
    "Kyoger Falls": Area(
        "Kyoger Falls",
        "You continue through the Forest and reach the waterfall. Its name comes from its creator, Kyoger the legendary Pokemon of water. In 2003, Kyoger awoken to battle Groundon, during his awakening this river was born.",
        ["Tropical", "Useless River"],
    ),
    "Useless River": Area(
        "Useless River", "Home to useless Pokemon", ["Kyoger Falls", "Great Pond"]
    ),
    "Great Pond": Area(
        "Great Pond",
        "This is a huge pond filled with alot of water pokemon. Be careful touching the water, Eletric pokemon loves to play here!",
        ["Useless River", "Poke Beach"],
    ),
    "Poke Beach": Area(
        "Poke Beach",
        "You walk on the other side of the pond and see a beach filled with peaceful trainers and sandy pokemon. ahead of the Beach is just more sand.",
        ["Great Pond", "Dust Bowl"],
    ),
    "Dust Bowl": Area(
        "Dust Bowl",
        "A sandy area with light dust storms brew up from dragon Pokemons, and humidity from the fire Pokemons.",
        ["Poke Beach", "Addax"],
    ),
    "Addax": Area(
        "Addax",
        "A pure white sandy area which is named after and extinct Pokemon. Most people reffer this area as the `holy lands`",
        ["Dust Bowl", "Base"],
    ),
    "Base": Area(
        "Base",
        "You get out of the dessert and reached the base of the mountain. There is an elevator near by to reach the peak of the mountain.",
        ["Addax", "Regice Line", "Peak"],
    ),
    "Regice Line": Area(
        "Regice Line",
        "The snow line of the mountain got its name from the Ice Legendary Pokemon named Regice. This area is his domain and filled with Pokemon. Dont worry about it attacking you, It is mainly in hiding.",
        ["Base", "Peak"],
    ),
    "Peak": Area(
        "Peak",
        "You are on top of the Mountain! There are an elevator and an eriee house. The elevator leads to the Base of the mountain, and the house... Is spoopy!",
        ["Base", "Haunted House"],
    ),
    "Haunted House": Area(
        "Haunted House",
        "Thunder strikes around the house, Clouds on top of the mountain began to turn black. You hear whispers and creeking from the house. The door to the house opens like its inviting you in!",
        ["Peak", "Lobby"],
    ),
    "Lobby": Area(
        "Lobby",
        "It looks just like an abandoned house, but there are wethered Maniquins and a box sitting in the middle of the room. You can also go upstairs!",
        ["Haunted House", "Box", "Upstairs"],
    ),
    "Box": Area(
        "Box",
        "In the middle of the lobby, a two foot wide and three feet tall black box sits there. The box is stripped with red... defenitly not blood... The box has six Maniquin arms and six Maniquin legs attatched to the box. In the middle of the box, there is a circle cut out of the box. On each side of the circle, three golden arrows point to the box! Maybe you can put something in this circle!",
        ["Open", "Lobby"],
    ),
    "Open": Area(
        "Box",
        "In the middle of the lobby, a two foot wide and three feet tall black box sits there. The box is stripped with red... defenitly not blood... The box has six Maniquin arms and six Maniquin legs attatched to the box. In the middle of the box, there is a circle cut out of the box. On each side of the circle, three golden arrows point to the box! Maybe you can put something in this circle!",
        ["Open", "Lobby"],
    ),
    "Upstairs": Area(
        "Upstairs",
        """You go upstairs and to your surprise...
Its you! But something is behind you in the photo. You look closer to the photo and see a silhouette of a man behind you. It looks like the guy will never give you up, never gonna let you down, never gonna run around and desert you! You turn your attention away from the photo and to the end of the room where a ladder is leading you to the Attic!""",
        ["Lobby", "Attic"],
    ),
    "Attic": Area(
        "Attic",
        "You go into the attic and find... Nothing but more Maniquins and empty boxes...",
        ["Upstairs"],
    ),
}

Grasslands = [
    Pokemon(
        "Oddish",
        "Grass",
        29,
        29,
        0,
        False,
        ["Razor Leaf", "Tackle"],
        [random.randint(15, 20), random.randint(10, 20)],
    ),
    Pokemon(
        "Tailow",
        "Normal",
        20,
        20,
        0,
        False,
        ["Peck", "Wing Attack"],
        [random.randint(15, 25), random.randint(30, 35)],
    ),
    Pokemon(
        "Bellsprout",
        "Grass",
        30,
        30,
        0,
        False,
        ["Acid", "Bullet Speed"],
        [random.randint(15, 25), random.randint(10, 20)],
    ),
    Pokemon(
        "Pidgey",
        "Flying",
        20,
        20,
        0,
        False,
        ["Areal Ace", "Air Cutter"],
        [random.randint(40, 50), random.randint(45, 55)],
    ),
]

Forest = [
    Pokemon(
        "Weedle",
        "Bug",
        25,
        25,
        0,
        False,
        ["Poison Sting", "Tackle"],
        [random.randint(25, 35), random.randint(10, 20)],
    ),
    Pokemon(
        "Wurmple",
        "Bug",
        30,
        30,
        0,
        False,
        ["Poison Sting", "Tackle"],
        [random.randint(15, 25), random.randint(10, 20)],
    ),
    Pokemon(
        "Phantump",
        "Ghost",
        35,
        35,
        0,
        False,
        ["Shadow Ball", "Shadow Claw"],
        [random.randint(20, 25), random.randint(25, 30)],
    ),
    Pokemon(
        "Ekans",
        "Poison",
        30,
        30,
        0,
        False,
        ["Acid", "Beat Up"],
        [random.randint(30, 40), random.randint(10, 20)],
    ),
]

River = [
    Pokemon(
        "Electrike",
        "Electric",
        35,
        35,
        0,
        False,
        ["Tackle", "Shockwave"],
        [random.randint(10, 20), random.randint(20, 30)],
    ),
    Pokemon("Magikarp", "Water", 15, 15, 0, False, ["Splash", "Better Splash"], [0, 0]),
    Pokemon(
        "Spheal",
        "Water",
        35,
        35,
        0,
        False,
        ["Rollout", "Water Gun"],
        [random.randint(20, 30), random.randint(25, 35)],
    ),
    Pokemon(
        "Dratini",
        "Dragon",
        40,
        40,
        0,
        False,
        ["Dragon Rage", "Spark"],
        [random.randint(15, 20), random.randint(25, 30)],
    ),
]

Dessert = [
    Pokemon(
        "Cubone",
        "Ground",
        20,
        20,
        0,
        False,
        ["Mud-Slap", "Boomerang"],
        [random.randint(15, 25)],
    ),
    Pokemon(
        "Onix",
        "Rock",
        35,
        35,
        0,
        False,
        ["Tackle", "Sand Tomb"],
        [random.randint(10, 20), random.randint(35, 45)],
    ),
    Pokemon(
        "Gible",
        "Dragon",
        30,
        30,
        0,
        False,
        ["Sand Tomb", "Tackle"],
        [random.randint(25, 35), random.randint(10, 20)],
    ),
    Pokemon(
        "Ponyta",
        "Fire",
        35,
        35,
        0,
        False,
        ["Tackle", "Tail Whip"],
        [random.randint(10, 20), random.randint(25, 35)],
    ),
]

Mountain = [
    Pokemon(
        "Machop",
        "Fighting",
        45,
        45,
        0,
        False,
        ["Revenge", "Low Sweep"],
        [random.randint(45, 50)],
    ),
    Pokemon(
        "Beldum",
        "Steel",
        35,
        35,
        0,
        False,
        ["Iron Head", "Tackle"],
        [random.randint(45, 55), random.randint(10, 20)],
    ),
    Pokemon(
        "Vanillite",
        "Ice",
        30,
        30,
        0,
        False,
        ["Icy Wind", "Avalanche"],
        [random.randint(45, 55), random.randint(50, 60)],
    ),
    Pokemon(
        "Mankey",
        "Fighting",
        40,
        40,
        0,
        False,
        ["Scratch", "Karate Chop"],
        [random.randint(30, 40), random.randint(40, 50)],
    ),
]

Haunted_house = [
    Pokemon(
        "Duskull",
        "Ghost",
        20,
        20,
        0,
        False,
        ["Astonish", "Pursuit"],
        [random.randint(20, 30), random.randint(30, 40)],
    ),
    Pokemon(
        "Pinsir",
        "Bug",
        60,
        60,
        0,
        False,
        ["Body Slam", "Brick Break"],
        [random.randint(50, 60), random.randint(60, 70)],
    ),
    Pokemon(
        "Ralts",
        "Psychic",
        30,
        30,
        0,
        False,
        ["Body Slam", "Double Edge"],
        [random.randint(50, 60), random.randint(60, 70)],
    ),
    Pokemon(
        "Absol",
        "Dark",
        65,
        65,
        0,
        False,
        ["Bite", "Cut"],
        [random.randint(50, 60), random.randint(40, 50)],
    ),
]


def pick_starter(player):
    print(
        f"{player.name}... Interesting... Well, welcome to the newly opened Safari Park, please choose a starter."
    )
    while True:
        print(
            "Treecko the grass pokemon, Mudkip the water pokemon, or Torchic the fire pokemon?"
        )
        starter = input("> ")
        if starter == "Treecko":
            player.party.append(
                Pokemon(
                    "Treecko",
                    "Grass",
                    35,
                    35,
                    0,
                    False,
                    ["Pound", "Absorb"],
                    [random.randint(15, 20), random.randint(25, 26)],
                )
            )
            print("You got the grass type Pokemon Treecko!")
            break
        elif starter == "Mudkip":
            player.party.append(
                Pokemon(
                    "Mudkip",
                    "Water",
                    45,
                    45,
                    0,
                    False,
                    ["Tackle", "Water Gun"],
                    [random.randint(10, 20), random.randint(25, 30)],
                )
            )
            print("You got the water type Pokemon Mudkip!")
            break
        elif starter == "Torchic":
            player.party.append(
                Pokemon(
                    "Torchic",
                    "Fire",
                    30,
                    30,
                    0,
                    False,
                    ["Scratch", "Ember"],
                    [random.randint(15, 20), random.randint(10, 26)],
                )
            )
            print("You got the fire type Pokemon Torchic!")
            break
        else:
            print(
                "We dont have that in our list of starters, please try choosing the correct option."
            )


def area_movement(location):
    while True:
        destination = input("> ")
        if destination in AREA:
            if destination in location.connections:
                location = AREA[destination]
                return location
            else:
                print(f"You cannot go to {destination}!")
                print("Where would you like to go?")
                listing_locations = ""
                for i in location.connections:
                    listing_locations += f"'{i}', "
                print(f"{listing_locations}or <Fly Back>")
        elif destination == "Fly Back":
            location = AREA["Safari Counter"]
            return location
        else:
            print(f"You cannot go to {destination}!")
            print("Where would you like to go?")
            listing_locations = ""
            for i in location.connections:
                listing_locations += f"'{i}', "
            print(f"{listing_locations}or <Fly Back>")


def encounter(player, location):
    if (
        location == AREA["Grasslands"]
        or location == AREA["Prairie"]
        or location == AREA["Pampas"]
        or location == AREA["Savanna"]
    ):
        start = random.randint(1, 4)
        if start == 1:
            pass
        else:
            wild_poke = wild_pokemon(player, location)
            print(f"The wild {wild_poke.name} appears.")
            catch_or_run(player, wild_poke)
    elif (
        location == AREA["The Forest Opening"]
        or location == AREA["Temperate"]
        or location == AREA["Boreal"]
        or location == AREA["Tropical"]
    ):
        start = random.randint(1, 4)
        if start == 1:
            pass
        elif start == 2 or start == 3 or start == 4:
            wild_poke = wild_pokemon(player, location)
            print(f"The wild {wild_poke.name} appears.")
            catch_or_run(player, wild_poke)
    elif (
        location == AREA["Kyoger Falls"]
        or location == AREA["Useless River"]
        or location == AREA["Great Pond"]
    ):
        start = random.randint(1, 4)
        if start == 1:
            pass
        elif start == 2 or start == 3 or start == 4:
            wild_poke = wild_pokemon(player, location)
            print(f"The wild {wild_poke.name} appears.")
            catch_or_run(player, wild_poke)
    elif (
        location == AREA["Poke Beach"]
        or location == AREA["Dust Bowl"]
        or location == AREA["Addax"]
    ):
        start = random.randint(1, 4)
        if start == 1:
            pass
        elif start == 2 or start == 3 or start == 4:
            wild_poke = wild_pokemon(player, location)
            print(f"The wild {wild_poke.name} appears.")
            catch_or_run(player, wild_poke)
    elif (
        location == AREA["Base"]
        or location == AREA["Regice Line"]
        or location == AREA["Peak"]
    ):
        start = random.randint(1, 4)
        if start == 1:
            pass
        elif start == 2 or start == 3 or start == 4:
            wild_poke = wild_pokemon(player, location)
            print(f"The wild {wild_poke.name} appears.")
            catch_or_run(player, wild_poke)
    elif (
        location == AREA["Haunted House"]
        or location == AREA["Lobby"]
        or location == AREA["Upstairs"]
        or location == AREA["Attic"]
    ):
        start = random.randint(1, 4)
        if start == 1:
            pass
        elif start == 2 or start == 3 or start == 4:
            wild_poke = wild_pokemon(player, location)
            print(f"The wild {wild_poke.name} appears.")
            catch_or_run(player, wild_poke)
    elif location == AREA["Safari Counter"]:
        store(player)
    elif location == AREA["PC"]:
        PC_actions(player, location)
    elif location == AREA["Battle Counter"]:
        battlecounter_options(player, location)
    # elif location == AREA["Box"] or location == AREA["Open"]:
    #     if "Gold Medal" in player.items:
    #         print(
    #             "Huh? your Golden Medal is vigorously shacking the closer you get to the box, when you get a closer look, there is a spot for the Medal. Will you insert the Medal into the slot of the box?"
    #         )
    #         insert_option = input("> ")
    #         if insert_option == "yes":
    #             Giratina(player, location)
    #         elif insert_option == "no":
    #             print("Oh well, its probably not that important")
    #         else:
    #             print("Please type yes or no")


def wild_pokemon(player, location):
    if (
        location == AREA["Grasslands"]
        or location == AREA["Prairie"]
        or location == AREA["Pampas"]
        or location == AREA["Savanna"]
    ):
        num = random.randint(0, 3)
        wild_poke = Grasslands[num]
        return wild_poke
    elif (
        location == AREA["The Forest Opening"]
        or location == AREA["Temperate"]
        or location == AREA["Boreal"]
        or location == AREA["Tropical"]
    ):
        num = random.randint(0, 3)
        wild_poke = Forest[num]
        return wild_poke
    elif (
        location == AREA["Kyoger Falls"]
        or location == AREA["Useless River"]
        or location == AREA["Great Pond"]
    ):
        num = random.randint(0, 3)
        wild_poke = River[num]
        return wild_poke
    elif (
        location == AREA["Poke Beach"]
        or location == AREA["Dust Bowl"]
        or location == AREA["Addax"]
    ):
        num = random.randint(0, 3)
        wild_poke = Dessert[num]
        return wild_poke
    elif (
        location == AREA["Base"]
        or location == AREA["Regice Line"]
        or location == AREA["Peak"]
    ):
        num = random.randint(0, 3)
        wild_poke = Mountain[num]
        return wild_poke
    elif (
        location == AREA["Haunted House"]
        or location == AREA["Lobby"]
        or location == AREA["Upstairs"]
        or location == AREA["Attic"]
    ):
        num = random.randint(0, 3)
        wild_poke = Haunted_house[num]
        return wild_poke


def catch_or_run(player, wild_poke):
    if len(player.party) < 5:
        while True:
            attempts = 0
            if attempts < 5:
                print("What will you do?")
                print("Catch")
                print("Run")
                action = input("> ")
                if action == "Run":
                    print("You got away safely...")
                    break
                elif action == "Catch":
                    print(player.items)
                    print("Which Pokeball will you use? ")
                    pokeball = input("> ")
                    if pokeball == "Pokeball" and "Pokeball" in player.items:
                        player.items.remove("Pokeball")
                        catch_rate = random.randint(1, 100)
                        if catch_rate in range(1, 40):
                            player.party.append(wild_poke)
                            print(f"You caught the wild {wild_poke.name}")
                            break
                        else:
                            attempts = attempts + 1
                            print(f"The wild {wild_poke.name} broke out")
                    elif pokeball == "Greatball" and "Greatball" in player.items:
                        player.items.remove("Greatball")
                        catch_rate = random.randint(1, 100)
                        if catch_rate in range(1, 50):
                            player.party.append(wild_poke)
                            print(f"You caught the wild {wild_poke.name}")
                            break
                        else:
                            attempts = attempts + 1
                            print(f"The wild {wild_poke.name} broke out")
                    elif pokeball == "Ultraball" and "Ultraball" in player.items:
                        player.items.remove("Ultraball")
                        catch_rate = random.randint(1, 100)
                        if catch_rate in range(1, 70):
                            player.party.append(wild_poke)
                            print(f"You caught the wild {wild_poke.name}")
                            break
                        else:
                            attempts = attempts + 1
                            print(f"The wild {wild_poke.name} broke out")
                    elif pokeball == "Masterball" and "Masterball" in player.items:
                        player.items.remove("Masterball")
                        player.party.append(wild_poke)
                        print(f"You caught the wild {wild_poke.name}")
                        break
                    else:
                        print("Please input a real pokeball!")
                else:
                    print("You have no time to be dumb, please run away or catch it!")
            else:
                print(f"The {wild_poke.name} ran away!")
                break
    else:
        print(
            f"A wild {wild_poke.name} appeared but you had no space for it, so you ran!"
        )


def store(player):
    while True:
        print("What would you like to buy? or q to quit?")
        print("- Pokeball")
        print("- Greatball")
        print("- Ultraball")
        print("- Masterball")
        action = input("> ")
        if action == "Pokeball" and player.money >= 100:
            print("You got a Pokeball")
            player.items.append("Pokeball")
        elif action == "Greatball" and player.money >= 300:
            print("You got a Greatball")
            player.items.append("Greatball")
        elif action == "Ultraball" and player.money >= 500:
            print("You got a Ultraball")
            player.items.append("Ultraball")
        elif action == "Masterball" and player.money >= 1500:
            if "Gold Medal" in player.items:
                print("You got a Masterball")
                player.items.append("Masterball")
            else:
                print("You do not have a Golden Medal yet!")
        elif action == "q":
            break
        else:
            print("Please select a valid Pokeball or get more money.")


def PC_actions(player, location):
    PC_list = []
    if location == AREA["PC"]:
        print("Do you want to use the PC? Y/N")
        action = input("> ")
        if action == "N":
            print("Have a Good Day!")
        elif action == "Y":
            while True:
                print("What will you like to do?")
                print("Deposit, Withdraw, Heal, or quit?")
                action = input("> ")
                if action == "Deposit" and len(player.party) >= 2:
                    print("Which Pokemon would you like to Deposit?")
                    for pokemon in player.party:
                        print(pokemon.name)
                        action = input("yes or no? ")
                    for pokemon in player.party:
                        if action.lower() == "yes":
                            PC_list.append(pokemon)
                            player.party.remove(pokemon)
                elif action == "Deposit" and len(player.party) < 2:
                    print("You need to keep at least 1 Pokemon in your party!")

                elif action == "Withdraw" and len(player.party) <= 5:
                    for pokemon in PC_list:
                        print(pokemon.name)
                    print("Which Pokemon would you like to Withdraw?")
                    print(PC_list)
                    action = input("> ")
                    for pokemon in PC_list:
                        if action == pokemon.name:
                            player.party.append(pokemon)
                            PC_list.remove(pokemon)
                elif action == "Withdraw" and len(player.party) == 6:
                    print(
                        f"You already have a full party!\nThis is your party: {player.party}"
                    )
                elif action == "Heal":
                    heal(player)
                else:
                    print("Please select a valid option")
        else:
            print("Please select a valid option")


def heal(player: Player) -> None:
    for pokemon in player.party:
        pokemon.fainted = False
        pokemon.health = pokemon.health_cap


def battlecounter_options(player: Player, location: Dict[str, Area]):
    while True:
        print(
            "Welcome to the Battle Counter! What Tower would you like to battle? or press q to quit."
        )
        print("Bronze")
        print("Silver")
        print("Gold")
        action = input("> ")
        if action == "Bronze":
            bronze_tower(player, location)
            break
        elif action == "Silver" and "Bronze Medal" in player.items:
            silver_tower(player, location)
            break
        elif action == "Gold" and "Silver Medal" in player.items:
            gold_tower(player, location)
            break
        elif action == "q":
            break
        else:
            print("Give a valid action")


def bronze_tower(player: Player, location: Dict[str, Area]) -> None:
    print(
        "This is the Bronze Tower you will have fight The Bronze Champion, Jacen`s Pokemon."
    )
    while True:
        if Grasslands[2].fainted == False:
            losers = battle(Grasslands[2], player, location)
            if losers == 1:
                break
        if Forest[3].fainted == False:
            losers = battle(Forest[3], player, location)
            if losers == 1:
                break
        if Grasslands[0].fainted == False:
            losers = battle(Grasslands[0], player, location)
            if losers == 1:
                break
        if Mountain[3].fainted == False:
            losers = battle(Mountain[3], player, location)
            if losers == 1:
                break
        if Haunted_house[1].fainted == False:
            battle(Haunted_house[0], player, location)
            if losers == 1:
                break
            heal_all()
            print("Bronze Champion Jacen has been defeated!")
            player.money += 1000
            player.items.append("Bronze Medal")
            print("For your outstanding battle skills you obtained the Bronze Medal")
            break


def silver_tower(player: Player, location: Dict[str, Area]) -> None:
    print(
        "This is the Silver Tower you will have fight The Silver Champion, Randy`s Pokemon."
    )
    while True:
        if Grasslands[3].fainted == False:
            losers = battle(Grasslands[3], player, location)
            if losers == 1:
                break
        if Forest[0].fainted == False:
            losers = battle(Forest[0], player, location)
            if losers == 1:
                break
        if Grasslands[1].fainted == False:
            losers = battle(Grasslands[1], player, location)
            if losers == 1:
                break
        if Dessert[3].fainted == False:
            losers = battle(Dessert[3], player, location)
            if losers == 1:
                break
        if Haunted_house[2].fainted == False:
            losers = battle(Haunted_house[2], player, location)
            if losers == 1:
                break
        else:
            heal_all()
            print("Silver Champion Randy has been defeated!")
            player.money += 1000
            player.items.append("Silver Medal")
            print("For your outstanding battle skills you obtained the Silver Medal")
            break


def gold_tower(player: Player, location: Dict[str, Area]) -> None:
    print(
        "This is the Gold Tower you will have fight The Gold Champion, Dylan Shipton`s Pokemon."
    )
    while True:
        if Dessert[2].fainted == False:
            losers = battle(Dessert[2], player, location)
            if losers == 1:
                break
        if Mountain[3].fainted == False:
            losers = battle(Mountain[3], player, location)
            if losers == 1:
                break
        if Haunted_house[0].fainted == False:
            losers = battle(Haunted_house[0], player, location)
            if losers == 1:
                break
        if Mountain[3].fainted == False:
            losers = battle(Mountain[3], player, location)
            if losers == 1:
                break
        if Dessert[0].fainted == False:
            losers = battle(Dessert[0], player, location)
            if losers == 1:
                break
        else:
            heal_all()
            print("Silver Champion Dylan Shipton has been defeated!")
            player.money += 1000
            player.items.append("Gold Medal")
            print("For your outstanding battle skills you obtained the Gold Medal")
            print("You can now record your Victory in the hall of Champions")
            champion(player)
            break


def battle(pokemon: Pokemon, player: Player, location: Dict[str, Area]):
    print(f"They send out {pokemon.name}!")
    if player.party[0].fainted == True:
        if player.party[1].fainted == True:
            if player.party[2].fainted == True:
                if player.party[3].fainted == True:
                    in_battle = player.party[4]
                else:
                    in_battle = player.party[3]
            else:
                in_battle = player.party[2]
        else:
            in_battle = player.party[1]
    else:
        in_battle = player.party[0]
    print(f"{player.name} sends out {in_battle.name}")
    while True:
        if in_battle.health > 0:
            print(f"{pokemon.name}: {pokemon.health_cap}/{pokemon.health}")
            print(f"{in_battle.name}: {in_battle.health_cap}/{in_battle.health}")
            for move in in_battle.moves:
                print(move)
            print("What move will you use?")
            action = input("> ")
            if action in in_battle.moves:
                attack = in_battle.moves.index(action)
                print(f"{in_battle.name} used {action}")
                pokemon.health = pokemon.health - in_battle.damage[attack]
                if pokemon.health > 0:
                    trainer_choice = random.randint(1, len(in_battle.moves))
                    trainer_choice = trainer_choice - 1
                    print(f"{pokemon.name} used {pokemon.moves[trainer_choice]}")
                    in_battle.health = in_battle.health - pokemon.damage[trainer_choice]
                    if in_battle.health <= 0:
                        in_battle.fainted = True
                        in_battle.health = 0
                        print(f"{in_battle.name} fainted!")
                else:
                    pokemon.fainted = True
                    pokemon.health = 0
                    print(f"{pokemon.name} fainted!")
                    break
            else:
                print("You can`t use that move")
        if in_battle.health <= 0:
            losers = 0
            for the_party in player.party:
                if the_party.fainted:
                    losers += 1
            if losers == len(player.party):
                death(location, player)
                return losers
                break
            in_battle.fainted == True
            in_battle = switch(in_battle, player)


def switch(in_battle: Pokemon, player: Player) -> Pokemon:
    while True:
        print('Which pokemon would you like to use?')
        for pokemon in player.party:
            if pokemon.fainted == False:
                print(pokemon.name)
        switch = input('> ')
        if switch == pokemon.name:
            in_battle = pokemon
            return in_battle
        else:
            print('Please give a valid pokemon')


def heal_all():
    Grasslands[2].fainted = False
    Forest[3].fainted = False
    Grasslands[0].fainted = False
    Mountain[3].fainted = False
    Haunted_house[0].fainted = False
    Grasslands[3].fainted = False
    Forest[0].fainted = False
    Grasslands[1].fainted = False
    Dessert[3].fainted = False
    Haunted_house[2].fainted = False
    Dessert[2].fainted = False
    Mountain[3].fainted = False
    Haunted_house[0].fainted = False
    Mountain[3].fainted = False
    Dessert[0].fainted = False
    Grasslands[2].health = Grasslands[2].health_cap
    Forest[3].health = Forest[3].health_cap
    Grasslands[0].health = Grasslands[0].health_cap
    Mountain[3].health = Mountain[3].health_cap
    Haunted_house[0].health = Haunted_house[0].health_cap
    Grasslands[3].health = Grasslands[3].health_cap
    Forest[0].health = Forest[0].health_cap
    Grasslands[1].health = Grasslands[1].health_cap
    Dessert[3].health = Dessert[3].health_cap
    Haunted_house[2].health = Haunted_house[2].health_cap
    Dessert[2].health = Dessert[2].health_cap
    Mountain[0].health = Mountain[0].health_cap
    Haunted_house[0].health = Haunted_house[0].health_cap
    Mountain[0].health = Mountain[0].health_cap
    Dessert[2].health = Dessert[2].health_cap


def champion(player: Pokemon) -> None:
    try:
        with open("champion.txt", "r") as x:
            champions = x.readlines()
            amount = len(champions)
        with open("champion.txt", "r") as x:
            print(f"There have been a total of {amount} champions.")
            print(f"{champions[-1]} was the last the Champion")
        with open("champion.txt", "a") as x:
            print("Your name will be wrote down in the Hall Of Champions")
            x.write(f"{player.name}\n")
            x.close()

    except FileNotFoundError:
        print("You are the first champion of the Gold Tower!")
        with open("champion.txt", "a") as x:
            print("Your name will be wrote down in the Hall Of Champions")
            x.write(f"{player.name}\n")
            x.close()


def death(location: Dict[str, Area], player: Player) -> None:
    print('You lost....You died!')
    for pokemon in player.party:
        if pokemon.health <= 0:
            pokemon.health = pokemon.health_cap
        if pokemon.fainted == True:
            pokemon.fainted = False
    heal_all()
    while True:
        print('Do you want to go back, or quit?')
        restart = input('> ')
        if restart == 'yes':
            location = AREA['Safari Counter']
            return location
        elif restart == 'quit':
            quit()
        else:
            print('Give a valid input')


def main():
    location = AREA["Safari Counter"]
    print(
        "Welcome to the world of Pokemon! Here is $1000 and 5 Pokeball`s for you to catch some interesting Pokemon, and of course you will need to pick a starter pokemon, but first!"
    )
    player_name = input("What is your name? ")
    player = Player(
        player_name,
        [],
        1000,
        ["Pokeball", "Pokeball", "Pokeball", "Pokeball", "Pokeball"],
    )
    pick_starter(player)
    while True:
        print(f"You are in the {location.name}")
        print(location.description)
        print("Where would you like to go?")
        listing_locations = ""
        for i in location.connections:
            listing_locations += f"'{i}', "
        print(f"{listing_locations}or 'Fly Home'")
        location = area_movement(location)
        encounter(player, location)


if __name__ == "__main__":
    main()
