class Solution:
	def __init__(self):
		self.__directions__ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def exist(self, board, word):
		if len(board) == 0:
			return False
		self.visited = []
		self.board = board
		self.search_word = word
		self.size = (len(board), len(board[0]))
		for i in range(self.size[0]):
			self.visited.append([False]*len(board[0]))
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				self.visited[i][j] = True
				if self.__search__(i, j, 0):
					return True
				self.visited[i][j] = False
		return False
	def __valid__(self, row, col):
		return row >= 0 and row < self.size[0] and col >= 0 and col < self.size[1]
	def __search__(self, row, col, count):
		if self.search_word[count] == self.board[row][col]: 
			#pdb.set_trace()
			if count == len(self.search_word) - 1: return True
			for d in self.__directions__:	
				r = row + d[0]
				c = col + d[1]
				if self.__valid__(r, c) and not self.visited[r][c]:
					self.visited[r][c] = True
					if self.__search__(r, c, count+1):
						return True
					self.visited[r][c] = False 
			return False
		else:
			return False