from collections import defaultdict

output = None
with open("input.txt") as file:
    output = file.read().strip().splitlines()


class Map:
    def __init__(self):
        self._map: dict[int, list[int]] = defaultdict(list)

    def add_to_map(self, num: int, smaller: int):
        self._map[num].append(smaller)

    def is_child_of(self, num: int, child: int):
        return child in self._map[num]


m = Map()

to_break = False
i = 0


while True:
    rules = output[i].split("|")
    if len(rules) < 2:
        i += 1
        break
    m.add_to_map(int(rules[0]), int(rules[1]))
    i += 1


# # checking loop part 1
# s = 0
# new_sum = 0
# while i < len(output):
#     ordering = output[i].split(",")
#     failed = False
#     for j in range(1, len(ordering)):
#         for k in range(0, j):
#             if m.is_smaller(int(ordering[j]), int(ordering[k])):
#                 failed = True
#                 j = len(ordering)
#                 break
#     if failed:
#         i -= 1
#     else:
#         print(ordering, int(ordering[(len(ordering) - 1) // 2]))
#         s += int(ordering[((len(ordering) -1) // 2 )])
#     i += 1

# checking loop part 2

s = 0
new_sum = 0
good_rows = 0
bad_rows: list[list[int]] = []
while i < len(output):
    ordering = list(map(int, output[i].split(",")))
    leng = len(ordering)
    failed = False
    for j in range(leng):
        for k in range(j + 1, leng):
            if m.is_child_of(ordering[k], ordering[j]):
                failed = True
                break

    if failed:
        bad_rows.append(ordering)
        failed = False

    else:
        good_rows += 1

    i += 1


bad_rows = [list(row) for row in set(tuple(row) for row in bad_rows)]

sum = 0

print(len(bad_rows))


bad_row_sum = 0
for ordering in bad_rows:
    resolved = False
    while not resolved:
        resolved = True
        for j in range(len(ordering)):
            for k in range(j + 1, len(ordering)):
                if m.is_child_of(ordering[k], ordering[j]):
                    ordering[j], ordering[k] = ordering[k], ordering[j]
                    resolved = False

    bad_row_sum += ordering[len(ordering) // 2]

print(bad_row_sum)
