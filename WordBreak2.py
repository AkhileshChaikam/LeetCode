#Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

#Return all such possible sentences.

#For example, given
#s = "catsanddog",
#dict = ["cat", "cats", "and", "sand", "dog"].

#A solution is ["cats and dog", "cat sand dog"].

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        mysol = []
        list1 = []
        dict1 = {}
        for i in range(0,len(s),1):
            list2 = [False]*len(s)
            list1.append(list2)
        self.myFun(s,dict,len(s),list1,dict1)
        self.dfs(list1,dict,s,mysol,0,"")
        print mysol

    def myFun(self, s, dict,n,list1,dict1):
        for i  in range(0,n+1,1):
            for j in range(i+1,n+1,1):
                if(s[i:j] in dict):
                    list1[i][j-1]=True

    def dfs(self,list1,dict,s,mysol,index,appendString):
        if(index == len(s)):
            mysol.append(appendString.strip())
            return
        for i in range(index,len(list1[0]),1):
            if(list1[index][i] is True):
                self.dfs(list1,dict,s,mysol,i+1,appendString+ " "+s[index:i+1])



string = "leetcode"
dict = {"leet","code"}
Soln = Solution()
Soln.wordBreak(string,dict)