output = ""

def valid(prev, current, increasing):
    difference = prev - current 
    return difference != 0 and abs(difference) < 4 and (difference >  0) == increasing


def is_list_valid(xs, increasing):
    for i in range(1, len(xs)):
        if not valid(xs[i - 1], xs[i], increasing):
            return False
    return True
    
with open("input.txt") as file:
    output = file.read().strip()

successful_reports = 0 

reports = [[int(x) for x in report.split(" ")] for report in output.split("\n")]

for report in reports:
    if is_list_valid(report, True) or is_list_valid(report, False):
            successful_reports += 1

    else:
        for i in range(len(report)):
            if is_list_valid(report[:i] + report[i + 1:], True) or is_list_valid(report[:i] + report[i + 1:], False):
                successful_reports += 1
                break
