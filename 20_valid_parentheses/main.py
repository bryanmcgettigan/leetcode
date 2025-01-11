
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if(len(s)%2!=0):
        return False

    stack = []


    for char in s:
        if char == "[" or char == "{" or char =="(":
            stack.append(char)
        if(char==')'):
            if stack:
                charnew = stack.pop()
                if charnew != '(':
                    return False
            else:
                return False
        elif(char=='}'):
            if stack:
                charnew = stack.pop()
                if charnew != '{':
                    return False
            else:
                return False
        elif(char==']'):
            if stack:
                charnew = stack.pop()
                if charnew != '[':
                    return False
            else:
                return False
    
    if stack:
        return False
    
    return True


s = "()[]{}"
print(isValid(s))