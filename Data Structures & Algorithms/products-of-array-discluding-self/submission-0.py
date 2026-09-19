class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        else:
            i = 0
            while i < len(nums):
                if nums[i] == 0:
                    i += 1
                    continue
                else:
                    product *= nums[i]
                i += 1
            i = 0
            while i < len(nums):
                if zero_count == 1:
                    ans = [0] * len(nums)
                    ans[nums.index(0)] = product
                    break
                else:
                    ans.append(int(product / nums[i]))
                i += 1
        return ans
        