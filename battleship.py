import time as t
import os
import random as r
import colorama
from colorama import Fore, Style


def clear():
    """Clear the shell/output"""
    clr = os.system("clear")
    clr


def player_board():
    """Print out the player board with the symbol definitions"""
    print("   1  2  3  4  5  6  7  8  9")
    counter = 0
    for i in plr_board:
        if counter % 10 == 0 and counter != 0:
            print()
        print(i, end="")
        counter += 1
    print("\t\tC- Carrier\tB- Battleship\tR- Cruiser\tS- Submarine\tD- Destroyer")


def computer_board():
    """Print out the computer board. Used for testing purposes"""
    print("   1  2  3  4  5  6  7  8  9")
    counter2 = 0
    for i in comp_board:
        if counter2 % 10 == 0 and counter2 != 0:
            print()
        print(i, end="")
        counter2 += 1
    print()


def opponent_board():
    """Print out the board the player sees their hits and misses. Used for testing purposes"""
    print("   1  2  3  4  5  6  7  8  9")
    counter3 = 0
    for i in opp_board:
        if counter3 % 10 == 0 and counter3 != 0:
            print()
        print(i, end="")
        counter3 += 1
    print("\t\tC- Carrier\tB- Battleship\tR- Cruiser\tS- Submarine\tD- Destroyer")


def check_vaild(input1, input2, size):
    """
    Checks is the ship coordinates are valid if the ship is placed verticaly
    input1 is the first coordinate of the ship
    input2 is the second coordinate of the ship
    size is the size of the ship
    """
    values = {
        "val_a": 1,
        "val_b": 2,
        "val_c": 3,
        "val_d": 4,
        "val_e": 5,
        "val_f": 6,
        "val_g": 7,
        "val_h": 8,
        "val_i": 9,
    }
    cl1 = "val_" + input1[0].lower()
    cl2 = "val_" + input2[0].lower()
    cce1 = input1[1]
    cce2 = input2[1]
    key1 = values.get(cl1)
    key2 = values.get(cl2)
    if (key2 - key1 == size or key1 - key2 == size) and (cce1 == cce2):
        return True
    else:
        return False


def deploy_fleet(cord1, cord2, name):
    """
    Edit the players board with the ship the player deployed
    cord1 is the first coordinate of the ship
    cord2 is the second coordinate of the ship
    name is the symbol that is used to represent the ship
    """
    val = {
        "A": 0,
        "B": 10,
        "C": 20,
        "D": 30,
        "E": 40,
        "F": 50,
        "G": 60,
        "H": 70,
        "I": 80,
    }
    row1 = cord1[0]
    row2 = cord2[0]
    num1 = int(cord1[1])
    num2 = int(cord2[1])

    length = -num1 + num2
    inc = 0
    if length > 0:
        length += 1
        inc = 1
    else:
        length -= 1
        inc = -1
    name = "  " + name
    if row1 == row2:
        key = val.get(row1)
        for i in range(num1 + key, num1 + length + key, inc):
            plr_board.pop(i)
            plr_board.insert(i, name)
    else:
        key3, key4 = find_larger(row1, row2)
        if key3 > key4:
            inc = -10
        else:
            inc = 10
        key1 = val.get(row1)
        key2 = val.get(row2)
        for i in range(num1 + key1, num1 + length + key2 + 10, inc):
            plr_board.pop(i)
            plr_board.insert(i, name)


def find_larger(input1, input2):
    """
    Finds which of the two coordinates of the ship are larger (further from the top)
    input1 is the first coordinate of the ship
    input2 is the second coordinate of the ship
    """
    values = {
        "val_A": 1,
        "val_B": 2,
        "val_C": 3,
        "val_D": 4,
        "val_E": 5,
        "val_F": 6,
        "val_G": 7,
        "val_H": 8,
        "val_I": 9,
    }
    cl1 = "val_" + input1
    cl2 = "val_" + input2
    key3 = values.get(cl1)
    key4 = values.get(cl2)
    return key3, key4


