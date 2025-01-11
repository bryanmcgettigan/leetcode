def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_map = {}
    for index,num in enumerate(nums):
        temp = target-num
        if temp in num_map:
            return[num_map[temp],index]
        
        num_map[num] = index
   
nums=[3,2,95,4,-3]

print(twoSum(nums,92))