
def part1(fish):
    for i in range(10):
        for k in range(len(fish)):
            fish[k] -= 1
        for j in range(len(fish)):
            if fish[j] == -1:
                fish.append(8)
                fish[j] = 6

        #print("day", i, fish)

    print(len(fish))

def part2(fish):
    counts = [0,0,0,0,0,0,0]
    newOnes = [0,0,0,0,0,0,0]
    for i in range(len(fish)):
        counts[fish[i]] += 1
    for i in range(256):
        pos = i % 7
        addPos = (pos + 2) % 7
        skip = newOnes[pos]
        #print("Pos curr: ", pos, "to skip:", skip)
        counts[addPos] += counts[pos] - skip
        #print("New ones:", counts[pos] - skip, "in pos**************", addPos)
        newOnes[addPos] = counts[pos]- skip
        #print(i, counts, newOnes)
        #input()
    print(sum(counts))

def main():
    file = open("day6input.txt", "r");
    lines = file.read().strip().split(",");
    fish = []
    for line in lines:
        fish.append(int(line))
    #part1(fish)
    part2(fish)
main()