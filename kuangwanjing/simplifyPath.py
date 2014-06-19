import pdb
class Solution:
	# @param path, a string
	# @return a string
	def __init__(self):
		self.__state__ = {
			'SLASH' : 0,
			'DOT'   : 1,	
			'CHAR'  : 2,
			'DOT2'  : 3,
			'ODOT'  : 4,
		}
	def simplifyPath(self, path):
		result = []
		dirname = []
		state = self.__state__['SLASH']
		#pdb.set_trace()
		for c in path:
			if state == self.__state__['SLASH']:
				if c == '/':
					continue
				else:
					if c == '.':
						state = self.__state__['DOT']
					else:
						dirname.append(c)
						state = self.__state__['CHAR']
			else:
				if state == self.__state__['DOT']:
					if c == '/':
						state = self.__state__['SLASH']
					else:
						if c == '.':
							state = self.__state__['DOT2']
						else:
							dirname.append('.' + c)
							state = self.__state__['CHAR']
				else:
					if state == self.__state__['DOT2']:
						if c == '/':
							if len(result) > 0:
								result.pop(-1)
							state = self.__state__['SLASH']
						else:
							if c == '.':
								dirname.append('...')	
								state = self.__state__['CHAR']
							else:
								dirname.append('..' + c)
								state = self.__state__['CHAR']
					else:
						if state == self.__state__['CHAR']:
							if c == '/':
								result.append(''.join(dirname))
								dirname = []
								state = self.__state__['SLASH']
							else:
								dirname.append(c)
		if len(dirname) > 0:
			result.append(''.join(dirname))
		if len(result) > 0:
			return '/' + '/'.join(result)
		else:
			return '/'

test = Solution()
print (test.simplifyPath('/a/./b/../../c'))
print (test.simplifyPath('/'))
print (test.simplifyPath('/abc/...'))
print (test.simplifyPath('/..hidden'))
print (test.simplifyPath('/.....hidden'))
print (test.simplifyPath('/..ab../'))
