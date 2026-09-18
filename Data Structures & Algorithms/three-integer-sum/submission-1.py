class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            tgt = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == tgt:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                if nums[j] + nums[k] > tgt:
                    k -= 1

                if nums[j] + nums[k] < tgt:
                    j += 1

        res = [list(i) for i in res]

        return res
        