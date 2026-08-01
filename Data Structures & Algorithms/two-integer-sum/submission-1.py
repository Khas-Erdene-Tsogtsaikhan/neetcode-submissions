class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        # brute force approach i can see is i in range and then j in range
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]