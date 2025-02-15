class Solution(object):
    def maxSubArray(self, nums):
        current=0
        best = -99999999999999999
        for num in nums:
            current = max(current+num,num)
            best = max(best,current)
 
        return best



solution = Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))