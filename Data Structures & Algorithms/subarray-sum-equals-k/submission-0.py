class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {}
        current_sum = 0
        res = 0

        for i in nums:
            current_sum += i
            if current_sum == k:
                res += 1
            
            if current_sum - k in prefix_sums:
                res += prefix_sums[current_sum - k]
            
            if not current_sum in prefix_sums:
                prefix_sums[current_sum] = 1
            else:
                prefix_sums[current_sum] += 1
        
        return res
