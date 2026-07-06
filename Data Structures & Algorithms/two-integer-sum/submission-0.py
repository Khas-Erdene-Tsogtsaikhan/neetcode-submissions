class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # put everything into a hash. while iterating thorugh the indexes
        # if we find anything that can add up to the target we return the indexes


        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            else:
                seen[nums[i]] = i
                