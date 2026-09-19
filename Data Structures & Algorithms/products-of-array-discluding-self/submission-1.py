class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        # Left pass
        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        
        # Right pass
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
        