def check_valid3(cord1, cord2):
    """ 
    This checks if the players ship, using cord1 and cord2, is trying to be placed in the way of another ship
    cord1 is the first coordinate of the ship
    cord2 is the second coordinate of the ship
    """
    val = {
        "A": 0,
        "B": 10,
        "C": 20,
        "D": 30,
        "E": 40,
        "F": 50,
        "G": 60,
        "H": 70,
        "I": 80,
    }

    row1 = cord1[0]
    row2 = cord2[0]
    num1 = int(cord1[1])
    num2 = int(cord2[1])

    length = -num1 + num2
    inc = 0
    return_val = False
    if length > 0:
        length += 1
        inc = 1
    else:
        length -= 1
        inc = -1

    if row1 == row2:
        key = val.get(row1)
        for i in range(num1 + key, num1 + length + key, inc):
            if plr_board[i] == "  _":
                return_val = True
            else:
                return_val = False
                break

    else:
        key3, key4 = find_larger(row1, row2)
        if key3 > key4:
            inc = -10
        else:
            inc = 10
        key1 = val.get(row1)
        key2 = val.get(row2)
        for i in range(num1 + key1, num1 + length + key2 + 10, inc):
            if plr_board[i] == "  _":
                return_val = True
            else:
                return_val = False
                break
    return return_val

def check_valid4(cord1, cord2):
    """
    Checks if the ship is all in the same row or same column
    cord1 is the first coordinate of the ship
    cord2 is the second coordinate of the ship
    """
    row1 = cord1[0]
    row2 = cord2[0]
    num1 = int(cord1[1])
    num2 = int(cord2[1])
    if row1==row2 or num1==num2:
        return True
    else:
        return False

def check_valid2(cord1, cord2):
    """ 
    This checks if the computers ship, using cord1 and cord2, is trying to be placed in the way of another ship
    cord1 is the first coordinate of the ship
    cord2 is the second coordinate of the ship
    """
    val = {
        "A": 0,
        "B": 10,
        "C": 20,
        "D": 30,
        "E": 40,
        "F": 50,
        "G": 60,
        "H": 70,
        "I": 80,
    }

    row1 = cord1[0]
    row2 = cord2[0]
    num1 = int(cord1[1])
    num2 = int(cord2[1])

    length = -num1 + num2
    inc = 0
    return_val = False
    if length > 0:
        length += 1
        inc = 1
    else:
        length -= 1
        inc = -1

    if row1 == row2:
        key = val.get(row1)
        for i in range(num1 + key, num1 + length + key, inc):
            if comp_board[i] == "  _":
                return_val = True
            else:
                return_val = False
                break

    else:
        key3, key4 = find_larger(row1, row2)
        if key3 > key4:
            inc = -10
        else:
            inc = 10
        key1 = val.get(row1)
        key2 = val.get(row2)
        for i in range(num1 + key1, num1 + length + key2 + 10, inc):
            if comp_board[i] == "  _":
                return_val = True
            else:
                return_val = False
                break
    return return_val


