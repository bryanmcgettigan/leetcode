def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    hmap={}
    for char in s:
        hmap[char] = hmap.get(char,0)+1
        if hmap[char] % 2 ==0:
            sum+=2
    
    for cnt in hmap.values():
        if cnt%2:
            sum+=1
            break


    return  sum

print(longestPalindrome("ababababa"))