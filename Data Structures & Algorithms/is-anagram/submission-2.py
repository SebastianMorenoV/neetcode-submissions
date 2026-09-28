class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newSet = set()

        sOrdered = "".join(sorted(s))
        tOrdered = "".join(sorted(t))

        newSet.add(sOrdered)
        newSet.add(tOrdered)

        if len(newSet) > 1:
            return False
        
        return True