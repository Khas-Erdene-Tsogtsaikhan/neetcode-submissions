class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        # use a hashmap to track and then look up
        # for each sub string, we are going to 
        maxf = 0
        # abbcacbbca, res = 3, freq would be B, in the current substring
        # the most frequent letter - len(substring), we get 2, and k < 2 so move left once 
        # until the substring is valid. eg when len- freq is equal to or less tahn k
        # sum of the hasmaps can be used as the size of the substring and then freq

        seen = {}

        #summary: hashmap, get most freq in relative window, and then see if the condition matches
        # and then filter out until its valid with teh left pointer sliding up until the condition
        #matches and then return the max of the resul

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            maxf = max(seen.values())

            while (i - left + 1) - maxf > k:
                seen[s[left]] -=1
                left += 1
                

            res = max(res, i-left+1)

        return res





        
        





        