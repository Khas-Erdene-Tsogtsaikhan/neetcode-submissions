class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
       

        #iterating through the range but -2 and then using left and righr pointers
        #this way we can effective use the three sum and then skipping over any duplicates


        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1


            while right> left:
                three_sum = (nums[left]+nums[right]+nums[i])
                if three_sum > 0:
                    right -=1
                    continue
                if three_sum < 0:
                    left +=1
                    continue
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while right > left and nums[left] == nums[left+1]:
                        left +=1
                    while right> left and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
        return res











        
 #[-4, -1, -1, 0, 1, 2]
# -4: 1, -1: 2, 0:1, 1:1, 2:1

#example current:
# -4: 1, -1: 1, 0:1, 1:1, 2:1



            


       




                


        