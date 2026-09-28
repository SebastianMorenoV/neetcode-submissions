class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowerCase = s.lower()
        formatedString = "".join(c for c in lowerCase if c.isalnum())

        print(formatedString)
        ## We have the String already with no symbols and Spaces.

        L = 0
        R = len(formatedString) - 1 

        while L < R:
            if formatedString[L] != formatedString[R]:
                return False
            
            L += 1
            R -= 1

        return True