__author__ = 'KH9057'
#There are N children standing in a line. Each child is assigned a rating value.

#You are giving candies to these children subjected to the following requirements:

#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.
#What is the minimum candies you must give?

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        List1 = [1]*len(ratings)
        List2 = [1]*len(ratings)
        i=1
        total = 0
        while(i<len(ratings)):
            if(ratings[i] > ratings [i-1]):
                List1[i] = List1[i-1]+1
            i+=1
        i= len(ratings)-1
        if(i>=0):
            total += max(List1[i],List2[i])
        i -= 1
        while(i>=0):
            if(ratings[i] > ratings[i+1]):
                List2[i] = List2[i+1]+1
            total += max(List1[i],List2[i])
            i-=1
        return total
sol = Solution()
print sol.candy([1,2,1])