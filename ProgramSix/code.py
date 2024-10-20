def isPalindrome(str):
    revStr = str[::-1]
    if(revStr == str): return True
    return False
    
print(isPalindrome("rabi"))
print(isPalindrome("racecar"))
print(isPalindrome("naman"))