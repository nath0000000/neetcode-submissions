class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ds, Dt = dict(), dict()
        for char in s: 
            if not (char in Ds):
                Ds[char] = 1
            else: 
                Ds[char] += 1
        for char in t: 
            if not char in Dt:
                Dt[char] = 1
            else: 
                Dt[char] += 1
        if len(Ds) != len(Dt):
            return False
        for char in t: 
            if not (char in Ds):
                return False
            if char in Ds and Ds[char] != Dt[char]:
                return False
        return True