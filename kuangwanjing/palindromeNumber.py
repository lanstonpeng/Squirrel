"""
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
"""
"""
class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		if x < 0:
			return False
		if x == 0:
			return True
		arr = []
		while x > 0:
			arr.append(x % 10)
			x = x / 10
		l = len(arr)
		for i in range(l/2):
			if arr[i] != arr[l-i-1]:
				return False
		return True
"""
class Solution: 
	# @return a boolean
	def isPalindrome(self, x):
		if x < 0:
			return False
		if 0 <= x < 10:
			return True
		count = 0
		temp = x
		while temp > 0:
			temp = temp / 10 
			count = count + 1
		numbit = count / 2
		half_reverse_num = 0
		for i in range(numbit):
			half_reverse_num = half_reverse_num * 10 + x % 10
			x = x / 10
		if count % 2 == 1:
			x = x / 10
		return half_reverse_num == x 