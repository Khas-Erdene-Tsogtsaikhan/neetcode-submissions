class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        # brute force approach i can see is i in range and then j in range
        # now we can optimize using a hashmap to make coutn and then once the if there is any in the
        #hashmap where the iterated numbers go over, and it equals targhet, we just get form the hashmap and tghe 
        #hashmap will be the invariant where the iundexes will be the nuymber, thje look up should be 
        # the l;ook up should be instant, so the num itself when minused form the target

        seen = {}

        for i in range(len(nums)):
            
            if target - nums[i] in seen:
                return [seen.get(target-nums[i]), i]
            seen[nums[i]] = i


