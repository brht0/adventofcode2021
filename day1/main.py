with open("input.txt", "r") as f:
	strinput = f.read()
nums = [int(n) for n in strinput.split()]

#part 1
cnt = sum(nums[i] > nums[i-1] for i in range(1, len(nums)))
print(cnt)

#part 2
cnt = sum(sum(nums[i+j] for j in range(3)) > sum(nums[i+j-1] for j in range(3)) for i in range(1, len(nums)-2))
print(cnt)
