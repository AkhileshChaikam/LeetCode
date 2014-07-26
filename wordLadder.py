__author__ = 'KH9057'
'''Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.'''

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if len(dict) is 0:
            return 0
        List1, List2 = [], []
        List1.append(start)
        List2.append(1)
        if(end not in dict):
            dict.append(end)
        return self.myFun(end, dict, List1, List2, [],[])

    def myFun(self, end, dict, List1, List2, finalList,push):
        if len(List1) is 0:
            return 0
        curr_distance = List2.pop(0)
        curr_element = List1.pop(0)
        if curr_element == end:
            finalList.append(push)
        for i in range(0, len(curr_element), 1):
            for j in range(ord('a'), ord('z')+1, 1):
                temp = curr_element[0:i]+chr(j)+curr_element[i+1:len(curr_element)]
                if temp in dict:
                    List1.append(temp)
                    List2.append(curr_distance+1)
                    dict.pop(dict.index(temp))
                    push.append(temp)
                    finalList = self.myFun(end, dict, List1, List2, finalList, push)
        return finalList
S = Solution()
print S.ladderLength("hit","cog",["hot","dot","dog","lot","log"])