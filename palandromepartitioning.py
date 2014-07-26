__author__ = 'KH9057'
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        Arr = []
        n= len(s)
        result = [0]*n
        res = n
        if(n ==0):
            return None
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
        List1 = []
        for i in range(0,n,1):
            if(Arr[0][i] == True):
                List1 = self.partitionii(Arr,i+1,s,List1,s[0:i+1]+"")
        return List1

    def partitionii(self, Arr,index,s,List1,str):
        if(index == len(s)):
            List2  = str.strip().split(" ")
            List1.append(List2)
            return List1
        for i in range(index,len(s),1):
            if(Arr[index][i] == True):
                List1 = self.partitionii(Arr,i+1,s,List1,str+" "+s[index:i+1])
        return List1

sol = Solution()
print sol.partition("a")