def deploy_x(x_deployed, x_c1, x_c2, x_length, x_symbol, x_name):
    """
    This is the deploy function for the player
    
    More detail comming soon...

    x_c1 is the first coordinate of the ship
    x_c2 is the second coordinate of the ship
    x_length is the length of the ship
    x_symbol is the symbol of the ship
    x_name is what the ship is called
    """
    x_length -= 1
    while x_deployed == False:
        x_length += 1
        try:
            x_c1 = input(
                "Input coordinate for "
                + x_name
                + " (Size: "
                + str(x_length)
                + ")(E.g. 'A1'): "
            )
            x_c2 = input("Input coordinate for " + x_name + ": ")
            cc1 = int(x_c1[1])
            cc2 = int(x_c2[1])
            x_length -= 1
            if (
                (cc2 - cc1 == x_length or cc1 - cc2 == x_length)
                or check_vaild(x_c1, x_c2, x_length)
            ) and check_valid3(x_c1, x_c2) and check_valid4(x_c1, x_c2):
                deploy_fleet(x_c1, x_c2, x_symbol)
                print(Style.RESET_ALL)
                print(Fore.RED + x_name.title() + " deployed!")
                print(Style.RESET_ALL)
                t.sleep(1)
                clear()
                player_board()
                break

            else:
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "Invalid coordinate")
                print(Style.RESET_ALL)
                t.sleep(1.5)
                clear()
                player_board()
        except:
            print(Style.RESET_ALL)
            print(Fore.YELLOW + "Invalid coordinate(s)")
            print(Style.RESET_ALL)
            x_length -= 1
            t.sleep(1.5)
            clear()
            player_board()


def deploy_fleet_comp(cord1, cord2, name):
    """
    Edit the computers board with the ship the computer deployed
    cord1 is the first coordinate of the ship
    cord2 is the second coordinate of the ship
    name is the symbol that is used to represent the ship
    """
    val = {
        "A": 0,
        "B": 10,
        "C": 20,
        "D": 30,
        "E": 40,
        "F": 50,
        "G": 60,
        "H": 70,
        "I": 80,
    }
    row1 = cord1[0]
    row2 = cord2[0]
    num1 = int(cord1[1])
    num2 = int(cord2[1])

    length = -num1 + num2
    inc = 0
    if length >= 0:
        length += 1
        inc = 1
    else:
        length -= 1
        inc = -1
    name = "  " + name
    if row1 == row2:
        key = val.get(row1)
        for i in range(num1 + key, num1 + length + key, inc):
            comp_board.pop(i)
            comp_board.insert(i, name)
    else:
        key3, key4 = find_larger(row1, row2)
        if key3 > key4:
            inc = -10
            length -= 2
        else:
            inc = 10
        key1 = val.get(row1)
        key2 = val.get(row2)
        for i in range(num1 + key1, num1 + length + key2, inc):
            comp_board.pop(i)
            comp_board.insert(i, name)


def deploy_x_comp(x_deployed, x_c1_comp, x_c2_comp, x_length, x_symbol, x_name):
    """
    This is the deploy function for the computer
    
    More detail comming soon...

    x_deployed is if the ship has been deployed/placed on the board
    x_c1_comp is the first coordinate of the ship
    x_c2_comp is the second coordinate of the ship
    x_length is the length of the ship
    x_symbol is the symbol of the ship
    x_name is what the ship is called
    """
    x_length -= 1
    while x_deployed == False:
        x_length += 1
        r.shuffle(cells)
        x_c1_comp = r.choice(cells)  # A1
        r.shuffle(cells)
        while True:
            x_c2_comp = r.choice(cells)
            if x_c2_comp[0] == x_c1_comp[0] or x_c2_comp[1] == x_c1_comp[1]:
                break
        cc1 = int(x_c1_comp[1])
        cc2 = int(x_c2_comp[1])
        x_length -= 1
        if (
            (cc2 - cc1 == x_length or cc1 - cc2 == x_length)  # Same row
            or check_vaild(x_c1_comp, x_c2_comp, x_length)  # Same column
        ) and check_valid2(
            x_c1_comp, x_c2_comp
        ):  # Checks if space is taken
            deploy_fleet_comp(x_c1_comp, x_c2_comp, x_symbol)
            break


def greet_player():
    """ Just the starting greeting for the player"""
    clear()
    print("Welcome to battle ship!")
    t.sleep(1)
    print("**Work in progress**")
    t.sleep(1)
    print("Current mode: Player VS computer")
    input("Press enter to start! ")
    clear()
    player_board()


