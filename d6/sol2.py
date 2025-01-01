
from pprint import pprint
from copy import deepcopy

import sys
sys.setrecursionlimit(10**6)

output = []
with open("input.txt") as file:
    output = file.readlines()

maze: list[list[str]] = list(
    map(lambda x: list(x[:-1] if x[-1] == "\n" else x), output)
)

old_maze = deepcopy(maze)

idx = 0
yidx = 0

for yidx, row in enumerate(maze):
    if "^" in row:
        idx = row.index("^")
        pprint((idx, yidx))
        maze[yidx][idx] = "X"
        break

print(idx, yidx)

obstructions = 0

moves = []

def traverse_maze(
    maze: list[list[str]], xidx: int, yidx: int, uniq: int, guard: str
) -> int:

    global obstructions
    if maze[yidx][xidx] == ".":
        moves.append((xidx, yidx))
        maze[yidx][xidx] = guard
        uniq += 1

    match guard:
        case "^":
            if yidx == 0:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx - 1][xidx][0] != "#":
                return traverse_maze(maze, xidx, yidx - 1, uniq, "^")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, ">")

        case ">":
            if xidx == len(maze[0]) - 1:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx][xidx + 1][0] != "#":
                return traverse_maze(maze, xidx + 1, yidx, uniq, ">")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, "v")

        case "<":
            if xidx == 0:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx][xidx - 1][0] != "#":
                return traverse_maze(maze, xidx - 1, yidx, uniq, "<")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, "^")

        case "v":
            if yidx == len(maze) - 1:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx + 1][xidx][0] != "#":
                return traverse_maze(maze, xidx, yidx + 1, uniq, "v")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, "<")

        case _:
            raise Exception()


pprint(traverse_maze(maze, idx, yidx, 1, "^"))
moves = list(set(moves))

def check_loop(
    maze: list[list[list[str]]], xidx: int, yidx: int, uniq: int, guard: str
) -> int | bool:

    if  guard in maze[yidx][xidx]:
        print(guard, xidx, yidx , maze[yidx][xidx])
        return True

    if maze[yidx][xidx][0] == ".":
        maze[yidx][xidx][0] = guard
        uniq += 1

    elif maze[yidx][xidx][0] != "#":
        maze[yidx][xidx].append(guard)

    match guard:
        case "^":
            if yidx == 0:
                return False

            elif maze[yidx - 1][xidx][0] != "#":
                return check_loop(maze, xidx, yidx - 1, uniq, "^")

            else:
                return check_loop(maze, xidx, yidx, uniq, ">")

        case ">":
            if xidx == len(maze[0]) - 1:
                return False

            elif maze[yidx][xidx + 1][0] != "#":
                return check_loop(maze, xidx + 1, yidx, uniq, ">")

            else:
                return check_loop(maze, xidx, yidx, uniq, "v")

        case "<":
            if xidx == 0:
                return False

            elif maze[yidx][xidx - 1][0] != "#":
                return check_loop(maze, xidx - 1, yidx, uniq, "<")

            else:
                return check_loop(maze, xidx, yidx, uniq, "^")

        case "v":
            if yidx == len(maze) - 1:
                return False

            elif maze[yidx + 1][xidx][0] != "#":
                return check_loop(maze, xidx, yidx + 1, uniq, "v")

            else:
                return check_loop(maze, xidx, yidx, uniq, "<")

        case _:
            raise Exception()


print("\n".join(["".join([str(col) for col in row]) for row in old_maze]))

old_new_maze = [[[old_maze[j][i]] for i in range(len(old_maze[j]))] for j in range(len(old_maze))]

for move in moves:
    new_maze = deepcopy(old_new_maze)
    new_maze[move[0]][move[1]][0] = "#"
    new_maze[yidx][idx][0] = "X"
    is_loop = check_loop(new_maze, idx, yidx, 1, "^")
    if is_loop:
        obstructions += 1

print(obstructions)
