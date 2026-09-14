class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if not mp[num]:
                l = mp[num-1]+mp[num+1]+1
                mp[num] = l
                mp[num-mp[num-1]] = l
                mp[num+mp[num+1]] = l
                res = max(res,mp[num])

        return res 
        