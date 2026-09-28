class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sortedArray = sorted(nums)
        solutions = []

        for i,num in enumerate(sortedArray):
            L = i + 1
            R = len(sortedArray) - 1

            if i > 0 and num == sortedArray[i -1]:
                continue

            while L < R:
                    if sortedArray[L] + sortedArray[i] + sortedArray[R] == 0:
                        solutions.append([sortedArray[L],sortedArray[i],sortedArray[R]])
                        L += 1
                        while L < R and sortedArray[L] == sortedArray[ L - 1]:
                            L+= 1
                        
                    elif sortedArray[L] + sortedArray[i] + sortedArray[R] > 0:
                        R -= 1
                    elif sortedArray[L] + sortedArray[i] + sortedArray[R] < 0:
                        L += 1
        return solutions

        
            
