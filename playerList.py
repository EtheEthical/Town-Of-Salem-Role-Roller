playerList = []

playerRoleList = {}

def forceRole(name, role, town):
    for key, value in playerRoleList.items():
        if value == role:
            town.select_role(key)
            break

    playerRoleList[name] = role





coven = [
"Coven Leader", "Hex Master", "Witch", "Conjurer",
                               "Dreamweaver",
                               "Enchanter",
                               "Illusionist",
                               "Jinx",
                               "Medusa",
                               "Necromancer",
                               "Poisoner",
                               "Potion Master",
                               "Ritualist",
                               "Voodoo Master",
                               "Wilding"
]

neutral = ["Pirate",
                     "Jester",
                     "Executioner",
                     "Amnesiac",
                      "Arsonist",
                        "Serial Killer",
                        "Werewolf",
                        "Shroud",
                        "Psychopath"]

apoc = ["Soul Collector",
                               "Baker",
                               "Plaguebearer",
                               "Beserker",]

town = ["Alchemist",
        "Jailor",
        "Marshal",
        "Mayor",
        "Monarch",
        "Prosecutor",
        "Duelist",
        "Admirer",
        "Bodyguard",
        "Catalyst",
        "Cleric",
        "Coroner",
        "Crusader",
        "Investigator",
        "Lookout",
        "Oracle",
        "Psychic",
        "Retributionist",
        "Seer",
        "Sheriff",
        "Socialite",
        "Spy",
        "Trapper",
        "Tavern Keeper",
        "Deputy",
        "Trickster",
        "Veteran",
        "Vigilante"]


town_members = []
coven_members = []
town_roles = []

all_evil_roles = []
#sybau sean

all_roles = []