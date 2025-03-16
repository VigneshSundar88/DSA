def squares_of_a_sorted_array(nums: list[int]) -> list[int]:
	left = 0
	right = len(nums) - 1
	res = [1] * len(nums)
	
	for i in range(len(nums)-1, -1, -1):
		if abs(nums[left]) <= abs(nums[right]):
			res[i] = nums[right] * nums[right]
			right -= 1
		else:
			res[i] = nums[left] * nums[left]
			left += 1
	return res