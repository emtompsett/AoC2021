
def getNums(lines):
    curr = lines[0].split(",")
    nums = []
    for num in curr:
        nums.append(int(num))
    return nums

def getBoards(lines):
    boardsInit = lines[1:]
    boards = []
    for i in range(0,len(boardsInit), 25):
        board = []
        for j in range(0, 25, 5):
            row = []
            for k in range(5):
                row.append(int(boardsInit[i+j+k]))
            board.append(row)
        boards.append(board)
    return boards

def printBoards(boards):
    for board in boards:
        for row in board:
            print(row)
        print()


def winRow(row):
    for elt in row:
        if elt != 'X':
            return False
    return True

def winCol(board, col):
    for i in range(len(board)):
        if board[i][col] != 'X':
            return False
    return True

def win(board):
    win = False
    for row in board:
        win = win or winRow(row)
    for i in range(len(board[0])):
        win = win or winCol(board, i)
    return win

def callNum(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                board[i][j] = 'X';
    return board


def part1(lines):
    nums = getNums(lines)
    boards = getBoards(lines)
    winner = -1
    currNum = 0

    while winner == -1 and currNum < len(nums):
        for i in range(len(boards)):
            boards[i] = callNum(boards[i], nums[currNum]);
        for i in range(len(boards)):
            if win(boards[i]):
                winner = i
        currNum += 1
    sum = 0
    for i in range(len(boards[winner])):
        for j in range(len(boards[winner][i])):
            if boards[winner][i][j] != 'X':
                sum += boards[winner][i][j]
    print(sum, nums[currNum-1])
    print(sum * nums[currNum-1])

def part2(lines):
    nums = getNums(lines)
    boards = getBoards(lines)
    winner = -1
    currNum = 0
    winNum = 0
    wonBoards = []
    winPos = []
    while currNum < len(nums):
        for i in range(len(boards)):
            if i not in wonBoards:
                boards[i] = callNum(boards[i], nums[currNum]);
        for i in range(len(boards)):
            if win(boards[i]):
                print(wonBoards)
                if i not in wonBoards:
                    wonBoards.append(i)
                    winPos.append(currNum)
        currNum += 1
    sum = 0
    winner = wonBoards[-1]
    winNum = nums[winPos[-1]]
    print(winner, boards[winner])
    for i in range(len(boards[winner])):
        for j in range(len(boards[winner][i])):
            if boards[winner][i][j] != 'X':
                sum += boards[winner][i][j]
    print(sum, winNum)
    print(sum * winNum)






def main():
    file = open("day4input.txt", "r");
    lines = file.read().strip().split();
    callNums = lines[0].split(",")
    boards = lines[1:]
    #part2(lines)

main();