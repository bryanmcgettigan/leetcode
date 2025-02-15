class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def feasable(divisor):
            sum =0
            for num in nums:
                sum = (((num//divisor) + ((num%divisor)>0))+sum)
            return sum<=threshold
        
        start=1
        end=max(nums)
        mid=0

        while start<end:
            mid=(start+end)//2

            if feasable(mid):
                if mid==1:
                    return mid
                end=mid-1
            else:
                start=mid+1
        if not feasable(end):
            return end+1
        else:
            return end         

solution = Solution()

        
nums = [9,63,69,43,95,11,7]
threshold = 302


print(solution.smallestDivisor(nums,threshold))
