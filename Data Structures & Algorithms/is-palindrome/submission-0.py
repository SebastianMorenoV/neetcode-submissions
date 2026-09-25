class Solution:
    def isPalindrome(self, s: str) -> bool:
        orderedString = "".join(c.lower() for c in s if c.isalnum())

        L = 0
        R = len(orderedString) - 1

        while L < R :
            if orderedString[L] != orderedString[R]:
                return False
            else :
                L += 1
                R-= 1
        return True
