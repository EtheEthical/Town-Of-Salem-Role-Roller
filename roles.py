from EtheLeRandom import randint
import playerList

class Coven:
    def __init__(self):
        self.power_selected = False
        self.killing_selected = False
        self.power = ["Coven Leader", "Hex Master", "Witch"]
        self.killing = ["Conjurer", "Jinx", "Ritualist", "Coven Leader"]
        self.everythingelse = ["Dreamweaver",
                               "Enchanter",
                               "Illusionist",
                               "Medusa",
                               "Necromancer",
                               "Poisoner",
                               "Potion Master",
                               "Voodoo Master",
                               "Wilding"]

    def select_role(self, player):
        if not self.power_selected:
            if randint(1, 2) == 1:
                role = self.power[randint(0, len(self.power)-1)]
                playerList.playerRoleList[player] = role
                self.power_selected = True
                if role == "Coven Leader":
                    self.power.remove("Coven Leader")
                    self.killing.remove("Coven Leader")
                    playerList.all_evil_roles.append(role)

            else:
                role = self.everythingelse[randint(0, len(self.everythingelse)-1)]
                self.everythingelse.remove(role)

                if role == "Coven Leader":
                    self.power.remove("Coven Leader")
                    self.killing.remove("Coven Leader")
                    playerList.all_evil_roles.append(role)

        elif not self.killing_selected:
            if randint(1, 2) == 1:
                self.killing_selected = True
                role = self.killing[randint(0, len(self.killing)-1)]
                if role == "Coven Leader":
                    self.power.remove("Coven Leader")
                    self.killing.remove("Coven Leader")
                    playerList.all_evil_roles.append(role)
            else:
                role = self.everythingelse[randint(0, len(self.everythingelse) - 1)]
                self.everythingelse.remove(role)
                if role == "Coven Leader":
                    self.power.remove("Coven Leader")
                    self.killing.remove("Coven Leader")
                    playerList.all_evil_roles.append(role)



        else:
            role = self.everythingelse[randint(0, len(self.everythingelse) - 1)]
            self.everythingelse.remove(role)
            if role == "Coven Leader":
                self.power.remove("Coven Leader")
                self.killing.remove("Coven Leader")

        playerList.playerRoleList[player] = role
        playerList.coven_members.append(role)
        playerList.all_roles.append(role)
        if role == "Coven Leader":
            if role == "Coven Leader":
                try:
                    self.power.remove("Coven Leader")
                    self.killing.remove("Coven Leader")
                except:
                    sixseven = 41


class Apoc:
    def __init__(self):
        self.roles = ["Soul Collector",
                               "Baker",
                               "Plaguebearer",
                               "Beserker",]

    def select_role(self, player):
            role = self.roles[randint(0, len(self.roles) - 1)]
            self.roles.remove(role)
            playerList.playerRoleList[player] = role
            playerList.all_roles.append(role)
            playerList.all_evil_roles.append(role)



class Neutral:
    def __init__(self):
        self.pirate = False
        self.exe = False
        self.evil = ["Pirate",
                     "Jester",
                     "Executioner",
                     "Amnesiac"]
        self.killing = ["Arsonist",
                        "Serial Killer",
                        "Werewolf",
                        "Shroud",
                        "Psychopath"]

    def select_role(self, player):
        if randint(1, 2) == 1:
            role = self.evil[randint(0, len(self.evil)-1)]
            self.evil.remove(role)

        else:
            role = self.killing[randint(0, len(self.killing)-1)]

        if role == "Executioner":
            self.exe = True

        playerList.playerRoleList[player] = role
        if role == "Pirate":
            self.pirate = True
        else:
            playerList.all_roles.append(role)
            playerList.all_evil_roles.append(role)


class Town:
    def __init__(self):
        self.admirer = 0
        self.power_count = 0
        self.alchemist_lol = False
        self.power = ["Alchemist", "Jailor", "Marshal", "Mayor", "Monarch", "Prosecutor", "Duelist"]
        self.everythingelse = ["Admirer",
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

    def select_role(self, player):
        if self.power_count < 3:
            if randint(1, 10) == 1:
                role = self.power[randint(0, len(self.power)-1)]
                self.power.remove(role)
                self.power_count = self.power_count + 1
                playerList.town_roles.append(role)
            else:
                role = self.everythingelse[randint(0, len(self.everythingelse)-1)]
                playerList.town_members.append(player)
                playerList.town_roles.append(role)
        else:
            role = self.everythingelse[randint(0, len(self.everythingelse) - 1)]
            playerList.town_members.append(player)
            playerList.town_roles.append(role)

        playerList.playerRoleList[player] = role
        playerList.all_roles.append(role)
        playerList.town_roles.append(role)

        if role == "Alchemist":
            self.alchemist_lol = True
        if role == "Admirer":
            self.admirer = self.admirer + 1
