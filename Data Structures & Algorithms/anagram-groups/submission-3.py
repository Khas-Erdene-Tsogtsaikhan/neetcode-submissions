class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # to do this, we can implement a sort of list for all 26 alphabets
        # using these alphabets we can initiate a list of 0's for the entire list
        # then for each word, we use its letter as a sort of code.
        # because in a list there is no order, only the code. 
        # and then we group them with the codes. hashmap the codes with the word basically
        # the key should be the hashmap. 

        
        seen = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            seen[tuple(count)].append(word)
        return list(seen.values())


        
        
        


        
        