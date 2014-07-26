__author__ = 'KH9057'

#Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

#For example, given
#s = "leetcode",
#dict = ["leet", "code"].

#Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        mysol = []
        n = len(s)
        if(n!=0 and len(dict) == 0):
            return False
        if(n==0 and len(dict) == 0):
            return True
        list1=[False]*n
        for i  in range(0,n,1):
            if(s[0:i+1] in dict):
                string = ""
                list1[i]=True
                if i == n-1:
                    return True
            if(list1[i] == True):
                for j in range(i+1,n+1,1):
                    if(s[i+1:j] in dict):
                        if(j == n):
                            return True
                        list1[j-1] = True
        return False


sol = Solution()
print sol.wordBreak("abcd",["a","abc","b","cd"])
