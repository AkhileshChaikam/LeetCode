__author__ = 'KH9057'
#Given an array of integers, every element appears three times except for one. Find that single one.
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one =0
        two =0
        both = 0
        for i in A:
            two = two |(one&i)
            one = one^i
            both = ~(one & two)
            one = one & both
            two = two & both
        return one | two
sol = Solution()
print sol.singleNumber([1,1,2,2,2,3])
