def isPalindrome( s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    result = ''.join(char for char in s if char.isalpha())
    result = result.lower()

    if len(result)%2==0:
        divide = int(round(len(result)/2))
    else:
        divide = int(round(len(result)/2))

    
    print(divide)
    if len(result)%2==0:
        for char in result[:divide]:
            stack.append(char)
            print("Pushing char " + char)

        for char in result[divide:]:
                popped = stack.pop()
                print("Current char " + char +" Popped char: " + popped)
                if(popped!=char):
                    return False
    else:
        for char in result[:divide]:
            stack.append(char)
            print("Pushing char " + char)

        for char in result[divide+1:]:
                popped = stack.pop()
                print("Current char " + char +" Popped char: " + popped)
                if(popped!=char):
                    return False 
            
            
    return True


s="A man, a plan, a canal: Panama"

print(isPalindrome(s))