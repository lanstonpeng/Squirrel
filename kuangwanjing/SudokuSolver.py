import pdb
import copy
class Solution:
	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def __init__(self):
		self.bitmark = []
		self.board = []
		for i in range(9):
			self.bitmark.append(1 << i)
	def recursive(self, count, i, j):
		if count == 81:
			#pdb.set_trace()	
			return True
		while self.board[i][j] != '.':
			if j < 8:
				j = j + 1
			else:
				i = i + 1
				j = 0
		result = False
		for k in range(9):
			blockNum = i / 3 * 3 + j / 3
			if not self.visited[k][0] & self.bitmark[i] and not self.visited[k][1] & self.bitmark[j] and not self.visited[k][2] & self.bitmark[blockNum]:
				t1 = copy.copy(self.visited[k][0])
				t2 = copy.copy(self.visited[k][1])
				t3 = copy.copy(self.visited[k][2])
				self.visited[k][0] = self.visited[k][0] | self.bitmark[i]
				self.visited[k][1] = self.visited[k][1] | self.bitmark[j]
				self.visited[k][2] = self.visited[k][2] | self.bitmark[blockNum]
				#self.board[i] = self.board[i][:j] + str(k+1) + self.board[i][j+1:]
				l = list(self.board[i])
				l[j] = str(k+1)
				self.board[i] = "".join(l)
				if j < 8:
					result = self.recursive(count+1, i, j+1)
				else:
					result = self.recursive(count+1, i+1, 0)
				if result:
					return True
				l = list(self.board[i])
				l[j] = '.' 
				self.board[i] = "".join(l)
				self.visited[k][0] = t1
				self.visited[k][1] = t2
				self.visited[k][2] = t3
		return False
				
	def solveSudoku(self, board):
		self.visited = [] # 0->row, 1->col, 2->block
		self.board = []
		for i in range(9):
			self.visited.append([0,0,0])
		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if num != '.':
					num = int(num)
					blockNum = i / 3 * 3 + j / 3
					self.visited[num-1][0] = self.visited[num-1][0] | self.bitmark[i]
					self.visited[num-1][1] = self.visited[num-1][1] | self.bitmark[j]
					self.visited[num-1][2] = self.visited[num-1][2] | self.bitmark[blockNum]

		count = 0
		for i in range(9):
			for j in range(9):
				if board[i][j] != '.':
					count = count + 1
		precount = 0 
		while precount < count:
			precount = count
			for i in range(9):
				for j in range(9):
					choices = []
					if board[i][j] == '.':
						blockNum = i / 3 * 3 + j / 3
						for k in range(9):
							if not self.visited[k][0] & self.bitmark[i] and not self.visited[k][1] & self.bitmark[j]:
								if not self.visited[k][2] & self.bitmark[blockNum]:
									choices.append(k+1)
						if len(choices) == 1:
							newnum = choices[0]
							l = list(board[i])
							l[j] = str(newnum)
							board[i] = "".join(l)
							count = count + 1
							self.visited[newnum-1][0] = self.visited[newnum-1][0] | self.bitmark[i]
							self.visited[newnum-1][1] = self.visited[newnum-1][1] | self.bitmark[j]
							self.visited[newnum-1][2] = self.visited[newnum-1][2] | self.bitmark[blockNum]
		self.board = board
		self.recursive(count, 0, 0)
		board = self.board
		for b in board:
			print b

if __name__ == "__main__":
	test = Solution()
	#input = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]	
	input = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
	test.solveSudoku(input)	

