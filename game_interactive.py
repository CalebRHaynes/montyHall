import random

def run_game():
    print("WELCOME TO LET'S MAKE A DEAL!")
    prizes = ["goat", "goat", "money"]
    random.shuffle(prizes)
    doors = ["1", "2", "3"]
    stage = dict(zip(doors, prizes))
    print('THERE ARE 3 DOORS. ONE HAS MONEY AND THE OTHERS HAVE A GOAT!')

    while True:
        door = input("Pick a Door (1, 2, or 3): ")
        if door in doors:
            break
        else:
            print('Invalid input. Please pick door 1, 2, or 3.')

    # Reveal a door without money (a goat)
    remaining_doors = [d for d in doors if stage[d] == "goat"]
    door_to_reveal = random.choice(remaining_doors)
    print(f"BEFORE YOU GO, DOOR {door_to_reveal} has a GOAT!")

    while True:
        switch = input('Would you like to SWITCH OR STAY?\nSWITCH (1) OR STAY (2): ')
        if switch in ['1', '2']:
            switch = int(switch)
            break
        else:
            print("Invalid input. Please pick 1 (SWITCH) or 2 (STAY).")

    if switch == 1:
        doors.remove(door_to_reveal)
        chosen_door = doors[0]
    else:
        chosen_door = door

    print(f"YOU CHOSE DOOR {chosen_door} AND GOT... {stage[chosen_door]}")

if __name__ == '__main__':
    run_game()
