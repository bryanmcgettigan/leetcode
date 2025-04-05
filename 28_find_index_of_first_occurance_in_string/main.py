class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for index in range(0,(len(haystack)-len(needle))+1):
            right=0
            currentChar=needle[right]
            left=index
            while(haystack[left]==currentChar):
                left=left+1
                right=right+1
                if right == len(needle):
                    return index
                currentChar=needle[right]
            
        return -1

        

solution = Solution()

haystack="abc"
needle="c"
print(solution.strStr(haystack,needle))