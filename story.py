from game import fight
from game import *

print( "  _______________________________________")
print( " /                                       \ ")
print( "/   _   _   _                 _   _   _   \ ")
print( "|  | |_| |_| |   _   _   _   | |_| |_| |  |")
print( "|   \   _   /   | |_| |_| |   \   _   /   |")
print( "|    | | | |     \       /     | | | |    |")
print( "|    | |_| |______|     |______| |_| |    |")
print( "|    |              ___              |    |")
print( "|    |  _    _    (     )    _    _  |    |")
print( "|    | | |  |_|  (       )  |_|  | | |    |")
print( "|    | |_|       |       |       |_| |    |")
print( "|   /            |_______|            \   |")
print( "|  |___________________________________|  |")
print( "\             Hamon Adventures            /")
print( " \_______________________________________/")

start = input("Začít hru (Ano/Ne):")
start = start.lower()

if start == "ano":
    intro()
elif start == "ne":
    print("Možná příště")    
else:
    print("Neplatná odpověď")


def intro():
    print("    ______________________________")
    print("    / \                             \.")
    print("    |   |                            |.")
    print("    \_ |     Vzbudil ses na pláži a  |.")
    print("        |    před sebou vidíš        |.")
    print("        |    obrovský středověký.    |.")
    print("        |    Nic si nepamatuješ,     |.")
    print("        |    ani své jmnéno.         |.")
    print("        |    Máš u sebe jenom        |.")
    print("        |    pergamen, na ketrém     |.")
    print("        |    je napsáno 'Vyhledat    |.")
    print("        |    a zníčit poslední       |.")
    print("        |    kamennou masku v        |.")
    print("        |    Evropě' a vzpomněl sis  |.")
    print("        |    na svoji misi, na kterou|.")
    print("        |    tě poslali tovoji       |.")
    print("        |    mistři, ale zbytek      |.")  
    print("        |    své minulosti sis       |.")
    print("        |    už nevybavil            |.")
    print("        |   _________________________|___")
    print("        |  /                            /.")
    print("        \_/____________________________/.")

    
    print("na mostě si potkal nekoho nějakou postavu")
    print("\n1.Kdo jsi\n2.Uhni nemám na tebe čas")
    answer = input("> ")

    if answer == "1":
        print("Já jsem Pojlič, strážce mostu, co tu pohledáváš")
        print("\n1.Já jsem Kane Higashikata a mám tu byznys s Drákulou\n2.Uhni nemám na tebe čas")
        answer = input("> ")
        if answer == "1":
            print("S mistrem nemá nikdo právo mluvit, odejdi nebo zemři")
            fight()
    elif answer == "2":
        fight()
        print("porazil jsi Pojsliče, našel jsi u něj mapu a přešel jsi most")
        prikaz = input("co mám dělat")
        movement()


