class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lNums = len(nums)
        setnums = set(nums)
        lsetNums = len(setnums)

        if lNums>lsetNums:
            return True
        else:
            return False

solution = Solution()


nums = [1,2,3,3]
result = solution.containsDuplicate(nums)

print(result)