def get_index(cord):
    """ 
    Gets the index of the cordinate
    cord is the coordinate
    """
    val = {
        "A": 0,
        "B": 10,
        "C": 20,
        "D": 30,
        "E": 40,
        "F": 50,
        "G": 60,
        "H": 70,
        "I": 80,
    }
    row = cord[0].upper()
    num = int(cord[1])

    # name = "  " + name
    key = val.get(row)
    index1 = num + key
    return index1


def update_board():
    """Checks if any of the ships are sunken, for the player and computer. If so prints, it will print the ships name out"""
    global carrier_sunken, battleship_sunken, cruiser_sunken, submarine_suken, destroyer_sunken
    global carrier_sunken_comp, battleship_sunken_comp, cruiser_sunken_comp, submarine_suken_comp, destroyer_sunken_comp
    if (
        "  C" not in comp_board[0:20] and "  C" not in comp_board[21:]
    ) and carrier_sunken_comp == False:
        print("You have sunk the opponents carrier!")
        carrier_sunken_comp = True

    if (
        "  B" not in comp_board[0:10]
        and "  B" not in comp_board[11:]
        and battleship_sunken_comp == False
    ):
        print("You have sunk the opponents battleship!")
        battleship_sunken_comp = True

    if "  R" not in comp_board and cruiser_sunken_comp == False:
        print("You have sunk the opponents cruiser!")
        cruiser_sunken_comp = True

    if "  S" not in comp_board and submarine_suken_comp == False:
        print("You have sunk the opponents submarine!")
        submarine_suken_comp = True

    if (
        "  D" in comp_board[0:30] and "  D" in comp_board[31:]
    ) and destroyer_sunken_comp == False:
        print("You have sunk the opponents destroyer!")
        destroyer_sunken_comp = True

    if (
        "  C" not in plr_board[0:20] and "  C" not in plr_board[21:]
    ) and carrier_sunken == False:
        print("Your carrier has been sunk!")
        carrier_sunken = True

    if (
        "  B" not in plr_board[0:10]
        and "  B" not in plr_board[11:]
        and battleship_sunken == False
    ):
        print("Your battleship has been sunk!")
        battleship_sunken = True

    if "  R" not in plr_board and cruiser_sunken == False:
        print("Your cruiser has been sunk!")
        cruiser_sunken = True

    if "  S" not in plr_board and submarine_suken == False:
        print("Your submarine has been sunk!")
        submarine_suken = True

    if (
        "  D" not in plr_board[0:30] and "  D" not in plr_board[31:]
    ) and destroyer_sunken == False:
        print("Your destroyer has been sunk!")
        destroyer_sunken = True


plr_board = [
    "A",
    "  _",  # A1
    "  _",  # A2
    "  _",  # A3
    "  _",  # A4
    "  _",  # A5
    "  _",  # A6
    "  _",
    "  _",
    "  _",
    "B",
    "  _",  # B1
    "  _",  # B2
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "C",
    "  _",  # C1
    "  _",  # C2
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "D",
    "  _",  # D1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "E",
    "  _",  # E1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "F",
    "  _",  # F1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "G",
    "  _",  # G1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "H",
    "  _",  # H1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "I",
    "  _",  # I1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
]  # Players board
opp_board = [
    "A",
    "  _",  # A1
    "  _",  # A2
    "  _",  # A3
    "  _",  # A4
    "  _",  # A5
    "  _",  # A6
    "  _",
    "  _",
    "  _",
    "B",
    "  _",  # B1
    "  _",  # B2
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "C",
    "  _",  # C1
    "  _",  # C2
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "D",
    "  _",  # D1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "E",
    "  _",  # E1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "F",
    "  _",  # F1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "G",
    "  _",  # G1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "H",
    "  _",  # H1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "I",
    "  _",  # I1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
]  # Board that the player sees their hits and misses
comp_board = [
    "A",
    "  _",  # A1
    "  _",  # A2
    "  _",  # A3
    "  _",  # A4
    "  _",  # A5
    "  _",  # A6
    "  _",
    "  _",
    "  _",
    "B",
    "  _",  # B1
    "  _",  # B2
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "C",
    "  _",  # C1
    "  _",  # C2
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "D",
    "  _",  # D1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "E",
    "  _",  # E1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "F",
    "  _",  # F1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "G",
    "  _",  # G1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "H",
    "  _",  # H1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "I",
    "  _",  # I1
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
    "  _",
]  # Computers board

