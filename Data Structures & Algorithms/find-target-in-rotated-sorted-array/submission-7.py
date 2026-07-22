class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid


            if nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                    continue
                
                else:
                    right = mid - 1
                    continue
            if nums[mid] >= nums[right]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1
                    continue
                
                else:
                    left = mid + 1
                    continue
        return -1

            
                # 1, 2, 3, 4, 5
                # 5, 1, 2, 3, 4
                #4, 5, 1, 2, 3
                #3, 4, 5, 1, 2

        