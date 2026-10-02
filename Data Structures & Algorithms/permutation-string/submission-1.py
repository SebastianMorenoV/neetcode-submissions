class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count_s1= {}
        window_count= {}

        for char in s1:
            count_s1[char] = count_s1.get(char,0) + 1
        
        windowSize = len(s1)
        for i in range (windowSize):
            window_count[s2[i]] = window_count.get(s2[i],0) + 1

        L= 0
        for R in range(len(s1),len(s2)):
            if count_s1 == window_count:
                return True
        
            left_char = s2[L]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            L += 1

            right_char = s2[R]
            window_count[right_char] = 1 + window_count.get(right_char,0)

            if count_s1 == window_count:
                return True
        return count_s1 == window_count


            


     