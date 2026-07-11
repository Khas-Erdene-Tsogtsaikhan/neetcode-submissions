class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #hashmap everythign and then iterate thorugh thte lsit
        #if nums[0]+1 exists 


        # have a )(N ) look up and then interate through every number keep looking up if num[i]-1 exists
        # then with teh length intialied we can then count from then on

        seen = {}
        res = 0

        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i], 1)
        
        for i in range(len(nums)):
            
            
            if nums[i] - 1 not in seen:
                length = 1
                curr = nums[i]
                while curr + 1 in seen:
                    length += 1
                    curr +=1
                res = max(res, length)
        return res



           


            # nums = [3, 2,20,4,10,3,4,5]

        



 












