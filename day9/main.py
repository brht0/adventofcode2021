from functools import reduce

def loadInput(filename):
    grid = None
    with open(filename, "r") as f:
        grid = [[int(c) for c in l] for l in f.read().split("\n") if l]
    return grid

testdata = loadInput("testinput.txt")
inputdata = loadInput("input.txt")

def isLowPoint(x, y, grid):
    if (x > 0 and grid[y][x-1] <= grid[y][x]) or \
       (y > 0 and grid[y-1][x] <= grid[y][x]) or \
       (x < len(grid[0])-1 and grid[y][x+1] <= grid[y][x]) or \
       (y < len(grid)-1 and grid[y+1][x] <= grid[y][x]):
        return False
    
    return True

def riskLevel(height):
    return height + 1

def part1(grid):
    risk = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if isLowPoint(x, y, grid):
                risk += riskLevel(grid[y][x])
    print(risk)

def getBasinSize(x, y, grid):
    size = 0
    floodHeads = [(x, y)]
    while floodHeads:
        newFloodHeads = []
        for xx, yy in floodHeads:
            if grid[yy][xx] in [-1, 9]:
                continue
            grid[yy][xx] = -1
            size += 1
            if xx > 0:              newFloodHeads += [(xx-1,    yy,)]
            if yy > 0:              newFloodHeads += [(xx,      yy-1,)]
            if xx < len(grid[0])-1: newFloodHeads += [(xx+1,    yy,)]
            if yy < len(grid)-1:    newFloodHeads += [(xx,      yy+1,)]

        floodHeads = newFloodHeads
    return size

def part2(grid):
    sizes = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 9 and grid[y][x] != -1:
                sizes += [getBasinSize(x, y, grid)]
    top3 = sorted(sizes, reverse=True)[:3]
    print(reduce(lambda x,y: x*y, top3))

# part1(inputdata)
part2(inputdata)
