class Solution(object):
    def twoSum(self, nums, target):
        #Use hmap
        hmap = {}
        for index,num in enumerate((nums)):
            remainder = target-num

            if remainder in hmap:
                return [index,hmap.get(remainder)]
            hmap[num] = index
        print(hmap.get(2))




solution = Solution()

nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums,target))