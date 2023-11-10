import random
import os
import keyboard
import time
import subprocess

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

# Create a function to get the locations of the monster, door, and start
def get_locations(grid):
    locations_dict = {}
    locations_dict['start'] = (4,0)

    return locations_dict
def show_help():
    print("")
# Create a function to draw the map
def draw_map(edge, current_room, previous_moves, locations, level):
    row = edge - 1
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

# Define the directions list
directions = ['U', 'D', 'L', 'R']


time.sleep(1)
current_room = 0
# Start the game loop
if __name__ == "__main__":

    grid = []
    level = ''
    grid = build_grid(5)
    edge = 5

    game_grid, boundary, difficulty = grid, edge, level
    starting_locations = get_locations(game_grid)
    show_help()
    current_room = starting_locations['start']
    players_moves = [current_room]
    draw_map(boundary, current_room, players_moves, starting_locations, difficulty)

    while True:
        data = ""

        #communication
        with open('communication.txt', 'r') as file:
            data = file.read()

            if data:
                #print("Received: ", data)
                with open('communication.txt', 'w') as clear_file:
                    clear_file.write("paused")
        time.sleep(1)


        # Check if arrow key events were triggered
        if data:
            if data == "l":
                player_choice = "L"
            elif data == "r":
                player_choice = "R"
            elif data == "u":
                player_choice = "U"
            elif data == "d":
                player_choice = "D"
            else:
                continue  # Skip other key events
            clear_screen()

            new_room = move_player(current_room, player_choice)
            print("Current Room.")
            players_moves.append(new_room)
            current_room = new_room
            draw_map(boundary, current_room, players_moves, starting_locations, difficulty)
