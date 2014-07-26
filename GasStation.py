__author__ = 'KH9057'
#There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

#Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

#Note:
#The solution is guaranteed to be unique.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total = 0
        sum = 0
        i = 0
        j = 0
        index = 0
        if(len(gas) is 0):
            return 0
        while(i<len(gas)):
            sum += gas[i] - cost[i]
            total += sum
            if(sum<0):
                sum =0
                j = i+1
            i += 1
        if(total < 0):
            return -1
        i = 0
        index = j
        while(i <len(gas)):
            sum += gas[j]-cost[j]
            if(sum < 0):
                return -1
            i += 1
            j =(j+1)%len(gas)
        return index



