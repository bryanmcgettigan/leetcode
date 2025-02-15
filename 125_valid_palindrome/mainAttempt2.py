class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s=s.replace(" ","")
        s=s.replace("   ","")
        s=s.replace(",","")
        s=s.replace(":","")

        
        s = list(s)
        nList = []
        for char in s:
            if char in "abcdefghijklmnopqrstuvwxyz":
                nList.append(char)
        reversedS = list(reversed(nList))
        print(s)
        print(reversedS)
        return nList==reversedS



solution = Solution()
s="......a....."
print(solution.isPalindrome(s))