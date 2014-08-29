# the solution is based on the largest Rectangle Area.
# and its solution is implemented in largestRectangleArea
# method.
class Solution:
	def largestRectangleArea(self, height):
		indexStack = []	
		height.append(0)
		result = 0
		i = 0
		while i < len(height):
			if len(indexStack) == 0 or height[indexStack[-1]] <= height[i]:
				indexStack.append(i)
				i += 1
			else:
				temp = indexStack[-1]	
				indexStack.pop()
				if len(indexStack) == 0:
					result = max(result, height[temp] * i)
				else:
					result = max(result, height[temp] * (i-indexStack[-1]-1))
		return result
		
	def maximalRectangle(self, matrix):
		if len(matrix) == 0:
			return 0
		if len(matrix[0]) == 0:
			return 0
		rc = len(matrix)
		cc = len(matrix[0])
		result = 0
		for i in range(rc):
			height = []
			# count the continuous 1 in one column starting at
			# row i
			for j in range(cc):
				index = i
				count = 0
				while index < rc and matrix[index][j] == "1":
					count += 1
					index += 1
				height.append(count)
			temp = self.largestRectangleArea(height)
			result = max(temp, result)
		return result