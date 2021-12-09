def loadData(filename):
	lines = None
	with open(filename, "r") as f:
		lines = [l for l in f.read().split("\n") if l]
	data = [[[y for y in p.strip().split(" ") if y] for p in l.split("|") if p] for l in lines if l]
	return data

testdata = loadData("testinput.txt")
inputdata = loadData("input.txt")

def part1(data):
	sumofunique = sum(len(x) in [2, 4, 3, 7] for p in data for x in p[1])
	print(sumofunique)

def part2(data):
	print(":(")

# part1(testdata)
# part1(inputdata)
part2(testdata)
# part2(inputdata)
