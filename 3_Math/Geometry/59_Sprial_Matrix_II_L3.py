def generateMatrix(self, n: int) -> List[List[int]]:
	steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	direction = 0
	res = [[None] * n for _ in range(n)]

	x, y = 0, 0
	for i in range(1, n * n + 1):
		res[x][y] = i
		a, b = steps[direction]
		if not (n > x + a >= 0 <= y + b < n and not res[x + a][y + b]):
			direction = (direction + 1) % 4
			a, b = steps[direction]
		x = x + a
		y = y + b

	return res
