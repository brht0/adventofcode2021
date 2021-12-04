# inputnums = [
# 	"00100",
# 	"11110",
# 	"10110",
# 	"10111",
# 	"10101",
# 	"01111",
# 	"00111",
# 	"11100",
# 	"10000",
# 	"11001",
# 	"00010",
# 	"01010"
# ]

with open("input.txt", "r") as f:
	inputnums = [str(s) for s in f.read().split("\n") if s]


def bintodec(num: str):
	return sum(int(num[i]) << (len(num)-1-i) for i in range(len(num)))

# part 1
# transpose
# nums = inputnums
# nums = [''.join(n[i] for n in nums) for i in range(len(nums[0])) if nums[i]]
# # most common bit
# nums = [sum(int(x) for x in nums[i]) > len(nums[i])/2 for i in range(len(nums))]

# g = ''.join(str(int(x)) for x in nums)
# e = ''.join(str(1-int(x)) for x in nums)

# g = bintodec(g)
# e = bintodec(e)

# print((g, e), "product:", g*e)


#part 2
co2 = inputnums
oxy = inputnums

for i in range(len(oxy[0])):

	if len(oxy) > 1:
		oxy0 = sum(o[i] == "0" for o in oxy)
		oxy1 = sum(o[i] == "1" for o in oxy)
		filterBit = None
		if(oxy1 >= oxy0):
			filterBit = "1"
		else:
			filterBit = "0"
		oxy = [o for o in oxy if o[i] == filterBit]

	if len(co2) > 1:
		co20 = sum(c[i] == "0" for c in co2)
		co21 = sum(c[i] == "1" for c in co2)
		filterBit = None
		if(co20 <= co21):
			filterBit = "0"
		else:
			filterBit = "1"
		co2 = [c for c in co2 if c[i] == filterBit]
	

oxy = bintodec(oxy[0])
co2 = bintodec(co2[0])

print((oxy, co2), "product:", oxy*co2)
