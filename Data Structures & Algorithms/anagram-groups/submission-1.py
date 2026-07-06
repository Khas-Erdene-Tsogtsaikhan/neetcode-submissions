class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted the indexed words and then use that sorted word as the key
        # if the word sorted already exists as a key, append taht wrod into the list
        group = {}
        for word in strs:
            key = ' '.join(sorted(word))

            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())


        
        