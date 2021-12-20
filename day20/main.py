def LoadInput(filename):
    with open(filename, "r") as f:
        lines = [x for x in f.read().split("\n") if x]
    a = lines[0]
    b = lines[2:]
    return a, b

def expandMap(in_map):
    map = in_map.copy()
    w = len(map[0])+2
    map = [f'.{x}.' for x in map]
    map = ['.'*w] + map + ['.'*w]
    return map

def boolListToBinary(boolList):
    result = 0
    for x in boolList:
        result *= 2
        result += x
    return result

def findReplacement(pixels, algo):
    index = [p == '#' for p in pixels]
    index = boolListToBinary(index)
    # print(f"index: {index}")
    return algo[index]

def conv(x, y, map):
    boolList = list()
    for iy in range(y-1, y+2):
        for ix in range(x-1, x+2):
            boolList += [map[iy][ix]]
    return boolList

def disExpandMap(in_map):
    map = in_map.copy()
    map = map[1:-1]
    map = [x[1:-1] for x in map]
    return map

def part1(algo, map):
    for i in range(10):
        map = expandMap(map)

    for i in range(2):
        nmap = map.copy()
        for y in range(1, len(map)-2):
            nmap[y] = "."*2
            for x in range(1, len(map[0])-2):
                bl = conv(x, y, map)
                r = findReplacement(bl, algo)
                nmap[y] += r
            nmap[y] += "."*2
        map = nmap
        print(f"iter {i}:", "-"*20)
        for r in map:
            print(r)
    
    for i in range(3):
        map = disExpandMap(map)

    return sum(sum(y=="#" for y in x) for x in map)

# algorithm, map = LoadInput("testinput.txt")
algorithm, map = LoadInput("input.txt")

# print(map)
# print(expandMap(map))
print(f"part1: {part1(algorithm, map)}")
