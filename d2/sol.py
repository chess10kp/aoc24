output = ""

with open("input.txt") as file:
    output = file.readlines()

successful_reports = 0 
for report in (output):
    levels = list(map(int, report.split()))
    is_increasing = None
    current, prev = None, None
    failed = False
    prev, current = 0, 0
    for i in range(1, len(levels)):
        current = i

        if is_increasing is None:
            is_increasing = levels[prev] > levels[current]

        if ( levels[prev] > levels[current]) != is_increasing or levels[prev] == levels[current] :
            failed = True
            break

        if  abs(levels[prev] - levels[current])  > 3:
            failed = True
            break

        prev = current

    if not failed:
        successful_reports += 1
