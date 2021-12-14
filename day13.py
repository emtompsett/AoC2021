def makeGrid(lines, rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(".")
        grid.append(row)

    #print(grid)
    for pos in lines:
        r, c = pos
        grid[r][c] = "#"
    #for g in grid:
        #print(g)
    return grid


def foldGrid(grid, dir, dist):
    #print(grid,dir, dist)
    if dir == "y": #fold horizontal
        y = int(dist)
        #print(y)
        for i in range(len(grid)-1, y, -1):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    grid[2*y-i][j] = "#"


        for i in range(len(grid) - 1, y - 1, -1):
            grid.pop(i)



    elif dir == "x":
        x = dist
        for j in range(len(grid[0])-1, x, -1):
            for i in range(len(grid)):
                if grid[i][j] == "#":
                    grid[i][2*x-j] = "#"
        for i in range(len(grid)):
            grid[i] = grid[i][:x]

    return grid




def part1(lines, fold):
    moves = []
    m = fold
    #for m in fold:
    f = m.split(" ")[-1]
    #print(f)
    dir = f[0]
    dist = f[2:]
        #moves.append((dir, dist))

    maxRow = 0
    maxCol = 0
    for l in lines:
        if l[0] > maxRow:
            maxRow = l[0]
        if l[1] > maxCol:
            maxCol = l[1]


    print("MAXES: ",maxRow, maxCol)
    grid = makeGrid(lines, maxRow+1, maxCol+1)
    #print(dir, ":", int(dist))
    #for move in moves:
    grid = foldGrid(grid, dir, int(dist))
    for r in grid:
        print(r)
    count = 0

    for r in grid:
        for c in r:
            if c == "#":
                count += 1

    print(count)

def part2(lines, folds):
    moves = []

    for m in folds:
        #print(m)
        f = m.split(" ")[-1]
        #print(f)
        dir = f[0]
        dist = f[2:]
        moves.append((dir, dist))

    maxRow = 0
    maxCol = 0
    for l in lines:
        if l[0] > maxRow:
            maxRow = l[0]
        if l[1] > maxCol:
            maxCol = l[1]


    print("Maxes: ", maxRow, maxCol)
    grid = makeGrid(lines, maxRow+1, maxCol+1)
    #print(dir, ":", int(dist))
    for move in moves:
        print(move)
        grid = foldGrid(grid, move[0], int(move[1]))
        print(len(grid), len(grid[0]))

    for g in grid:
        for r in g:
            if r == "#":
                print("X", end = "")
            else:
                print(" ", end = "")
        print()
        #print(g)
    #print(grid)

def main():
    file = open("day13input.txt", "r");
    lines = file.read().strip().split("\n");
    moves =[]
    while lines[-1][0] == "f":
        moves.insert(0,lines[-1])
        lines.pop(-1)
    #print(moves)
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        #print(lines[i])
        col = int(lines[i][0])
        row = int(lines[i][1])
        lines[i] = (row, col)
    #print(lines)
    part2(lines, moves)
main()