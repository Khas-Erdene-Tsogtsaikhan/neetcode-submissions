class Solution:
    def findMin(self, nums: List[int]) -> int:

        # 1, 2, 3, 4, 5

        # 5, 1, 2, 3, 4
        # 4, 5, 1, 2, 3
        # 3, 4, 5, 1, 2

        #2, 3, 4, 5, 1


        # check if mid is bigger than first
        # check if first is bigger than last

        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left <= right:
            # invariant is that in a sorted list nums[right] will always be bigger than left
            if nums[right] > nums[left]:
                res = min(res, nums[left])
                break
            # found a pattern that if mid is greater or less, then right or left is sorted based on that
            mid = (right + left) // 2
            if nums[mid] < nums[right]:
                res = min(res, nums[mid])
                right = mid -1
            else:
                res = min(res, nums[mid])
                left = mid + 1
        return res





           