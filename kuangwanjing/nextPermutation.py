class Solution:
	def nextPermutation(self, num):
		length = len(num)
		index = length-1
		while index >= 0: 
			target = num[index]
			temp = False 
			for j in range(index+1, length):
				if num[j] > target:
					if temp == False:
						temp = num[j] 
						pos = j
					else:
						if temp > num[j]:
							temp = num[j]
							pos = j
			if temp:
				num[index] = temp
				num[pos] = target
				tempnum = num[index+1:length]
				tempnum.sort()
				return num[0:index+1] + tempnum
			index = index - 1
		num.sort()
		return num