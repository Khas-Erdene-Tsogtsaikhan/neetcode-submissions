class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        seen = {}
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]

            left = i + 1
            right = len(nums)-1

            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                    continue
                if three_sum > 0:
                    right -=1
                    continue
                if three_sum == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left +=1
                    right -=1
                    while right > left and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


        return res
                # -4, -1, -1, -1 0, 1, 2
                #-3






        
 #[-4, -1, -1, 0, 1, 2]
# -4: 1, -1: 2, 0:1, 1:1, 2:1

#example current:
# -4: 1, -1: 1, 0:1, 1:1, 2:1



            


       




                


        