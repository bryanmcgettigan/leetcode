class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        start=0
        average=0.0
        # Calculate the average of the first window
        for i in range(k):
            average += float(nums[i]) / k
        maxAverage=average
        end=k
        
        while end<len(nums):
            average=average-nums[start]/k
            average+=nums[end]/k
            maxAverage=max(maxAverage,average)
            start+=1
            end+=1
        return maxAverage
        


solution=Solution()

nums=[1,2,3,4]
k=3
print(solution.findMaxAverage(nums,k))