def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    pLength = 0
    singleUsed=False
    if len(s)==1:
        return 1
    hmap = {}
    for letter in s:
        hmap[letter] = hmap.get(letter,0) + 1
    for val in hmap:
        if (hmap.get(val)%2==0):
            pLength = pLength+hmap.get(val)
        elif (hmap.get(val)==1 ) and not singleUsed:
            pLength=pLength+1
            singleUsed=True
        else:
             pLength = pLength+hmap.get(val)-1
    return pLength


print(longestPalindrome("ccc"))