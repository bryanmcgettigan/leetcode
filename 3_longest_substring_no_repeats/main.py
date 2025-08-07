class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length<2:
            return length
        p1 = 0
        p2 = 1
        maxLength=1
        cLength=1
        cList=[s[p1]]
        
        while p2<length:
            if s[p2] in cList:
                p1=p1+1
                p2=p1+1
                cList=[s[p1]]
                cLength=1
            else:
                cList.append(s[p2])
                p2=p2+1
                cLength=cLength+1
            maxLength=max(maxLength,cLength)

        return maxLength
        


solution = Solution()
s="au"
print(solution.lengthOfLongestSubstring(s))
