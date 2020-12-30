from items import *
from characters import *
from map import *
from random import randint


in_use = [titanovy_mec.name, boots.name, potion.name]

# if titanovy_mec.name in in_use:
#     print("\nVýber útok:\n1.Útok mečem -> udělí 20 požkození\n2.Útok mečem kombinovaný s hamon -> údělí 30 požkození")
# player_move = input("> ")

# if player_move == "1":
#     if titanovy_mec.name in in_use:
#         print(player_move+" is your move")
# else:
#     print(player_move + " WTF?!")

while map[main_character.location][Boss]['a'] != False:
    winner = None
    # turn = randint(1,2)
    turn = 1

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
                print("3.Vyléčení -> vyléčí 15-60 životů")
            if boots.name in in_use:
                print("4.Uhnutí -> vyhneš se dalšímu útoku od nepřítele")

        
        player_move = input("> ")
        move_miss = randint(1,5) # 20% of missing
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
                    print(map[main_character.location][Boss]['hp'])
                elif  kovovy_mec.name in in_use:
                    player_move = actions["kovovy mec"]["sword attack"]
                    map[main_character.location][Boss]['hp'] -= player_move
                    print(map[main_character.location][Boss]['hp'])
                print("\nYou used Punch. It dealt ", player_move, " damage.")
            elif player_move == "2":
                if titanovy_mec.name in in_use:
                    player_move = actions["titanovy mec"]["hamon attack"]
                    map[main_character.location][Boss]['hp'] -= player_move
                    print(map[main_character.location][Boss]['hp'])
                elif  kovovy_mec.name in in_use:
                    player_move = actions["kovovy mec"]["hamon attack"]
                    map[main_character.location][Boss]['hp'] -= player_move
                    print(map[main_character.location][Boss]['hp'])
                print("\nYou used Mega Punch. It dealt ", player_move, " damage.")
            elif player_move == "3":
                if potion.name in in_use:
                    player_move = actions["potion"]["heal"]
                    main_character.hp += actions["potion"]["heal"]
                elif apple.name in in_use:
                    player_move = actions["apple"]["heal"]
                    main_character.hp += actions["apple"]["heal"]
                print("\nYou used Heal. It healed for ", player_move, " health.")
            # if player_move not in ["1", "2", "3", "4"]:
            #     print("\nneplatný příkaz, zadej číslo akce, kterou chceš vykonat.")
            if main_character.hp != 0 and map[main_character.location][Boss]['hp'] <= 0:
                winner = main_character.n
                print("Vyhrál jsi souboj!!")
                map[main_character.location][Boss]['a'] = False
            else:
                winner = map[main_character.location][Boss]['n']
                main_character.a = False   

    # else: # computer turn

    #     move_miss = randint(1,5)
    #     if move_miss == 1:
    #         miss = True
    #     elif boots.name in in_use and player_move == "3":
    #         miss = True
    #     else:
    #         miss = False

    #     if miss:
    #         enemy_move = 0 # the computer misses and deals no damage
    #         if boots.name in in_use and player_move == "3":
    #             print("Použil jsi uhnití "+map[main_character.location][Boss]['n']+" ti nic neubral")
    #         else:
    #             print("Nepřítel minul!")
    #     else:
    #         enemy_move = map[main_character.location][Boss]['dmg']
    #         print(map[main_character.location][Boss]['n']+ " na tebe použil"+ map[main_character.location][Boss]['ab']+" a dal ti "+ str(map[main_character.location][Boss]['dmg'])+" požkození")
    #         print("zbýva ti "+ str(main_character.hp)+" životů")

