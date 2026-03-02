import EtheLeRandom
import roles
import playerList
from EtheLeRandom import randint
from colorama import Fore


success = False

print("Formatting: ")
print("file.txt:")
print("Ethan")
print("Ben")
print("Etc")
print(" ")

while not success:
    path: str = input("Please paste the path to the file that has all the players: ").rstrip()

    try:
        with open(path, 'r') as file:
            for line in file:
                playerList.playerList.append(line.strip())
                success = True
    except:
        print(Fore.RED + "Invalid path!" + Fore.RESET)

def reset_max():
    global maxEvilTeam, MaxCoven, MaxApoc, MaxNeutral
    maxEvilTeam = EtheLeRandom.randint(0, 7)

    MaxCoven = randint(3, 4)
    MaxApoc = maxEvilTeam - MaxCoven

    MaxNeutral = EtheLeRandom.randint(0, len(playerList.playerList) - maxEvilTeam - 7)

    while MaxNeutral + maxEvilTeam < 5:
        MaxNeutral = EtheLeRandom.randint(0, len(playerList.playerList) - maxEvilTeam - 7)

reset_max()


# coven is random from 2-4 and the rest of the maxEvilTeam goes to apoc!!!
# how manny town tho??? gets determined by this!!
# maxEvilTeam (apoc and coven) subtract total players from that, and minus how many town there going to be, if less then 5 evils, reroll how many neutral!

#MaxNeutral = len(playerList.playerList) - MaxApoc - MaxCoven - randint(6, 10)+1

Coven = roles.Coven()

Apoc = roles.Apoc()

Neutral = roles.Neutral()

Town = roles.Town()

def StartNewGame():

    CovenCount = 0
    ApocCount = 0
    NeutralCount = 0

    while playerList.playerList:

        playerfr = playerList.playerList[randint(0, len(playerList.playerList)-1)]

        if CovenCount < MaxCoven:
            Coven.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            CovenCount = CovenCount + 1

        elif ApocCount < MaxApoc:
            Apoc.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            ApocCount = ApocCount + 1

        elif NeutralCount < MaxNeutral:
            Neutral.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            NeutralCount = NeutralCount + 1

        else:
            Town.select_role(playerfr)
            playerList.playerList.remove(playerfr)


try:
    StartNewGame()
except:
    StartNewGame()

no_no_roles = ["Coven Leader", "Dreamweaver", "Illusionist", "Enchanter", "Medusa", "Voodoo Master"]


def alchemy():
    role = "hi"
    if Town.alchemist_lol:
        thing = randint(1, 16)
        if thing < 4:
            pot_role = Coven.power[randint(0, len(Coven.power)-1)]
            if pot_role not in no_no_roles:
                role = pot_role
                print(Fore.CYAN + f"The Alchemists's Ability is {role}!" + Fore.RESET)

            else:
                alchemy()
        elif thing < 8:
            pot_role = Coven.killing[randint(0, len(Coven.killing)-1)]
            if pot_role not in no_no_roles:
                role = pot_role
                print(Fore.CYAN + f"The Alchemists's Ability is {role}!" + Fore.RESET)

            else:
                alchemy()

        else:
            pot_role = Coven.everythingelse[randint(0, len(Coven.everythingelse)-1)]
            if pot_role not in no_no_roles:
                role = pot_role
                print(Fore.CYAN + f"The Alchemist's Ability is {role}!" + Fore.RESET)

            else:
                alchemy()


def clear_screen():
    for i in range(1000):
        print("")


def exe():
    if Neutral.exe:
        thing = playerList.town_members[randint(0, len(playerList.town_members)-1)]
        print(Fore.CYAN + f"The Executioner's Target is {thing}")

def admirer():
    for i in range(Town.admirer):
        thing = playerList.town_members[randint(0, len(playerList.town_members)-1)]
        print(Fore.CYAN + f"The Admirer's Obsession is {thing}")
        playerList.town_members.remove(thing)

def pirate():
    landlubbers = []
    if Neutral.pirate:
        a = playerList.all_roles[randint(0, len(playerList.all_roles)-1)]
        landlubbers.append(a)

        b = playerList.town_roles[randint(0, len(playerList.town_roles)-1)]
        landlubbers.append(b)

        c = playerList.coven_members[randint(0, len(playerList.coven_members)-1)]
        landlubbers.append(c)

        for i in range(len(landlubbers)):
            print(Fore.CYAN + f"Landlubber: {landlubbers[i]}")

#kill yourself, nathan

for k, v in playerList.playerRoleList.items():

    color = Fore.WHITE

    if v in playerList.coven:
        color = Fore.MAGENTA
    if v in playerList.apoc:
        color = Fore.RED
    if v in playerList.neutral:
        color = Fore.YELLOW
    if v in playerList.town:
        color = Fore.GREEN

    print(color + f"{k}: {v}")

print('')
pirate()
alchemy()
exe()
admirer()


while True:
    print("\n\n")
    roll_again = input(Fore.CYAN + "Press enter to roll again!" + Fore.RESET)

    if not roll_again or roll_again:

        clear_screen()

        playerList.playerList.clear()
        playerList.playerRoleList.clear()
        playerList.town_members.clear()
        playerList.coven_members.clear()
        playerList.all_roles.clear()

        Coven = roles.Coven()
        Apoc = roles.Apoc()
        Neutral = roles.Neutral()
        Town = roles.Town()

        with open(path, 'r') as file:
            for line in file:
                playerList.playerList.append(line.strip())

        reset_max()

        StartNewGame()

        for k, v in playerList.playerRoleList.items():
            color = Fore.WHITE
            if v in playerList.coven:
                color = Fore.MAGENTA
            if v in playerList.apoc:
                color = Fore.RED
            if v in playerList.neutral:
                color = Fore.YELLOW
            if v in playerList.town:
                color = Fore.GREEN

            print(color + f"{k}: {v}")

        print('')
        pirate()
        alchemy()
        exe()
        admirer()
