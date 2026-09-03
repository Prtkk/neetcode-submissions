class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for i in s:
            counts[i] = 1 + counts.get(i,0)

        for i in t:
            if i not in counts.keys():
                return False
            counts[i] -= 1

        for i,k in counts.items():
            if k != 0:
                return False

        return True
        