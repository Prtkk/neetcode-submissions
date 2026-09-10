class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq_ls = [[] for i in range(len(nums)+1)]

        for n in nums:
            counts[n] += 1

        for n,c in counts.items():
            freq_ls[c].append(n)

        res = []
        for i in range(len(freq_ls)-1,0,-1):
            for n in freq_ls[i]:
                res.append(n)
                if len(res) == k:
                    return res