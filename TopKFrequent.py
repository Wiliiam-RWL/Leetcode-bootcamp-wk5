from ast import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for n in nums:
            if count.get(n, -1) == -1:
                count[n] = 0
            count[n] += 1
        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        keys = list(count.keys())
        for i in range(k):
            res.append(keys[i])
        return res
