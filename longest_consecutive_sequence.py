def longestConsecutive(nums):
	if len(nums) == 0:
		return 0

	nums.sort()
	longest = 1
	last_longest = 1

	for i in range(1, len(nums)):
		print(longest)
		if nums[i] - nums[i - 1] == 1:
			longest += 1
		else:
			if nums[i] - nums[i - 1] != 0:
				last_longest = longest if longest > last_longest else last_longest
				longest = 1

	if longest < last_longest:
		longest = last_longest

	return longest



print(longestConsecutive([1,0,1,2]))