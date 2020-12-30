from characters import*
from item_appearance import *
from items import *
from map import *
import random


commands = ["up", "back", "left", "riht", "navod", "zkoumat", "information", "inevtory", "současná poloha", "pouzit"]
inventory = []
in_use = []
prikaz = input("co dělat:")
prikaz = prikaz.lower()

if prikaz not in commands:
    print("neplatný přákaz")

def movement():
    if prikaz == commands[0]:
        if map[main_character.location][Up] == False:
            print("zde není žádná místnost")
        else:
            main_character.location = map[main_character.location][Up]
            print("Nacházíš se v " + map[main_character.location][Room])     
    elif prikaz == commands[1]:
        if map[main_character.location][Back] == False:
            print("zde není žádná místnost")
        else:
            main_character.location = map[main_character.location][Back]
            print("Nacházíš se v " + map[main_character.location][Room])
    elif prikaz == commands[2]:
        if map[main_character.location][Left] == False:

            print("zde není žádná místnost")
        else:
            main_character.location = map[main_character.location][Left]
            print("Nacházíš se v " + map[main_character.location][Room])
    elif prikaz == commands[3]: 
        if map[main_character.location][Right] == False:
            print("zde není žádná místnost")
        else:
            main_character.location = map[main_character.location][Right]
            print("Nacházíš se v " + map[main_character.location][Room])

    if map[main_character.location][Boss] != False:
        fight()
    else:
        print("V místnosti "+ map[main_character.location][Room])


def add_to_inventory():
    if map[main_character.location][Item] != False:
        odpoved = input("přidat do inventáře? (y/n)")
        if odpoved == 'y':
            inventory.append(map[main_character.location][Item]['name'])
        else:
            print("předmět nebyl přidát do inventáře")

def in_use(prikaz):
    if prikaz == commands[7]:
        command = input("napiš jméno předmětu, který chceš použít:")
        if command in inventory:
            in_use.append(command)
            consumabels = [potion.name, apple.name]
        if command in consumabels:
            inventory.remove(command)



def examine():
    print(map[main_character.location][Story])
    if map[main_character.location][Item] != False:
        print(map[main_character.location][Item]['name'])
        print(map[main_character.location][Item]['description'])
        


def fight():
    while map[main_character.location][Boss]['hp'] != False and main_character.a != False:
        winner = None
        turn = random.randint(1,2)

        if turn == 1:
            player_turn = True
            enemy_turn = False
            print("Jsi na řadě")
        else:
            player_turn = False
            enemy_turn = True
            print(map[main_character.location][Boss]['n'] +" je na řadě")

        while map[main_character.location][Boss]['hp'] != 0 or main_character.hp != 0:
            miss = False
            if player_turn:
                if titanovy_mec.name in in_use:
                    print("\nVýber útok:\n1.Útok mečem -> udělí 20 požkození\n2.Útok mečem kombinovaný s hamon -> údělí 30 požkození")
                elif kovovy_mec.name in in_use:
                    print("\nVýber útok:\n1.Útok mečem -> udělí 15 požkození\n2.Útok mečem kombinovaný s hamon -> údělí 24 požkození")
                else:
                    print("\nVýber útok:\n1.Útok pěstí -> udělí 5-8 požkození\n2.Útok mečem kombinovaný s hamon -> údělí 10-15 požkození")
                if (potion.name or apple.name) in in_use:
                    print("3.Vyléčení -> vyléčí 10-20 životů")
                if boots.name in in_use:
                    print("4.Uhnutí -> vyhneš se dalšímu útoku od nepřítele")

            
            player_move = input("> ")
            move_miss = random.randint(1,5) # 20% of missing
            if move_miss == 1:
                miss = True
            else:
                miss = False

            if miss:
                player_move = 0 # player misses and deals no damage
                print("minul si")
            else:
                if player_move == "1":
                    if titanovy_mec.name in in_use:
                        player_move = actions["titanovy mec"]["sword attack"]
                        map[main_character.location][Boss]['hp'] -= player_move
                    elif  kovovy_mec.name in in_use:
                        player_move = actions["kovovy mec"]["sword attack"]
                        map[main_character.location][Boss]['hp'] -= player_move
                    print("\nYou used Punch. It dealt ", player_move, " damage.")
                elif player_move == "2":
                    if titanovy_mec.name in in_use:
                        player_move = actions["titanovy mec"]["hamon attack"]
                        map[main_character.location][Boss]['hp'] -= player_move
                    elif  kovovy_mec.name in in_use:
                        player_move = actions["kovovy mec"]["hamon attack"]
                        map[main_character.location][Boss]['hp'] -= player_move
                    print("\nYou used Mega Punch. It dealt ", player_move, " damage.")
                elif player_move == "3":
                    heal_up = True # heal activated
                    if potion.name in in_use:
                        player_move = actions["potion"]["heal"]
                    elif apple.name in in_use:
                        player_move = actions["apple"]["heal"]
                    print("\nYou used Heal. It healed for ", player_move, " health.")
                else:
                    print("\nneplatný příkaz, zadej číslo akce, kterou chceš vykonat.")
                    continue

        else: # computer turn

            move_miss = random.randint(1,5)
            if move_miss == 1:
                miss = True
            elif boots.name in in_use and player_move == "3":
                miss = True
            else:
                miss = False

            if miss:
                enemy_move = 0 # the computer misses and deals no damage
                if boots.name in in_use and player_move == "3":
                    print("Použil jsi uhnití "+map[main_character.location][Boss]['n']+" ti nic neubral")
                else:
                    print("Nepřítel minul!")
            else:
                enemy_move = map[main_character.location][Boss]['dmg']
                print(map[main_character.location][Boss]['n']+ " na tebe použil"+ map[main_character.location][Boss]['ab']+" a dal ti "+ str(map[main_character.location][Boss]['dmg'])+" požkození")
                print("zbýva ti "+ str(main_character.hp)+" životů")

        if main_character.hp != 0 and map[main_character.location][Boss]['hp'] == 0:
            winner = main_character.n
            map[main_character.location][Boss]['hp'] != False
        else:
            winner = map[main_character.location][Boss]['n']
            main_character.a != False




if prikaz == commands[4]:
    print("        _______________________________________________________")
    print("        /\                                                      \ ")
    print("    (O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("        \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/")
    print("        (                                                      (")
    print("        )  Přílazy k pohybu jsou 'u', 'b', 'l', 'r'.           )")
    print("        (  'up' slouží k pohybu dopředu.                       (")
    print("        )  'back' slouží k pohybu zpět .                       )")
    print("           'left' slouží k pohybu do leva.                     )")
    print("        (  'right' slouží k pohybu do prava                    (")
    print("        )  'inventory' otevře inventář                         )")
    print("        (  'info' vypíše jméno a příjmení autora,              (")
    print("        )   den zahájení práce, den ukončení práce,            )")
    print("            odhadovaný čas práce v hodinách                     ")
    print("        (   'zkoumat' ukáže příběh nebo schopnost              (")
    print("        )   zbraně či místnosti                                )")
    print("        (   'sp' zkratka pro 'současná poloha'                 (")
    print("        )   vypíše tvoji současnou pozici                      )")
    print("                                                               ")
    print("        (                                                      (")
    print("        )                                                      )")
    print("        (                                                      (")
    print("        /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\ ")    
    print("    (O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)")
    print("        \/______________________________________________________/")

elif prikaz in ["up", "back", "left", "right"]:
    movement()
elif prikaz == commands[5]:
    examine()
elif prikaz == commands[7]:
    print(inventory)
elif prikaz == commands[8]:
    print( map[main_character.location][Room])
