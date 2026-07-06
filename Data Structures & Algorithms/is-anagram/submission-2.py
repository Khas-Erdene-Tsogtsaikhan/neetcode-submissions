class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = 1 + seen.get(s[i], 0)
        for i in range(len(s)):
            if t[i] not in seen:
                return False
            else:
                seen[t[i]] -=1
                if seen[t[i]] < 0:
                    return False
        return True

        