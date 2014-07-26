__author__ = 'KH9057'
'''Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.'''

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        Arr = []
        n= len(s)
        result = [0]*n
        res = n
        if(n <=1):
            return 0
        i=0
        for i in range(0,n,1):
            temp = [False]*len(s)
            Arr.append(temp)
        i=0
        for i in range(0,n,1):
            Arr[i][i] = True
            if(i!= n-1 and s[i] == s[i+1]):
                Arr[i][i+1] = True
        i = 0
        k = 2
        for i in range(0,n-k,1):
            m = 0
            for j in range(i+k,n,1):
                if(s[m] == s[j] and Arr[m+1][j-1]):
                    Arr[m][j] = True
                m += 1
        i=0
        for i in range(0,n,1):
            res= n
            if(Arr[0][i]):
                result[i] = 0
            else:
                for j in range(1,i+1,1):
                    if(Arr[j][i] and res>result[j-1] + 1):
                        res = result[j-1]+1
                result[i] = res
        return result[n-1]
sol = Solution()
print sol.minCut("abbaabba")