cells = [
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6",
    "B7",
    "B8",
    "B9",
    "C1",
    "C2",
    "C3",
    "C4",
    "C5",
    "C6",
    "C7",
    "C8",
    "C9",
    "D1",
    "D2",
    "D3",
    "D4",
    "D5",
    "D6",
    "D7",
    "D8",
    "D9",
    "E1",
    "E2",
    "E3",
    "E4",
    "E5",
    "E6",
    "E7",
    "E8",
    "E9",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "G1",
    "G2",
    "G3",
    "G4",
    "G5",
    "G6",
    "G7",
    "G8",
    "G9",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "H7",
    "H8",
    "H9",
    "I1",
    "I2",
    "I3",
    "I4",
    "I5",
    "I6",
    "I7",
    "I8",
    "I9",
]  # Cells that the computer can choose from when attacking the player

plr_used_cells = []

# _____ Greet the player _____
greet_player()

# _____ Player deployed booleans _____
carrier_deployed = False
battleship_deployed = False
cruiser_deployed = False
submarine_deployed = False
destroyer_deployed = False

# _____ Computer deployed booleans _____
carrier_deployed_comp = False
battleship_deployed_comp = False
cruiser_deployed_comp = False
submarine_deployed_comp = False
destroyer_deployed_comp = False

# _________ Deploy player ships __________
carrier_c1 = ""
carrier_c2 = ""
deploy_x(carrier_deployed, carrier_c1, carrier_c2, 5, "C", "carrier")

battleship_c1 = ""
battleship_c2 = ""
deploy_x(battleship_deployed, battleship_c1, battleship_c2, 4, "B", "battleship")

cruiser_c1 = ""
cruiser_c2 = ""
deploy_x(cruiser_deployed, cruiser_c1, cruiser_c2, 3, "R", "cruiser")

submarine_c1 = ""
submarine_c2 = ""
deploy_x(submarine_deployed, submarine_c1, submarine_c2, 3, "S", "submarine")

destroyer_c1 = ""
destroyer_c2 = ""
deploy_x(destroyer_deployed, destroyer_c1, destroyer_c2, 2, "D", "destroyer")
clear()

# _________ Deploy computer ships __________
print("Your fleet has been deployed!")
print("Generating computer fleet!")
t.sleep(1.5)
carrier_c1_comp = ""
carrier_c2_comp = ""
deploy_x_comp(
    carrier_deployed_comp, carrier_c1_comp, carrier_c2_comp, 5, "C", "carrier"
)
battleship_c1_comp = ""
battleship_c2_comp = ""
deploy_x_comp(
    battleship_deployed_comp,
    battleship_c1_comp,
    battleship_c2_comp,
    4,
    "B",
    "battleship",
)
cruiser_c1_comp = ""
cruiser_c2_comp = ""
deploy_x_comp(
    cruiser_deployed_comp, cruiser_c1_comp, cruiser_c2_comp, 3, "R", "cruiser"
)
submarine_c1_comp = ""
submarine_c2_comp = ""
deploy_x_comp(
    submarine_deployed_comp, submarine_c1_comp, submarine_c2_comp, 3, "S", "submarine"
)
destroyer_c1_comp = ""
destroyer_c2_comp = ""
deploy_x_comp(
    destroyer_deployed_comp, destroyer_c1_comp, destroyer_c2_comp, 2, "D", "destroyer"
)
print("Computer fleet has been deployed")
t.sleep(1.5)


