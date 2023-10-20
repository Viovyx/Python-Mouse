import setup


def log_movement(state, direction):
    if state == 1:
        print(f"SUCCESS: mice move {direction.upper()} | pos: {setup.mice}")
    elif state == 0:
        print(f"FAILURE: mice move {direction.upper()} | pos: {setup.mice}")


def check_for_wall(x, y):
    if setup.maze[y][x] == 0:
        return 'free'
    else:
        return 'wall'


def move(direction):
    current_x = setup.mice[0]
    current_y = setup.mice[1]

    if direction == 'right':
        new_x = current_x + 1
        if check_for_wall(new_x, current_y) == 'free':
            setup.mice[0] = new_x
            log_movement(1, direction)
        elif check_for_wall(new_x, current_y) == 'wall':
            log_movement(0, direction)

    elif direction == 'left':
        new_x = current_x - 1
        if check_for_wall(new_x, current_y) == 'free':
            setup.mice[0] = new_x
            log_movement(1, direction)
        elif check_for_wall(new_x, current_y) == 'wall':
            log_movement(0, direction)

    elif direction == 'up':
        new_y = current_y - 1
        if check_for_wall(current_x, new_y) == 'free':
            setup.mice[1] = new_y
            log_movement(1, direction)
        elif check_for_wall(current_x, new_y) == 'wall':
            log_movement(0, direction)

    elif direction == 'down':
        new_y = current_y + 1
        if check_for_wall(current_x, new_y) == 'free':
            setup.mice[1] = new_y
            log_movement(1, direction)
        elif check_for_wall(current_x, new_y) == 'wall':
            log_movement(0, direction)
