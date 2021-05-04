'''PROBLEM : Running Sum Of 1D Array '''

#CODE :

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:

        sum = 0

        sum_arr = []

        for i in range(len(nums)):
            sum += nums[i]
            sum_arr.append(sum)

        return sum_arr
