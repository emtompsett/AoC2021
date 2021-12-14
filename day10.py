
def isValidStack(line):
    dictClose = {"]":"[", ")":"(", ">":"<", "}":"{"}
    dictOpen = {"[":"]", "(":")", "<":">", "{":"}"}
    stack = []

    for c in line:
        if c == "[" or c == "(" or c == "<" or c == "{":
            stack.append(c)
        elif stack[-1] == dictClose[c]:
            stack.pop()
        else:
            return "Corrupted";
    if len(stack) != 0:
        return stack

def isValid(line):
    sqBr = 0
    parens = 0
    curly = 0
    angle = 0
    for ch in line:
        #print(angle)
        if ch == "[":
            sqBr += 1
        elif ch == "(":
            parens += 1
        elif ch == "{":
            curly += 1
        elif ch == "<":
            angle += 1
        elif ch == "]":
            sqBr -= 1
        elif ch == ")":
            parens -= 1
        elif ch == "}":
            curly -= 1
        elif ch == ">":
            angle -= 1
        if sqBr < 0 or parens < 0 or curly < 0 or angle < 0:
            #print(sqBr, parens, curly, angle)
            return "Corrupted"
    if sqBr == 0 and parens == 0 and curly == 0 and angle == 0:
        return "Complete & Uncorupted"
    return "Incomplete"

def part1(lines):
    score = 0
    scores = {")":3, "]":57, "}":1197, ">":25137}
    for i in range(len(lines)):
        ret = isValidStack(lines[i])
       # print(ret)
        if ret != "Incomplete":
            #print(ret[-1])
            score += scores[ret[-1]]

    print(score)

def part2(lines):
    allScores = []
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    for i in range(len(lines)):
        score = 0
        ret = isValidStack(lines[i])
        #print(i,ret)
        if ret != "Corrupted":
            for i in range(len(ret)-1, -1, -1):
                score = score * 5 + scores[ret[i]]
            allScores.append(score)
            #print(score)
    allScores.sort()
   # print(len(allScores)//2)
    print(allScores[len(allScores)//2])


def main():
    file = open("day10input.txt", "r");
    lines = file.read().strip().split("\n");
    part2(lines)
main()