class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach
        # hashmap everything and then sort the list and then get the highest two ines
        # instead we can implement bucket sort where we can
        # attach using the index for how frequent it is and then give the k
        # hashmap everything in to seen, then sorting based on the key 
        #nlogn on top of n, m + m

        count = {}

        for i in range(len(nums)):
            count[nums[i]]=1+count.get(nums[i], 0)

        # nums = [7, 8, 8, 5, 5, 5]  
        # 7:1 8:2 5:3
        bucket = [[] for _ in range(len(nums)+1)]

        for x, y in count.items():
            bucket[y].append(x)

        res = []
        for i in range(len(nums), -1, -1):
            if bucket[i] is not None:
                for num in bucket[i]:
                    res.append(num)
                    k-=1
            if k == 0:
                break
        return res
            




       


        


        
        