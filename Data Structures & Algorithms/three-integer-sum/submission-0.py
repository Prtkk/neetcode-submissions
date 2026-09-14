class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i,a in enumerate(nums):
            if a>0:
                break

            if i>0 and a==nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                s =a+nums[l]+nums[r]
                if s == 0:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res

                