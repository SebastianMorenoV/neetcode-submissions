class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap1= {}
        hashMap2= {}

        for i in range (len(s)):
            hashMap1[s[i]] = hashMap1.get(s[i],0) + 1
        
        for i in range(len(t)):
            hashMap2[t[i]] = hashMap2.get(t[i],0) + 1

        return hashMap1 == hashMap2