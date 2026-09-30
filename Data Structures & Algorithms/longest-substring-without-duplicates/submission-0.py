class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        char_set = set()
        maxLength = 0
        for R in range(len(s)):

            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1

            char_set.add(s[R])

            window = R - L + 1
            maxLength = max(maxLength, window)
        return maxLength
        
