class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        number_frecuencies = {}

        for i in range(len(nums)):
            if nums[i] not in number_frecuencies:
                number_frecuencies[nums[i]] = 0
            number_frecuencies[nums[i]] += 1
        
        frecuencies = []

        for number, count in number_frecuencies.items():
            frecuencies.append([count,number])
        
        frecuencies.sort(reverse = True)

        tops = []
        for i in range(k):
            tops.append(frecuencies[i][1])

        return tops