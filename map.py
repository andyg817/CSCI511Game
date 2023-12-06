import random
import os
import keyboard
import time
import subprocess
import psutil
import threading


def measure_performance_before(duration_seconds):
    cpu_percentages = []
    memory_percentages = []

    end_time = time.time() + duration_seconds

    while time.time() < end_time:
        # Get CPU usage
        cpu_percentages.append(psutil.cpu_percent(interval=1))

        # Get memory usage
        memory_percentages.append(psutil.virtual_memory().percent)

    # Calculate average CPU and memory usage
    average_cpu = sum(cpu_percentages) / len(cpu_percentages)
    average_memory = sum(memory_percentages) / len(memory_percentages)

    return average_cpu, average_memory

def measure_performance(duration_seconds, result):
    cpu_percentages = []
    memory_percentages = []

    end_time = time.time() + duration_seconds

    while time.time() < end_time:
        # Get CPU usage
        cpu_percentages.append(psutil.cpu_percent(interval=1))

        # Get memory usage
        memory_percentages.append(psutil.virtual_memory().percent)

    # Calculate average CPU and memory usage
    average_cpu = sum(cpu_percentages) / len(cpu_percentages)
    average_memory = sum(memory_percentages) / len(memory_percentages)

    result['average_cpu'] = average_cpu
    result['average_memory'] = average_memory

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
    row = 4
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
print(f"Measuring performance for {10} seconds...")
average_cpu, average_memory = measure_performance_before(10)

initial_cpu = f"Initial Average CPU Usage: {average_cpu:.2f}%"
initial_mem = f"Initial Average Memory Usage: {average_memory:.2f}%"
# Start the game loop
if __name__ == "__main__":

    grid = []
    level = ''
    grid = build_grid(10)
    edge = 10

    game_grid, boundary, difficulty = grid, edge, level
    starting_locations = get_locations(game_grid)
    show_help()
    current_room = starting_locations['start']
    players_moves = [current_room]
    draw_map(boundary, current_room, players_moves, starting_locations, difficulty)

    # Initialize the result dictionary
    performance_result = {'average_cpu': 0, 'average_memory': 0}

    # Start measuring performance in a separate thread
    performance_thread = threading.Thread(target=measure_performance, args=(10, performance_result))
    performance_thread.start()

    end = True
    while end == True:
        data = ""

        #checking file
        with open('communication.txt', 'r') as file:
            data = file.read()

            #locking the file
            if data:
                with open('communication.txt', 'w') as lock_file:
                    lock_file.write("locked")

        #Critical section

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
            elif data == "f":
                end = False
                break
            else:
                continue  # Skip other key events
            clear_screen()

            new_room = move_player(current_room, player_choice)
            print("Current Room.")
            players_moves.append(new_room)
            current_room = new_room
            draw_map(boundary, current_room, players_moves, starting_locations, difficulty)

            #release lock
            with open('communication.txt', 'w') as file:
                pass

    performance_thread.join()
    # Access the performance results
    print(initial_cpu)
    print(initial_mem)
    print(f"Final Average CPU Usage: {performance_result['average_cpu']:.2f}%")
    print(f"Final Average Memory Usage: {performance_result['average_memory']:.2f}%")

