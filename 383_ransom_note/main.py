def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    hmap_mag = {}
    for char in magazine:
        hmap_mag[char] = hmap_mag.get(char,0)+1

    for char in ransomNote:
        if hmap_mag.get(char):
            hmap_mag[char] = hmap_mag.get(char)-1
            if hmap_mag[char] <0:
                return False
        else:
            return False
        
    return True


ransomNote="abcdxe"
magazine = "aabbcccdde"

print(canConstruct(ransomNote,magazine))