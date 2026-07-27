class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force approach
        # hashmap everything and then sort the list and then get the highest two ines
        # instead we can implement bucket sort where we can
        # attach using the index for how frequent it is and then give the k
        # hashmap everything in to seen, then sorting based on the key 
        #nlogn on top of n, m + m
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            # coutnb how many there are in the hashmap
            # 1, 1 2, 2 3, 3
        freq = [[] for i in range(len(nums)+1)]
        # bu8cket sort
        # index correlate to how frequent
        for num in seen:
            val = seen[num]
            freq[val-1].append(num)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        



        
            




       


        


        
        