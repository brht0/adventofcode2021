# with open("inputdemo.txt", "r") as f:
with open("input.txt", "r") as f:
	lines = [l for l in f.read().split("\n") if l]
	pos = [int(x) for l in lines for x in l.split(",")]

def getCost(position):
	return sum(abs(positer - position) for positer in pos)

def part1():
	minsumpos = 0
	minsum = getCost(0)
	for testpos in range(1, 1000):
		ns = getCost(testpos)
		if ns < minsum:
			minsumpos = testpos
			minsum = ns
	print(minsumpos, minsum)

def sumfactorial(x):
	return x * (x+1) / 2

def getCost2(position):
	return sum(sumfactorial(abs(positer - position)) for positer in pos)

def part2():
	minsumpos = 0
	minsum = getCost2(0)
	for testpos in range(1, 1000):
		ns = getCost2(testpos)
		if ns < minsum:
			minsumpos = testpos
			minsum = ns
	print(minsumpos, minsum)

# part1()
part2()
