class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # simple one
        zero = 0
        total = 1
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                total *= nums[i]

        if zero>1:
            return [0 for i in range(len(nums))]
        if zero == 0:
            for i in range(len(nums)):
            
                temp = total//nums[i]

                res.append(temp) 
            return res

        if zero == 1:
               
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(total)
                else: 
                    res.append(0)
        return res
            



        