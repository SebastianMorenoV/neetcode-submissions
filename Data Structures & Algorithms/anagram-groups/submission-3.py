class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        keys = {}

        # Iterate across all the original array
        for i in range(len(strs)):
            # We need to order the word alphabetically to always know if it is on the map already.
            sortedWord = "".join(sorted(strs[i]))
            # if the word is not in the dictionary it means that we need to add the new key.
            if sortedWord not in keys:
                keys[sortedWord] = []
            # even the key is already there, we add the original word to the dictionary.   
            keys[sortedWord].append(strs[i])
        return list(keys.values())
            

        