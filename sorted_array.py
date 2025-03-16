def sorted_array(arr_1: list[int], arr_2: list[int]) -> list[int]:
	left = 0
	right = 0
	res = []
	
	while left < len(arr_1) and right < len(arr_2):
		if arr_1[left] <= arr_2[right]:
			res.append(arr_1[left])
			left += 1
		else:
			res.append(arr_2[right])
			right += 1
	
	while left < len(arr_1):
		res.append(arr_1[left])
		left += 1
	
	while right < len(arr_2):
		res.append(arr_1[right])
		right += 1
	
	return res