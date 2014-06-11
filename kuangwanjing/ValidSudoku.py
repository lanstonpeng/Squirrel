# use bit vector to record 
# focus on each number, each number has three vectors to relate to its different
# positions in the grid world. The first vector record the row information.
# The second vector records the column information.
# The third vector records the cell information. 
# eg. If the first vector of number 2 is [0,0,0,1,1,0,0,1,0] which means the 3rd,
# 4th and the 7th row have number 2. When trasversing the numbers, check the collision
# between the position of that number and its own position vector.
import pdb
class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def __init__(self):
		self.bitmark = []
		for i in range(9):
			self.bitmark.append(1 << i)
	def isValidSudoku(self, board):
		visited = [] # 0->row, 1->col, 2->block
		for i in range(9):
			visited.append([0,0,0])
		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if num != '.':
					num = int(num)
					if visited[num-1][0] & self.bitmark[i] != 0:
						return False
					if visited[num-1][1] & self.bitmark[j] != 0:
						return False
					blockNum = i / 3 * 3 + j / 3
					if visited[num-1][2] & self.bitmark[blockNum] != 0:
						return False
					visited[num-1][0] = visited[num-1][0] | self.bitmark[i]
					visited[num-1][1] = visited[num-1][1] | self.bitmark[j]
					visited[num-1][2] = visited[num-1][2] | self.bitmark[blockNum]
				#pdb.set_trace()	
		return True

if __name__ == "__main__":
	test = Solution()
	input = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]	
	result = test.isValidSudoku(input)	
	print (result)