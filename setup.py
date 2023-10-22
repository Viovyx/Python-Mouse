#        0  1  2  3  4  5  6  7  8  9  10
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

start = [1, 1]
finish = [5, 5]
mouse = []
mouse += start


def print_maze(mouse_, finish_):
    row = 0
    print_row = ""

    print()
    for i in range(0, len(maze)):
        for j in range(0, len(maze[row])):
            if (row == mouse_[1]) and (j == mouse_[0]):
                print_row += 'M  '
            elif (row == finish_[1]) and (j == finish_[0]):
                print_row += 'F  '
            else:
                print_row += f'{maze[row][j]}  '

        print(print_row)
        row += 1
        print_row = ""
    print()


def init():
    print("==========================")
    print("       Python Mouse\n  (1 = wall | 0 = open)\n (M = mouse | F = finish)")
    print("==========================")
    print_maze(mouse, finish)
