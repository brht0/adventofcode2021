# with open("inputdemo.txt", "r") as f:
with open("input.txt", "r") as f:
	lines = [l for l in f.read().split("\n")]
	lines = [[[int(p.strip()) for p in c.split(",")] for c in l.split("->")] for l in lines if l]
	# print(lines)

def part1():
	dct = {}
	counter = 0
	for l in lines:
		x1, y1 = l[0]
		x2, y2 = l[1]

		if x1 == x2:
			for y in range(min(y1, y2), max(y1, y2)+1):
				key = (x1, y)
				if key in dct:
					dct[key] += 1
					if dct[key] == 2:
						counter += 1
				else:
					dct[key] = 1
		elif y1 == y2:
			for x in range(min(x1, x2), max(x1, x2)+1):
				key = (x, y1)
				if key in dct:
					dct[key] += 1
					if dct[key] == 2:
						counter += 1
				else:
					dct[key] = 1
		else:
			pass
	print(counter)

def part2():
	dct = {}
	counter = 0
	for l in lines:
		x1, y1 = l[0]
		x2, y2 = l[1]

		if x1 == x2:
			for y in range(min(y1, y2), max(y1, y2)+1):
				key = (x1, y)
				if key in dct:
					dct[key] += 1
					if dct[key] == 2:
						counter += 1
				else:
					dct[key] = 1
		elif y1 == y2:
			for x in range(min(x1, x2), max(x1, x2)+1):
				key = (x, y1)
				if key in dct:
					dct[key] += 1
					if dct[key] == 2:
						counter += 1
				else:
					dct[key] = 1
		else:
			dx = x2 - x1
			dy = y2 - y1
			
			r = abs(dx) # == abs(dy)
			dx //= r
			dy //= r

			for i in range(r+1):
				x = x1 + dx * i
				y = y1 + dy * i
				
				key = (x, y)
				if key in dct:
					dct[key] += 1
					if dct[key] == 2:
						counter += 1
				else:
					dct[key] = 1

	print(counter)

# part1()
part2()