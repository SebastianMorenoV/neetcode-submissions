class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        
        longest_sequence = 0        
        for num in nums:
            if num -  1 not in numberSet:
                
                current_length = 1

                while(num + current_length) in numberSet:
                    current_length += 1
                if current_length > longest_sequence:
                    longest_sequence = current_length
        return longest_sequence
  
        