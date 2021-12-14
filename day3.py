import copy
def part1(lines):
    gamma = []
    eps = []
    ones = 0
    zeros = 0
    for pos in range(len(str(lines[0]))):
        ones = 0
        zeros = 0
        for row in range(len(lines)):
           # print(row, pos)
            if lines[row][pos] == "0":
                zeros += 1
            else:
                ones += 1

       # print("Zeros: ", zeros, "ones:", ones)
        if ones > zeros:
            gamma.append(1)
            eps.append(0)
        elif ones == zeros:
           # print("EQUAL")
            gamma.append(1)
            eps.append(0)
        else:
            gamma.append(0)
            eps.append(1)
    return gamma,eps

def toDec(binList):
    num = 0
    exp = 0
    for i in range(len(binList)-1, -1, -1):
        num = num + int(binList[i]) * (2 ** exp)
        exp += 1
    return num



def oxGen(lines):
    oxGen = copy.deepcopy(lines)
    mostCom, leastCom = part1(lines)
    #print(mostCom)
    #ooxGen first - remove ones that aren't least common
    for bit in range(len(oxGen[0])):
        mostCom, leastCom = part1(oxGen)
        #print(bit, mostCom[bit], oxGen)
        i = 0

        while i < len(oxGen):
            #print(i, "OxGen:", oxGen, "removing starting with", mostCom[bit])
            if int(mostCom[bit]) != int(oxGen[i][bit]):
                #print("removing", oxGen[i])
                oxGen.pop(i)
            else:
                i+=1
            if len(oxGen) == 1:
                return oxGen



def co2(lines):
    co2Scrub = copy.deepcopy(lines)
    for bit in range(len(co2Scrub[0])):
        mostCom, leastCom = part1(co2Scrub)
        #print(bit, mostCom[bit], oxGen)
        i = 0

        while i < len(co2Scrub):
            #print(i, "OxGen:", oxGen, "removing starting with", mostCom[bit])
            if int(leastCom[bit]) != int(co2Scrub[i][bit]):
                #print("removing", co2Scrub[i])
                co2Scrub.pop(i)
            else:
                i+=1
            if len(co2Scrub) == 1:
                return co2Scrub


def main():
    file = open("day3input.txt", "r");
    lines = file.read().strip().split();
    print(lines)
   #print(int(toDec(oxGen(lines)[0]) * int(toDec(co2(lines)[0]))))
main()