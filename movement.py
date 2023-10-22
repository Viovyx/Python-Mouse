from setup import *


def log_movement(state, direction):
    if state == 1:
        print(f"SUCCESS: mice move {direction.upper()} | pos: {mouse}")
    elif state == 0:
        print(f"FAILURE: mice move {direction.upper()} | pos: {mouse}")


def check_tile(x, y):
    if (finish[0] == x) and (finish[1] == y):
        return 'finish'
    elif maze[y][x] == 0:
        return 'open'
    elif maze[y][x] == 1:
        return 'wall'
    else:
        return 'error'


def move(direction):
    current_x = mouse[0]
    current_y = mouse[1]

    if direction == 'right':
        new_x = current_x + 1

        if check_tile(new_x, current_y) == 'open':
            mouse[0] = new_x
            log_movement(1, direction)

        elif check_tile(new_x, current_y) == 'wall':
            log_movement(0, direction)

        elif check_tile(new_x, current_y) == 'finish':
            print("SUCCESS: finish reached!")
            exit()

        elif check_tile(new_x, current_y) == 'error':
            print("FAILURE: unknown tile")
            exit()

    elif direction == 'left':
        new_x = current_x - 1

        if check_tile(new_x, current_y) == 'open':
            mouse[0] = new_x
            log_movement(1, direction)

        elif check_tile(new_x, current_y) == 'wall':
            log_movement(0, direction)

        elif check_tile(new_x, current_y) == 'finish':
            print("SUCCESS: finish reached!\n")
            exit()

        elif check_tile(new_x, current_y) == 'error':
            print("FAILURE: unknown tile")
            exit()

    elif direction == 'up':
        new_y = current_y - 1

        if check_tile(current_x, new_y) == 'open':
            mouse[1] = new_y
            log_movement(1, direction)

        elif check_tile(current_x, new_y) == 'wall':
            log_movement(0, direction)

        elif check_tile(current_x, new_y) == 'finish':
            print("SUCCESS: finish reached!")
            exit()

        elif check_tile(current_x, new_y) == 'error':
            print("FAILURE: unknown tile")
            exit()

    elif direction == 'down':
        new_y = current_y + 1

        if check_tile(current_x, new_y) == 'open':
            mouse[1] = new_y
            log_movement(1, direction)

        elif check_tile(current_x, new_y) == 'wall':
            log_movement(0, direction)

        elif check_tile(current_x, new_y) == 'finish':
            print("SUCCESS: finish reached!")
            exit()

        elif check_tile(current_x, new_y) == 'error':
            print("FAILURE: unknown tile")
            exit()


def reset_pos(start_pos):
    mouse[0] = start_pos[0]
    mouse[1] = start_pos[1]
