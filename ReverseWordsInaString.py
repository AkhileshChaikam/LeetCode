__author__ = 'KH9057'
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s= s.strip()
        if(len(s) == 0):
            return ""
        List1 = s.split(' ')
        print List1
        print len(List1)
        i=0
        while(i < len(List1)):
            if(len(List1[i]) == 0):
                List1.remove(List1[i])
                i -= 1
            else:
                reversed(List1[i])
            i+=1
        List1.reverse()
        print List1
        return ' '.join(List1)




obj = Solution()
print obj.reverseWords("  akhil     good   boy")