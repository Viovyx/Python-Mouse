import random
import setup

from movement import *

setup.print_maze()


def main():
    manual = (input("\nWould you like to control the mice manual? (y/N): ") == 'y')

    if manual:
        print("MANUAL MODE: type 'stop' to stop\n")

        while True:
            direction = input("Choose a direction (right, left, up, down): ")

            while direction not in ['right', 'left', 'up', 'down']:
                if direction == 'stop':
                    reset_pos(start)
                    print("POSITION RESET")
                    main()

                print("FAILURE: invalid input\n")
                direction = input("Choose a direction (right, left, up, down): ")

            move(direction)
            print()

    elif not manual:
        print("SEMI AUTO MODE: type 'stop' to stop\n")
        stop = ''

        while stop != 'stop':
            directions = ['right', 'left', 'up', 'down']
            random_directions = random.choice(directions)
            move(random_directions)
            stop = input("Press ENTER to continue...\n")

        reset_pos(start)
        print("POSITION RESET")

    main()


if __name__ == '__main__':
    main()
