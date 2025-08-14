"""

dekho current item er age ba pore kono number visit kore felecho kina
age pore ja I visit korecho shobguloke ek koro
longest update koro


Example 1: 

[100, 4, 200, 1, 3, 2]

{
	100: [],
	4: [],
	200: [],
	1: []
	1: [2, 3, 4],
}

Example 2:
[0,3,7,2,5,8,4,6,0,1]

{
	0: [],
	3: [2, 3],
	7: [],
	2: [2, 3],
	5: [2, 3, 4, 5, 6],
	4: [2, 3, 4, 5, 6],
	6: [2, 3, 4, 5, 6, 7],
}

"""



def longestConsecutive(nums):
	if len(nums) == 0:
		return 0
		
	nums.sort()
	longest = 1
	last_longest = 1

	print(nums)

	for i in range(1, len(nums)):
		print(longest)
		if nums[i] - nums[i - 1] == 1:
			longest += 1
		else:
			if nums[i] - nums[i - 1] != 0:
				last_longest = longest if longest > last_longest else last_longest
				longest = 1

	print(last_longest)

	if longest < last_longest:
		longest = last_longest

	return longest



print(longestConsecutive([1,0,1,2]))