import movement, random


while True:
    manual = (input("Would you like to control the mice manual? (y/N): ") == 'y')

    if manual:
        print("MANUAL MODE: type 'stop' to stop\n")
        while True:
            direction = str(input("Choose a direction (right, left, up, down): "))
            if direction == 'stop':
                break
            while direction != ('right' or 'left' or 'up' or 'down'):
                print("FAILURE: invalid input\n")
                direction = input("Choose a direction (right, left, up, down): ")
            movement.move(direction)
            print()

    elif not manual:
        print("AUTO MODE: type 'stop' to stop\n")
        stop = ''
        while stop != 'stop':
            directions = ['right', 'left', 'up', 'down']
            random_directions = random.choice(directions)
            movement.move(random_directions)
            stop = input("Press ENTER to continue...\n")
