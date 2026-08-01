class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if not the same len return false, 
        # if the i think we shouyld hash on eword, since if they are anagrams
        # which is the invariant, then we should minus from the other word
        # and then return the len o fht ehasmap

        if len(s) != len(t):
            return False
        seen = {}
        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1
        for char in t:
            if char in seen:
                seen[char] -= 1
                if seen[char] == 0:
                    seen.pop(char)
            else:
                return False
        return len(seen) == 0

        
        
                
        