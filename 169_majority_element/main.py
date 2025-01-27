def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)/2
    hmap = {}
    for num in nums:
        curr = hmap.get(num,0)
        hmap[num] = curr+1
        if curr>=length:
            return num

nums =[2,2,1,1,1,2,2]

print(majorityElement(nums))