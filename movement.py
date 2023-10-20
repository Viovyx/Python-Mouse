from setup import *


def log_movement(state, direction):
    if state == 1:
        print(f"SUCCESS: mice move {direction.upper()} | pos: {mouse}")
    elif state == 0:
        print(f"FAILURE: mice move {direction.upper()} | pos: {mouse}")


def check_for_wall(x, y):
    if maze[y][x] == 0:
        return 'open'
    else:
        return 'wall'


def move(direction):
    current_x = mouse[0]
    current_y = mouse[1]

    if direction == 'right':
        new_x = current_x + 1

        if check_for_wall(new_x, current_y) == 'open':
            mouse[0] = new_x
            log_movement(1, direction)

        elif check_for_wall(new_x, current_y) == 'wall':
            log_movement(0, direction)

    elif direction == 'left':
        new_x = current_x - 1

        if check_for_wall(new_x, current_y) == 'open':
            mouse[0] = new_x
            log_movement(1, direction)

        elif check_for_wall(new_x, current_y) == 'wall':
            log_movement(0, direction)

    elif direction == 'up':
        new_y = current_y - 1

        if check_for_wall(current_x, new_y) == 'open':
            mouse[1] = new_y
            log_movement(1, direction)

        elif check_for_wall(current_x, new_y) == 'wall':
            log_movement(0, direction)

    elif direction == 'down':
        new_y = current_y + 1

        if check_for_wall(current_x, new_y) == 'open':
            mouse[1] = new_y
            log_movement(1, direction)

        elif check_for_wall(current_x, new_y) == 'wall':
            log_movement(0, direction)


def reset_pos(start_pos):
    mouse[0] = start_pos[0]
    mouse[1] = start_pos[1]
