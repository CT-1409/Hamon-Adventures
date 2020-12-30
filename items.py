from random import randint

class Weapons:
    def __init__(self, n, des, dmg):
        self.name = n
        self.description = des
        self.damage = dmg

class Armour_and_Special_items:
    def __init__(self, n, des, e):
        self.name = n
        self.description = des
        self.effect = e

titanovy_mec = Weapons("titanový meč", "skvěle vede hamon, je lehký a odolný, jediný svého druhu, s příměsí stříbra pro boj againts monsters", 20)
kovovy_mec = Weapons("normální kovový meč","těžký, ve všem průměrný", 12)
key = Armour_and_Special_items("klíč krále Šalamouna", "klíč krále Šalamouna, očarovaný aby dokázal odemknout všechny dveře", "otevře všechny dveře")
boots = Armour_and_Special_items("boty strážce Zoubka", "tyto boty mají schopnost, které dávají možnost u6ivateli vzhnout všem nepřátelským útokům, ale jsou velice vzácné, vyrobené ze sls lidí co nenosí přezuvky", "uhnutí bude stát 0 many")
scroll = Armour_and_Special_items("svitek pravdy", "pokud hráč tento sitek najde, dozví se příběh svůj příběh", "vidění pravdy")
potion = Armour_and_Special_items("lektvar zdravý", "kouzelný lektvar, který umí léčit","vyléčí 10-14 životů")
apple = Armour_and_Special_items("jablko života", "dle legendy rostou jenom v zahradách hradu", "vyléčí 15-20 životů")


actions = {
    "titanovy mec":{
        "sword attack": randint(16, 20),
        "hamon attack": randint(21, 30)
    },
    "kovovy mec":{
        "sword attack": randint(9, 15),
        "hamon attack": randint(16, 24)
    },
    "potion":{
        "heal": randint(15, 45),
    },
    "apple":{
        "heal": randint(46, 60),
    }
}