class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## NEEED TO REVIEW THIS PROBLEM IS VERY TRICKY I NEED TO CLEARLY UNDERSTAND THE LOGIC BEHIND.
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postFix = 1
        for i in range(len(nums)-1, -1,-1):
            result[i]*=postFix
            postFix *= nums[i]
        return result
        
            