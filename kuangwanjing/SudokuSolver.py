class Solution:
	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def __init__(self):
		self.bitmark = []
		for i in range(9):
			self.bitmark.append(1 << i)
	def solveSudoku(self, board):
		self.visited = [] # 0->row, 1->col, 2->block
		self.choices = []
		for i in range(9):
			self.visited.append([0,0,0])
			self.choices
		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if num != '.':
					num = int(num)
					blockNum = i / 3 * 3 + j / 3
					visited[num-1][0] = visited[num-1][0] | self.bitmark[i]
					visited[num-1][1] = visited[num-1][1] | self.bitmark[j]
					visited[num-1][2] = visited[num-1][2] | self.bitmark[blockNum]
		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if num == '.':
					blockNum = i / 3 * 3 + j / 3
					for k in range(9):