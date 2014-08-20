# Given a list of integers, find the first missing positive integer
# in one pass using constant space.

# Algorithm: go through the list, if A[i] is less than the length 
# of A, then put it on the (A[i])th position, excluding the negative integer,
# otherwise, ignore it. For example, if 8 occurs in a list of 4 elements,
# number 8 can not influence the final result unless the list have enough
# room storing number 1-7. By eliminating the unwanting number, we can
# find the first missing positive element in one pass.
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A): 
        pointer = 0 
        length = len(A)
        #pdb.set_trace()
        while pointer != length:
            if A[pointer] <= 0 or A[pointer] > length or A[pointer] == pointer+1:
                pointer = pointer + 1 
                continue
            index = A[pointer]
            if A[pointer] == A[index-1]:
                pointer = pointer + 1
                continue
            A[pointer] = A[index-1]
            A[index-1] = index 
        #print A
        target = 1 
        for a in A:
            if target == a:
                target = target + 1 
            else:
                break
        return target