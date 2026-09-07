class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq[i] will store all numbers that appear exactly i times
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        # Scan from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res