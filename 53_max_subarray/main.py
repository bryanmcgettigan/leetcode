class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return sum(nums)
        if min(nums) > 0:
            return sum(nums)
        if max(nums) <0:
            return max(nums)
        
        current = 0
        best = -99999999999
        #Sliding door to exclude portions of array that are less than the best
        for num in nums:
            current = max(num,current+num)
            best = max(best,current)
        return best

        
solution=Solution()
nums = [1,1,2,-6,1]
result=solution.maxSubArray(nums)
print(result)