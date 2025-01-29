class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s ==t:
            return True
        index=0

        while index<len(s)-1:

            if s[0]=="#":
                s = s[1:]
                continue

            if s[index+1] == '#':
                s = s[:index] + s[index+2:]
                index=0
                continue
            else:
                index=index+1
        index=0
        while index<len(t)-1:
            
            if t[0]=="#":
                t = t[1:]
                continue
            if t[index+1] == '#':
                t = t[:index] + t[index+2:]
                index=0
                continue
            else:
                index=index+1

        return s==t

        
s="y#fo##f"
t="y#f#o##f"
solution = Solution()

result = solution.backspaceCompare(s,t)

print(result)