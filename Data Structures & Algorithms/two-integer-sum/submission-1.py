class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,v in enumerate(nums):
            k = target - v 
            if k in seen:
                return [seen[k],i]
            
            seen[v] = i

        return []