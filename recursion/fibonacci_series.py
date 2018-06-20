def fib_recr(num, buffer=None):
	if num == 0:
		return 1

	if num == 1:
		return 1

	if buffer is None:
		buffer = dict()

	if num - 1 in buffer:
		prev1 = buffer[num - 1]
	else:
		prev1 = fib_recr(num - 1, buffer)
		buffer[num - 1] = prev1

	if num - 2 in buffer:
		prev2 = buffer[num - 2]
	else:
		prev2 = fib_recr(num - 2, buffer)
		buffer[num - 2] = prev2

	return prev1 + prev2


if __name__ == '__main__':
	print(fib_recr(55))