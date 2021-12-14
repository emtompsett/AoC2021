def printGrid(grid):
    for row in grid:
        print(row)
    print()

def processPoints(lines):
    segments = []
    for i in range(0, len(lines), 3):
        start = lines[i].split(",")
        start[0] = int(start[0])
        start[1] = int(start[1])
        end = lines[i+2].split(",")
        end[0] = int(end[0])
        end[1] = int(end[1])
        if start[0] > end[0]:
            end, start = start, end
        elif start[1] > end[1]:
            end, start = start, end


        segments.append([start, end])
    return segments

def removeNonHorVer(segments):
    i = 0
    while i < len(segments):
        segment = segments[i]
        if segment[0][0] != segment[1][0] and segment[0][1] != segment[1][1]:
            segments.pop(i)
        else:
            i+=1
    return segments


def part1(segments, grid):
   # print(segments)
    segments = removeNonHorVer(segments)
    #print(segments)
    for seg in segments:
        startX = seg[0][0]
        startY = seg[0][1]
        endX = seg[1][0]
        endY = seg[1][1]
        #print(seg)
        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                grid[j][i] += 1
    # summing multiples
    count = 0
    for row in grid:
        for elt in row:
            if elt >= 2:
                count += 1
    print(count)


def part2(segments, grid):

    for seg in segments:
        startX = seg[0][0]
        startY = seg[0][1]
        endX = seg[1][0]
        endY = seg[1][1]
        #print(seg)
        if startX == endX or startY == endY:
            for i in range(startX, endX + 1):
                for j in range(startY, endY + 1):
                    grid[j][i] += 1
        # dealing with diagonal
        else:
            #print("Diagonal!!!", seg)
            xSlope = 1
            ySlope = 1
            if startX - endX > 0:
                xSlope = -1
            if startY - endY > 0:
                ySlope = -1

            for i in range(0, abs(endX - startX) + 1):
                #print(i, startY + i * ySlope, startX + i * xSlope)
                grid[startY + i * ySlope][startX + i * xSlope] += 1
            #printGrid(grid)
        # input()
    # summing multiples
    count = 0
    for row in grid:
        for elt in row:
            if elt >= 2:
                count += 1
    print(count)

def main():
    file = open("day5input.txt", "r");
    lines = file.read().strip().split();
    segments = processPoints(lines)
    grid = []
    for i in range(1001):
        row = []
        for j in range(1001):
            row.append(0)
        grid.append(row)
    #printGrid(grid)
    part2(segments, grid)





main()