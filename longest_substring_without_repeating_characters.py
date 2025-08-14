def lengthOfLongestSubstring(s):
	if len(s) <= 2:
		return len(s) if len(s) <= 1 else 2 if s[0] != s[1] else 1

	max_count = 0

	for j in range(len(s) - 1):
		visited = []
		count = 0
		for k in range(j, len(s)):
			if s[k] not in visited:
				count += 1
				max_count = count if count > max_count else max_count
			else:
				break
			visited.append(s[k])

	return max_count


print(lengthOfLongestSubstring("pwwkew"))