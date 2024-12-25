output = None
with open("input.txt") as file:
    output = file.read().strip()
    output = output.split("\n")


keys: list[list[int]] = []
locks: list[list[int]] = []

line_idx = 0
while line_idx < len(output):
    if output[line_idx][0] == ".":
        # key
        pass
        heights = [0] * 5
        while output[line_idx] != "":
            for i in range(5):
                if output[line_idx][i] == "#":
                    heights[i] += 1
            line_idx += 1
            if line_idx >= len(output):
                break

        keys.append(heights)
        line_idx += 1

    elif output[line_idx][0] == "#":
        # lock
        heights = [0] * 5
        while output[line_idx] != "":
            for i in range(5):
                if output[line_idx][i] == "#":
                    heights[i] += 1
            line_idx += 1

        locks.append(heights)
        line_idx += 1

    else:
        raise Exception("Invalid input")


ret = 0 
for i in range(len(keys)):
    for j in range(len(locks)):
        for k in range(5):
            if keys[i][k] + locks[j][k] > 7:
                break
        else:
            ret += 1

print(ret)
