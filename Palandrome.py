__author__ = 'KH9057'
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i=0
        j=len(s)
        while(i<j):
            while(i<j and not(s[i].isalpha())):
                i+=1
            while(i<j and not(s[j].isalpha())):
                j-=1
            if(i<j and s[i].lower()!=s[j].lower()):
                return False
        return True