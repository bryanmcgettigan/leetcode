def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    sList = []
    tList = []
    for char in s:
        sList.append(char)

    for char in t:
        tList.append(char)

    sList= sorted(sList)
    tList = sorted(tList)

    for index,char in enumerate(sList):
        if char != tList[index]:
            return False
    
    return True


s = "hello"
t= "ollhse"

print(isAnagram(s,t))