def LoadData(datafile):
    with open(datafile, "r") as f:
        lines = [l for l in f.readlines() if l]
    points = []
    folds = []
    for l in lines:
        if l[0] == "f":
            folds += [(l.split(" ")[2][0], int(l.split("=")[1]))]
        else:
            newpoint = [int(x) for x in l.strip().split(",") if x]
            if newpoint:
                points += [newpoint]
    return (points, folds)

def visualize(points, w, h):
    for y in range(h):
        line = ''.join(['█' if (x, y) in points else '.' for x in range(w)])
        print(line)

def fold(points, folds):
    for axis, position in folds:
        newpoints = []
        for (x, y) in points:
            if axis == 'x' and x > position:
                x = position - abs(position - x)
            if axis == 'y' and y > position:
                y = position - abs(position - y)
            if (x, y) not in newpoints:
                newpoints += [(x, y)]
        points = newpoints
    return points

def part1(data):
    points = fold(data[0], data[1][:1])
    return len(points)
    
def part2(data):
    points = fold(data[0], data[1])
    visualize(points, 50, 15)

if __name__ == '__main__':
    testdata = LoadData("testdata.txt")
    fulldata = LoadData("data.txt")

    result = part1(testdata)
    print(f"part1 test: {result}")
    result = part1(fulldata)
    print(f"part1 full: {result}")
    
    result = part2(testdata)
    print(f"part2 test: {result}")
    result = part2(fulldata)
    print(f"part2 full: {result}")
