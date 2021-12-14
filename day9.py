


def isLow(row, col, grid):
    elt = grid[row][col]
    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    rowPos = [up, down]
    colPos = [left, right]
    if up < 0:
        rowPos.remove(up);
    if  left < 0:
        colPos.remove(left);
    if down >= len(grid):
        rowPos.remove(down)
    if right >= len(grid[row]):
        colPos.remove(right)
    toRet = True
    for r in rowPos:
        toRet = toRet and elt < grid[r][col]
    for c in colPos:
        toRet = toRet and elt < grid[row][c]
    return toRet
def part1(lines):
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if isLow(i, j, lines):
                count += int(lines[i][j])+1
    print(count)

def getDirs(row, col, grid):
    up = row - 1
    down = row + 1
    left = col - 1
    right = col + 1

    rowPos = [-1, 1]
    colPos = [-1, 1]
    if up < 0:
        rowPos.remove(-1);
    if  left < 0:
        colPos.remove(-1);
    if down >= len(grid):
        rowPos.remove(1)
    if right >= len(grid[row]):
        colPos.remove(1)
    return rowPos, colPos

def getBasin(row, col, grid, positions):
    val = grid[row][col]
    #print(row,",", col, ":", val)
    rowPos, colPos = getDirs(row, col, grid)
    for r in rowPos:
        if val < grid[row + r][col] and grid[row+r][col] != '9':
            if [row+r, col] not in positions:
                positions.append([row+r, col])
                getBasin(row+r, col, grid, positions)
    for c in colPos:
        if val < grid[row][col+c] and grid[row][col+c] != '9':
            if [row,col+c] not in positions:
                positions.append([row, col+c])
                getBasin(row, col+c, grid, positions)
    #print(positions)
    return positions








def part2(lines):
    lowPos = []
    basins = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if isLow(i, j, lines):
                lowPos.append((i, j))
    for l in lowPos:
        basin = getBasin(l[0], l[1], lines,[[l[0],l[1]]])
        #print("FINAL BASIN: ", len(basin))
        basins.append(len(basin))

    print(basins)
    max1 = max(basins)
    basins.remove(max1)
    max2 = max(basins)
    basins.remove(max2)
    max3 = max(basins)
    print(max1 * max2 * max3)
    #print(lowPos)

def main():
    file = open("day9input.txt", "r");
    lines = file.read().strip().split();
    print(lines)
    part2(lines)


main()