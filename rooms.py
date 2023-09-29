import random
import os
import keyboard

# Create a function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Create a function to generate a grid
def build_grid(size):
    x_axis = list(range(0, size))
    y_axis = list(range(0, size))
    grid_list = []

    for x_point in x_axis:
        for y_point in y_axis:
            grid_point = (x_point, y_point)
            grid_list.append(grid_point)

    return grid_list

# Create a function to set the difficulty level and create the grid
def set_difficulty():
    easy = 5
    med = 10
    hard = 15
    grid = []
    level = ''
    while True:
        print("How difficult would you like this to be?")
        difficulty = input("Type EASY, MED, HARD >> ").upper()
        if difficulty == "EASY":
            grid = build_grid(easy)
            edge = easy
            break
        elif difficulty == "MED":
            grid = build_grid(med)
            edge = med
            break
        elif difficulty == "HARD":
            grid = build_grid(hard)
            edge = hard
            level = 'hard'
            break
        else:
            print("That is not a valid selection. Try again")

    return grid, edge, level

# Create a function to get the locations of the monster, door, and start
def get_locations(grid):
    locations_dict = {}
    while True:
        locations_dict['monster'] = random.choice(grid)
        locations_dict['door'] = random.choice(grid)
        locations_dict['start'] = random.choice(grid)
        if not (locations_dict['monster'] == locations_dict['door'] and locations_dict['monster'] == locations_dict['start'] and locations_dict['door'] == locations_dict['start']):
            break

    return locations_dict
# Create a function to generate random events
def gen_event():
    rand_num = random.randint(1, 20)  # Generate a random number between 1 and 20

    if rand_num == 1:
        player_choice = input("You find a chest. Open it? y/n >> ").upper()
        if player_choice == "Y":
            print("You got eaten by the chest.")
        elif player_choice == "N":
            print("You missed a big treasure.")
    elif rand_num == 2:
        print("You hit your head. Lose health.")
    elif rand_num == 3:
        print("You got tired. Lose energy.")
    elif rand_num == 4:
        print("You encounter a friendly animal.")
    elif rand_num == 5:
        print("You discover a hidden passage.")
    elif rand_num == 6:
        print("You find a healing potion. Use it? y/n >> ")
# Create a function to show game instructions
def show_help():
    print("\nTry to find the way out before the monster finds you.")
    print("You can move up(U), down(D), left(L), or right(R).")
    print("\nYou cannot move into any space you have already been in.")
    print("If you box yourself in or get eaten by the monster, you lose.")
    print("\nTo show these instructions again type HELP.  To end the game type QUIT.")

# Create a function to draw the map
def draw_map(edge, current_room, previous_moves, locations, level):
    row = edge - 1

    if current_room == locations['monster']:
        map_key = '@'
    elif current_room == locations['door']:
        map_key = '*'
    else:
        map_key = 'X'

    print('_.' * edge)
    while row >= 0:
        column = 0
        while column < edge:
            if (row, column) == current_room:
                if column == edge -1:
                    print('|{}|'.format(map_key))
                else:
                    print('|{}'.format(map_key), end='')
            elif (row, column) in previous_moves:
                if column == edge - 1:
                    print('|/|')
                else:
                    print('|/', end='')
            elif level == 'hard' and (row, column) == locations['monster']:
                if column == edge - 1:
                    print('|@|')
                else:
                    print('|@', end='')
            else:
                if column == edge -1:
                    print('|_|')
                else:
                    print('|_', end='')
            column += 1
        row -= 1 

    return

# Create a function to move the player through the grid
def move_player(current_room, direction):
    x_axis, y_axis = current_room

    if direction == 'U':
        x_axis += 1
    elif direction == 'D':
        x_axis -= 1
    elif direction == 'R':
        y_axis += 1
    else:
        y_axis -= 1

    next_room = x_axis, y_axis

    return next_room

# ... (the rest of your code remains the same)

# Define the directions list
directions = ['U', 'D', 'L', 'R']

# Start the game loop
if __name__ == "__main__":
    game_grid, boundary, difficulty = set_difficulty()
    starting_locations = get_locations(game_grid)
    show_help()
    current_room = starting_locations['start']
    players_moves = [current_room]
    draw_map(boundary, current_room, players_moves, starting_locations, difficulty)

    while True:
        event = keyboard.read_event()
        
        # Check if arrow key events were triggered
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "left":
                player_choice = "L"
            elif event.name == "right":
                player_choice = "R"
            elif event.name == "up":
                player_choice = "U"
            elif event.name == "down":
                player_choice = "D"
            else:
                continue  # Skip other key events
            clear_screen()

            if player_choice == 'HELP':
                show_help()
                draw_map(boundary, current_room, players_moves, starting_locations, difficulty)
            elif player_choice == 'QUIT':
                break
            elif player_choice not in directions:
                print('\n>> That is not a recognized selection. <<')
                show_help()
                draw_map(boundary, current_room, players_moves, starting_locations, difficulty)
            else:
                new_room = move_player(current_room, player_choice)
                if new_room in players_moves:
                    print("Sorry. You've already been to that room. Try again")
                elif new_room == starting_locations['monster']:
                    print("Oh bad luck. You wandered into a room and found the monster waiting")
                    print("You die screaming while the monster eats you alive (>-<)")
                    print("\nThanks for playing. Better luck in your next incarnation")
                    break
                elif new_room == starting_locations['door']:
                    print("Congratulations! You found the way out")
                    print("The monster, still trapped in the dungeon, dies of starvation")
                    print("\nThanks for playing. Maybe you'll give another monster a chance at a good meal")
                    break
                else:
                    print("Current Room.")
                    gen_event()
                    players_moves.append(new_room)
                    current_room = new_room
                draw_map(boundary, current_room, players_moves, starting_locations, difficulty)
