'''PRoblem : Minimum Moves to Equal Array Elements II '''

#CODE :

class Solution:
    def minMoves2(self, nums):
        nums.sort()
        mid=len(nums)//2
        res=0
        for n in nums:
            res+=abs(n-nums[mid])
        return res
