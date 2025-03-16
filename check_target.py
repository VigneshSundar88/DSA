def check_target(nums: list[int], target: int) -> bool:
	left = 0
	right = len(nums) - 1
	
	while left < right:
		if nums[left] + nums[right] > target:
			right -= 1
		elif nums[left] + nums[right] < target:
			left -= 1
		else:
			return True
	return False