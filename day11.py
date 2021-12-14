

def getAdj(row, col, grid):
    adj = [(row + 1, col), (row - 1, col),
          (row, col + 1), (row, col - 1),
          (row - 1, col - 1), (row + 1, col + 1),
          (row - 1, col + 1), (row + 1, col -1)]
    for i in range(len(adj) - 1, -1, -1):
        pos = adj[i]
        if pos[0] < 0 or pos[0] >= len(grid):
            adj.pop(i)
        elif pos[1] < 0 or pos[1] >= len(grid[0]):
            adj.pop(i)
    #print(adj)
    return adj

def printGrid(grid):
    for r in grid:
        print(r)

def inc(i,j, grid):#, positions):
    #print('**************', grid[i][j], end = "")
    grid[i][j] += 1
    if grid[i][j] <= 9:
        #print("JUST INC: ", grid[i][j])
        return grid
    if grid[i][j] == 10:
        #print(positions)
        #if (i,j) not in positions:
            #positions.append((i,j))

        adj = getAdj(i, j, grid)
        #print("greater than 9", adj)
        for pos in adj:
            r, c = pos
            grid = inc(r, c, grid)#, positions)
    return grid



def oneStep(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            ##printGrid(grid)
            grid = inc(i, j, grid)#,[])

    #reset
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9:
                grid[i][j] = 0
                #print("Flash:",i,j)
                count+=1
    return grid, count

def part1(grid):
    count = 0
    #i = 1
    for i in range(100):
        #print("Step#", i+1)
        grid, c = oneStep(grid)
        #printGrid(grid)
        count += c
        #input()
        i+=1
    print(count)

def part2(grid):
    def part1(grid):
        count = 0
        i = 1
        while (True):
            # print("Step#", i+1)
            grid, c = oneStep(grid)
            # printGrid(grid)
            count += c
            if c == len(grid) * len(grid[0]):
                print(i)
                break
            # input()
            i += 1
        print(count)


def main():
    file = open("day11input.txt", "r");
    lines = file.read().strip().split();
    grid = []
    for l in lines:
        row = []
        for c in l:
            row.append(int(c))
        grid.append(row);
    print(grid)
    part1(grid)
main()