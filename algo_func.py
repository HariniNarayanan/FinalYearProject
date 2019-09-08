from sp import sp_func

def capControllerPlacement(disArray, K):
	lower = 0
	upper = len(disArray - 1)
	while lower<upper :
		mid = (lower+upper)/2
		r = disArray[mid]
		n = sp_func(r)
		if n>K:
			lower = mid + 1
		else:
			upper = mid

	index = lower
	num_of_controllers = sp_func(disArray[index])
	while num_of_controllers>K:
		index = index + 1
		num_of_controllers = sp_func(disArray[index])

	return disArray[index]
