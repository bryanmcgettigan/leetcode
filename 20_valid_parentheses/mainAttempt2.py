class Solution:
    def isValid(self, s):


        stack = []
        for char in s:

            if char =="(" or char =="{" or char == "[":
                stack.append(char)
            if char == "}" or char=="]" or char==")":
                if not stack:
                    return False
                newChar = stack.pop()
                if newChar == "{" and char != "}":
                    return False
                if newChar == "(" and char != ")":
                    return False
                if newChar == "[" and char != "]":
                    return False
                
        
        if stack:
            return False
        return True

solution = Solution()
s = "[[]"
print(solution.isValid(s))
        