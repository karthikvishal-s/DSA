from collections import defaultdict

def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
        
    # Initialize a defaultdict that defaults to integers (0)
    charCount = defaultdict(int)
    
    # Now you can safely use += and -= !
    for ch in s1:
        charCount[ch] += 1
        
    for ch in s2:
        charCount[ch] -= 1
        
    for value in charCount.values():
        if value != 0:
            return False
            
    return True