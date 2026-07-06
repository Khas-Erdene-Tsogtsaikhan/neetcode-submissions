class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hashmap and then if there exists the value in the hashmap
        # return true else false after iterating over the loop

        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = 1

        return False