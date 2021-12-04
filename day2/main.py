with open("input.txt", "r") as f:
	lines = f.read().split('\n')

# part 1
def tocoord(d, l):
	d = d[:1]
	if d == 'f':
		return (l, 0)
	elif d == 'd':
		return (0, l)
	elif d == 'u':
		return (0, -l)
	else:
		return (0, 0) # invalid input
x, y = (0, 0)
for line in lines:
	if not line:
		continue
	d, l = line.split(' ')
	c = tocoord(d, int(l))
	x, y = [x + c[0], y + c[1]]
print((x, y), "product: ", x * y)

# part 2
x, y, aim = (0, 0, 0)
for line in lines:
	if not line:
		continue
	d, l = line.split(' ')
	d = d[:1]
	l = int(l)

	if d == 'f':
		x += l
		y += aim * l
	elif d == 'd':
		aim += l
	elif d == 'u':
		aim -= l

print((x, y), "product:", x * y)
