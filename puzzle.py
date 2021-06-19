import random
import time

def _range(x, y):
    if(x < 0 or y < 0 or x > 2 or y > 2):
        return False
    else:
        return True


dx = [0 , 0, -1, 1]
dy = [1, -1, 0, 0]
puzzle = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

for x in range(3):
    for y in range(3):
        print(puzzle[x][y], end=" ")
    print("\n")

temp = 0

run = True

while run:
    print("==============================\n")
    for x in range(3):
        for y in range(3):
            if puzzle[x][y] == 0:
                current_y = y
                current_x = x
                print("0", end=" ")
            elif puzzle[x][y] > 0:
                print(puzzle[x][y], end=" ")
        print("\n")

    time.sleep(3)
    move = random.randint(0, 3)

    print("pos=", current_x, current_y)

    nx = current_x + dx[move]
    ny = current_y + dy[move]


    if _range(nx, ny):
        if move == 0 and puzzle[nx][ny] > puzzle[current_x][current_y]:
            puzzle[nx][ny], puzzle[current_x][current_y] = puzzle[current_x][current_y],  puzzle[nx][ny]
        elif move == 1 and  puzzle[nx][ny] > puzzle[current_x][current_y]:
            puzzle[nx][ny], puzzle[current_x][current_y] = puzzle[current_x][current_y],  puzzle[nx][ny]
        elif move == 2 and puzzle[nx][ny] > puzzle[current_x][current_y]:
            puzzle[nx][ny], puzzle[current_x][current_y] = puzzle[current_x][current_y],  puzzle[nx][ny]
        elif move == 3 and puzzle[nx][ny] < puzzle[current_x][current_y]:
            puzzle[nx][ny], puzzle[current_x][current_y] = puzzle[current_x][current_y],  puzzle[nx][ny]

    print("==============================\n")

    for x in range(3):
        for y in range(3):
            print(puzzle[x][y], end=" ")
        print("\n")