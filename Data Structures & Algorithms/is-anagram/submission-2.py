class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for ch in s:
            if ch not in countS:
                countS[ch]  = 0 
            countS[ch] += 1

        for ch in t:
            if ch not in countT:
                countT[ch] = 0
            countT[ch] += 1
            
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True