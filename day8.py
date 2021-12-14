origDisp = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
origDispSize = []
for disp in origDisp:
    origDispSize.append(len(disp))
frequencies = {}
for letter in "abcdefg":
    count = 0
    for d in origDisp:
        if letter in d:
            count+=1
    frequencies[letter] = count




def decodeSimple(d):
    disp = d[0]
    decodedDisp = ["_"] * 10
    for d in disp:
        if len(d) == 2:
            decodedDisp[origDispSize.index(2)] = d
        if len(d) == 3:
            decodedDisp[origDispSize.index(3)] = d
        if len(d) == 7:
            decodedDisp[origDispSize.index(7)] = d
        if len(d) == 4:
            decodedDisp[origDispSize.index(4)] = d
    return decodedDisp


def count1478(d):
    count = 0
    decoded = decodeSimple(d)
    #print(decoded, end = " ")
    code = d[1]
    for c in code:
        if c in decoded:
            count += 1
    #print(count)
    return count

def part1(disp):
    count = 0
    i = 0
    for d in disp:
       # print(i, end = " ")
        count += count1478(d)
        i+=1
    print(count)

def part2(disp):
    count = 0
    for line in disp:
        #print("line: ", line)
        num = 0
        decoded = decodeEntirely(line[0])
        print(decoded)
        print(line[1])
        for c in line[1]:
            num = num * 10 + decoded.index(c)
       # print(num)
        count += num
    print(count)



def decodeEntirely(disp):
    decodedDisp = ["_"] * 10
    decodedLetters = ["?"] * 7
    dF = {}
    for letter in "abcdefg":
        count = 0
        for d in disp:
            if letter in d:
                count += 1
        dF[letter] = count
   # print(frequencies)
   # print(dF)
    #print(origDisp)

    for let in dF:
        if dF[let] == 4:
            decodedLetters[4] = let
        if dF[let] == 9:
            decodedLetters[5] = let
        if dF[let] == 6:
            decodedLetters[1] = let
        if dF[let] == 8:
            decodedLetters[0] += let
            decodedLetters[2] += let
        if dF[let] == 7:
            decodedLetters[3] += let
            decodedLetters[6] += let
    #print(decodedLetters)





    #print(disp)
    for d in disp:
        if len(d) == 2:
            decodedDisp[origDispSize.index(2)] = d
        if len(d) == 3:
            decodedDisp[origDispSize.index(3)] = d
        if len(d) == 7:
            decodedDisp[origDispSize.index(7)] = d
        if len(d) == 4:
            decodedDisp[origDispSize.index(4)] = d
        if len(d) == 6:
            if decodedLetters[4] not in d:
                decodedDisp[9] = d
        if len(d) == 5:
            if decodedLetters[5] not in d and decodedLetters[1] not in d:
                decodedDisp[2] = d
        if len(d) == 5:
            if decodedLetters[4] not in d and decodedLetters[1] not in d:
                decodedDisp[3] = d

   # finishing 1
    oneList = list(decodedDisp[1])
    oneList.remove(decodedLetters[5])
    decodedLetters[2] = oneList[0]
    aList = list(decodedLetters[0][1:])
    aList.remove(decodedLetters[2])
    decodedLetters[0] = aList[0]

    for d in disp:
        if len(d) == 6:
            if decodedLetters[2] not in d:
                decodedDisp[6] = d
        if len(d) == 5:
            if decodedLetters[2] not in d:
                decodedDisp[5] = d
    for d in disp:
        if d not in decodedDisp:
            decodedDisp[0] = d
   # for letter in "abcdefg":
      #  if decoded[]

   # print(list("abcdefg"))
   # print(decodedLetters)
   # print(decodedDisp)
    return decodedDisp



def main():
    file = open("day8input.txt", "r");
    lines = file.read().strip().split("\n");
    displays = []
    print(origDispSize)
    for line in lines:
        sp = line.split("|")
        disp = (sp[0].split(), sp[1].split())
        for i in range(len(disp[0])):
            lst = list(disp[0][i])
            lst.sort()
            disp[0][i] = ''.join(lst)
        for i in range(len(disp[1])):
            lst = list(disp[1][i])
            lst.sort()
            disp[1][i] = ''.join(lst)
        #print(disp)
        displays.append(disp)
        #print(disp)
    #print(lines)
    part2(displays)





main()