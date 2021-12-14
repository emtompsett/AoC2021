import copy
def oneStep(curr, pairs):
    newCurr = []
    newCurr.append(curr[0])
    for i in range(0, len(curr)-1):
        seq = curr[i] + curr[i+1]
        #print(seq)
        if seq in pairs:
            #if pairs[seq] == "B":
                #print("adding a B:", curr[i]+ curr[i+1])
            newCurr.append(pairs[seq])
            newCurr.append(curr[i+1])
            #print(newCurr)
    #print(newCurr)
    return newCurr
def part1(pTemp, pairs):
    for i in range(5):
        print('************', i )
        pTemp = oneStep(pTemp, pairs)
        #print(str(pTemp))
    print('___________________', len(pTemp))
    #counts = {}
    ''' 
    for i in range(len(pTemp)):
        if pTemp[i] in counts:
            counts[pTemp[i]] += 1
        else:
            counts[pTemp[i]] = 1


    min1 = 10000000000
    mkey1 = ""
    for key in counts:
        if counts[key] < min1:
            min1 = counts[key]
            mkey1 = key


    max = 0
    mkey2 = ""
    for key in counts:
        if counts[key] > max:
            max = counts[key]
            mkey2 = key
    '''


def part2Step(counts, pairs, singles):
    newCounts = copy.deepcopy(counts)

    for k in counts:
        newCounts[k] -= counts[k]
        newCounts[k[0] + pairs[k]] += counts[k]
        newCounts[pairs[k] + k[1]] += counts[k]
        singles[pairs[k]] += counts[k]

    return newCounts, singles


def part2Counts(curr, pairs):
    # setting up countPairs and singles dictionaries
    counts = {}
    for p in pairs:
        counts[p] = 0
    for i in range(0, len(curr)-1):
        counts[curr[i] + curr[i+1]] +=1

    singles = {}
    for i in range(len(curr)):
        if curr[i] in singles:
            singles[curr[i]] += 1
        else:
            singles[curr[i]] = 1

    #actually iterating and making the steps
    for i in range(40):
        counts,singles = part2Step(counts, pairs, singles)

    return singles




def part2(pTemp, pairs):
    counts = part2Counts(pTemp, pairs)

    #get min and max
    min1 = 100000000000000000000000000000
    mkey1 = ""
    for key in counts:
        if counts[key] < min1:
            min1 = counts[key]
            mkey1 = key

    max = 0
    mkey2 = ""
    for key in counts:
        if counts[key] > max:
            max = counts[key]
            mkey2 = key
    print(max, min)
    print(max - min1)


def main():
    file = open("day14input.txt", "r");
    lines = file.read().strip().split("\n");
    pTemp = list(lines[0])
    lines.pop(0)
    lines.pop(0)
    pairs = {}
    for l in lines:
        p = l.split("->")
        st = p[0].strip(" ")
        end = p[1].strip(" ")
        pairs[st] = end
    #part1(pTemp, pairs)
    part2(pTemp, pairs)
main()
