
def part1(lines):
    depth = 0
    hPos = 0
    print(lines)
    for i in range(0,len(lines)-1,2):
        dir = lines[i]
        amt = int(lines[i+1])
        print(dir, amt)
        if dir == "up":
            depth -= amt
        elif dir == "down":
            depth += amt
        elif dir == "forward":
            hPos += amt
    return hPos * depth

def part2(lines):
    depth = 0
    hPos = 0
    aim = 0
    print(lines)
    for i in range(0,len(lines)-1,2):
        dir = lines[i]
        amt = int(lines[i+1])
        print(dir, amt)
        if dir == "up":
            aim -= amt
        elif dir == "down":
            aim += amt
        elif dir == "forward":
            hPos += amt
            depth += aim * amt
    return hPos * depth





def main():
    file = open("day2input.txt", "r");
    lines = file.read().strip().split();
    print(part2(lines))


main()