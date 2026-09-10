class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        res = dict(sorted(counts.items(),key=lambda x:x[1], reverse=True))

        return list(res.keys())[:k]