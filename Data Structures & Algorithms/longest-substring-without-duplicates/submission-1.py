class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0

        hashSet = set()
        length = 0

        for R in range (len(s)):

            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1

            length = max(length,R - L + 1)
            hashSet.add(s[R])

        return length