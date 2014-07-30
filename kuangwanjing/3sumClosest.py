"""
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
"""
class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):
		num.sort()
		closetResult = num[0] + num[1] + num[2]
		for i in range(len(num)):
			j = i + 1
			k = len(num)-1
			while(k > j):
				temp = num[i] + num[j] + num[k]
				if temp == target:
					return target
				if abs(target-temp) < abs(target-closetResult):
					closetResult = temp
				if temp > target:
					k = k - 1
				else:
					j = j + 1
		return closetResult