def LoadInput(filename):
    with open(filename, "r") as f:
        lines = [x for x in f.read().split("\n") if x]
    a = lines[0]
    b = lines[2:]
    return a, b

algorithm, map = LoadInput("testinput.txt")
# algorithm, map = LoadInput("input.txt")

print(algorithm)
print()
print()
print(map)
