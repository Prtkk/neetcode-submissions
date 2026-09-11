class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1]*(len(nums))

        preprod = 1
        for i in range(len(nums)):
            prods[i] = preprod
            preprod *= nums[i]
        postprod = 1
        for i in range(len(nums)-1,-1,-1):
            prods[i] *= postprod
            postprod *= nums[i]

        return prods