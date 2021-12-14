


def part1(lines):
    print(lines)
    positions = max(lines)
    fuels = []
    for pos in range(positions):
        sum = 0
        for line in lines:
            sum += abs(line - pos)
        fuels.append(sum)
    print(min(fuels))
    print(fuels.index(min(fuels)))

def sumInts(max):
    return max * (max+1)/2

def part2(lines):
    print(lines)
    positions = max(lines)
    fuels = []
    for pos in range(positions):
        sum = 0
        for line in lines:
            sum += sumInts(abs(line - pos))
        fuels.append(sum)
    print(int(min(fuels)))
    print(fuels.index(min(fuels)))








def main():
    file = open("day7input.txt", "r");
    lines = file.read().strip().split(",");
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    part2(lines)
main()