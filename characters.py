from random import randint

class MC:
    def __init__(self, name, race, healtpoints, alive, location):
        self.n = name
        self.r = race
        self.hp = healtpoints
        self.a = alive
        self.location = location

class Boss:
    def __init__(self, name, race, healtpoints, damage, ability, alive):
        self.n = name
        self.r = race
        self.hp = healtpoints
        self.dmg = damage
        self.ab = ability
        self.a = alive

main_character = MC("Kane Higashikata", "člověk", 100, True, "a2")
main_boss = Boss("Dracula", "upír", 250, randint(24, 30), "sání krve", True)
mini_boss_1 = Boss("Walker", "zombie", 175, randint(14, 20), "úder ze záhrobí", True)
mini_boss_2 = Boss("Skeletor", "kostlivec", 130, randint(9, 15), "kostní šíp", True)
mini_boss_3 = Boss("Ukz", "skřet", 200, randint(14, 20), "skřetí mnohoúder", True)
mini_boss_4 = Boss("Zombie man", "zombie", 150, randint(14, 20), "úder ze záhrobí", True)
minion = Boss("Pojslič a jeho kloni", "zombie", 75, randint(6, 12), "slabé údery pěstí", True)