# Boolean for whether player ships have been sunk
carrier_sunken = False
battleship_sunken = False
cruiser_sunken = False
submarine_suken = False
destroyer_sunken = False

# Boolean for whether computer ships have been sunk
carrier_sunken_comp = False
battleship_sunken_comp = False
cruiser_sunken_comp = False
submarine_suken_comp = False
destroyer_sunken_comp = False

# Loop that runs the game (the attacking part)
while True:
    clear()
    print("Your board: ")
    player_board()
    print("\nOpponents board")
    opponent_board()
    # ______ Players's turn ______
    while True:
        # ______ Players turn ______
        attack_cords = input("Input coordinates (E.g. A1): ")
        try:
            if (
                attack_cords[0].lower() in "abcdefghij"
                and attack_cords[1] in "123456789"
                and attack_cords not in plr_used_cells
            ):
                break
            elif attack_cords in plr_used_cells:
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "You already tried this")
                print(Style.RESET_ALL)
            else:
                print(Style.RESET_ALL)
                print(Fore.YELLOW + "Invalid coordinates")
                print(Style.RESET_ALL)
        except:
            print(Style.RESET_ALL)
            print(Fore.YELLOW + "Invalid coordinates")
            print(Style.RESET_ALL)
    print("Launching missile!\t (X- Hit   O- Miss)")
    index_of_attack = get_index(attack_cords)
    opp_board.pop(index_of_attack)
    plr_used_cells.append(attack_cords)
    if comp_board[index_of_attack].strip() != "_":
        opp_board.insert(index_of_attack, "  X")
        print(Style.RESET_ALL)
        print(Fore.RED + "You hit a ship at " + attack_cords + "!")
        print(Style.RESET_ALL)
        comp_board.pop(index_of_attack)
        comp_board.insert(index_of_attack, "  _")
        update_board()
    else:
        opp_board.insert(index_of_attack, "  O")
        print(Style.RESET_ALL)
        print(Fore.RED + "You missed at " + attack_cords)
        print(Style.RESET_ALL)
    t.sleep(2.25)
    print("\nUpdated opponents board: ")
    opponent_board()
    if (
        carrier_sunken_comp
        and battleship_sunken_comp
        and cruiser_sunken_comp
        and submarine_suken_comp
        and destroyer_sunken_comp
    ):
        t.sleep(1.5)
        break
    t.sleep(2.15)
    clear()
    # ______ Computer's turn ______
    print("Computers turn!")
    attack_cords_comp = r.choice(cells)
    cells.remove(attack_cords_comp)
    index_of_attack_comp = get_index(attack_cords_comp)
    if plr_board[index_of_attack_comp].strip() != "_":
        plr_board.pop(index_of_attack_comp)
        plr_board.insert(index_of_attack_comp, "  X")
        print(Style.RESET_ALL)
        print(Fore.RED + "The computer hit a ship at " + attack_cords_comp + "!")
        print(Style.RESET_ALL)
        update_board()
    else:
        print(Style.RESET_ALL)
        print(Fore.RED + "The computer missed at " + attack_cords_comp)
        print(Style.RESET_ALL)
    t.sleep(2.25)
    if (
        carrier_sunken_comp
        and battleship_sunken_comp
        and cruiser_sunken_comp
        and submarine_suken_comp
        and destroyer_sunken_comp
    ):
        break

clear()
if (
    carrier_sunken
    and battleship_sunken
    and cruiser_sunken
    and submarine_suken
    and destroyer_sunken
):
    print("Game over!")
    print("The winner is...")
    t.sleep(3)
    print("The computer!")
elif (
    carrier_sunken_comp
    and battleship_sunken_comp
    and cruiser_sunken_comp
    and submarine_suken_comp
    and destroyer_sunken_comp
):
    print("Game over!")
    print("The winner is...")
    t.sleep(3)
    print("The player!")

print("Thanks for playing!")
