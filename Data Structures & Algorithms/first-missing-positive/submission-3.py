class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1

        max_num = max(nums)
        
        for i in range(1, max_num+2):
            if i not in nums:
                res = i
                break
        return res
