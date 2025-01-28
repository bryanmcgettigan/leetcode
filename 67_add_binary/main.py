def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    lengthA = len(a)
    lengthB = len(b)

    reversedA = list(reversed(a))
    reversedB = list(reversed(b))

    output = ""
    if lengthB<lengthA:
        for index,char in enumerate(reversedB):
            if(char == "1" and reversedA[index] == "1"):
                output = output+"0"
                output = output+"1"
                continue
            elif((reversedA[index] == "1") or ((char=="1" ))):
                output = output+"1"

            
    reversedstr="".join(reversed(output))
    return reversedstr

a = "10101"
b = "11"

s = addBinary(a,b)

print(s)