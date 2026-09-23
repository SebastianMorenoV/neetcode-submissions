class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for numberWord in range(len(strs)):
            sortedLetters = sorted(strs[numberWord])
            sortedWord = "".join(sortedLetters)

            if sortedWord not in groups:
                groups[sortedWord] = []
            groups[sortedWord].append(strs[numberWord])
        
        return list(groups.values())
