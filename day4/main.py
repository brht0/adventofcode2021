with open("input.txt", "r") as f:
	strtables = [str(s) for s in f.read().split("\n\n") if s]
	order = [int(x) for x in strtables[0].split(",") if x]
	tables = [[[int(p) for p in l.split(" ") if p] for l in t.split("\n") if l] for t in strtables[1:]]

# order = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# tables = [[[int(z) for z in y.split(" ") if z] for y in ''.join(x).split("\n") if y] for x in ''.join([
# "22 13 17 11  0\n",
#  "8  2 23  4 24\n",
# "21  9 14 16  7\n",
#  "6 10  3 18  5\n",
#  "1 12 20 15 19\n",
# "\n",
#  "3 15  0  2 22\n",
#  "9 18 13 17  5\n",
# "19  8  7 25 23\n",
# "20 11 10 24  4\n",
# "14 21 16 12  6\n",
# "\n",
# "14 21 17 24  4\n",
# "10 16 15  9 19\n",
# "18  8 23 26 20\n",
# "22 11 13  6  5\n",
#  "2  0 12  3  7\n",
# ]).split("\n\n")]

# for t in tables:
# 	print(t)

def part1():
	def isSudoku(t):
		# digleft = True
		# digright = True
		for i in range(5):
			hor = True
			ver = True
			for j in range(5):
				if(t[j][i] != " "):
					hor = False
				if(t[i][j] != " "):
					ver = False
			if hor or ver:
				return True
			# if t[i][i] != " ":
			# 	digleft = False
			# if t[i][4-i] != " ":
			# 	digright = False
		# if digleft or digright:
		# 	return True

	s = None
	try:
		for o in order:
			for t in tables:
				for x in range(5):
					for y in range(5):
						if t[y][x] == o:
							t[y][x] = " "
				# print("\ntable:")
				# for l in t:
				# 	print(l)
				if isSudoku(t):
					s = o * sum(t[y][x] for x in range(5) for y in range(5) if t[y][x] != " ")
					raise ("ok")
	except:
		print(s)


def part2():
	def isSudoku(t):
		for i in range(5):
			hor = True
			ver = True
			for j in range(5):
				if(t[j][i] != " "):
					hor = False
				if(t[i][j] != " "):
					ver = False
			if hor or ver:
				return True

	s = None
	prevWinTable = None
	prevLastBingoNum = None
	for o in order:
		for i, t in enumerate(tables):
			if not t:
				continue
			for x in range(5):
				for y in range(5):
					if t[y][x] == o:
						t[y][x] = " "
			if isSudoku(t):
				prevWinTable = t.copy()
				prevLastBingoNum = o
				tables[i] = None
				print(prevWinTable)
	s = prevLastBingoNum * sum(prevWinTable[y][x] for x in range(5) for y in range(5) if prevWinTable[y][x] != " ")
	print(s)

#part1()
part2()