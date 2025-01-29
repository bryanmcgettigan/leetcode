class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def values(char):
            valueMap={
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "M":1000
            }
            return valueMap.get(char)
        if len(s) == 1:
            return values(s)
        sum =0
        for index in range(len(s)):
                if(index+1<len(s) and values(s[index])<values(s[index+1]) ):
                    sum-=values(s[index])
                else:
                    sum+=values(s[index])
        return sum

solution = Solution()
s="III"
result = solution.romanToInt(s)

print(result)