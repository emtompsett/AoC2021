

def part1(lines):
    incCount = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            incCount += 1
    print(incCount)
    return incCount

def part2(lines):
    incCount = 0
    prevWindow = int(lines[0]) + int(lines[1]) + int(lines[2])
    currWindow = 0
    for i in range(1, len(lines)-2):
        currWindow = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        if prevWindow < currWindow:
            incCount += 1
        prevWindow = currWindow
    return incCount


def main():
    file = open("day1input.txt", "r");
    lines = file.read().strip().split();
    print(lines)
    print(part1(lines))

main()











#file = open("day1input.txt", "r")
#lines = file.read().strip().split()
#lines is a list of the input numbers






