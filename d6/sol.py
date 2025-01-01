from pprint import pprint

import sys
sys.setrecursionlimit(10**6)

output = []
with open("input.txt") as file:
    output = file.readlines()

maze: list[list[str]] = list(
    map(lambda x: list(x[:-1] if x[-1] == "\n" else x), output)
)

idx = 0
yidx = 0

for yidx, row in enumerate(maze):
    if "^" in row:
        idx = row.index("^")
        pprint((idx, yidx))
        maze[yidx][idx] = "X"
        break

print(idx, yidx)

def traverse_maze(
    maze: list[list[str]], xidx: int, yidx: int, uniq: int, guard: str
) -> int:
    if maze[yidx][xidx] == ".":
        maze[yidx][xidx] = guard
        uniq += 1
    match guard:
        case "^":
            if yidx == 0:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx - 1][xidx] != "#":
                return traverse_maze(maze, xidx, yidx - 1, uniq, "^")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, ">")

        case ">":
            if xidx == len(maze[0]) - 1:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx][xidx + 1] != "#":
                return traverse_maze(maze, xidx + 1, yidx, uniq, ">")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, "v")

        case "<":
            if xidx == 0:
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx][xidx - 1] != "#":
                return traverse_maze(maze, xidx - 1, yidx, uniq, "<")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, "^")

        case "v":
            if yidx == len(maze):
                print("\n".join(["".join([str(col) for col in row]) for row in maze]))
                return uniq

            elif maze[yidx + 1][xidx] != "#":
                return traverse_maze(maze, xidx, yidx + 1, uniq, "v")

            else:
                return traverse_maze(maze, xidx, yidx, uniq, "<")

        case _:
            raise Exception()


pprint(traverse_maze(maze, idx, yidx, 1, "^"))
