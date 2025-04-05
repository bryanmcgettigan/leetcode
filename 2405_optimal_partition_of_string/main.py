class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        rList=[]
        left =0
        right=1
        while left<=len(s)-1:
            cString=s[left]
            right=left+1
            if right>len(s)-1:
                rList.append(cString)
                break

            while s[right] not in cString:
                cString+=s[right]
                right=right+1
                if right>len(s)-1:
                    break

            rList.append(cString)
            left=right

        
        return len(rList)


solution = Solution()

s="ssssss"
print(solution.partitionString(s))
            
        