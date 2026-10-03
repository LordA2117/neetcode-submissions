class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = j+1
                l = len(nums)-1
                while k < l:
                    curr_sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if curr_sum == target:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        l -= 1
                        k += 1
                        continue
                    
                    if curr_sum < target:
                        k += 1
                        continue
                    
                    if curr_sum > target:
                        l -= 1
                        continue
        
        res = [list(i) for i in res]
        return res
                    

        