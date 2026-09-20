class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            k_candidate = left + (right - left) // 2
            # Find the total hours
            tot_hours = 0
            for i in piles:
                tot_hours += (i + k_candidate - 1) // k_candidate

            # If this is bigger than h, it is too slow, so discard the left half entirely
            if tot_hours > h:
                left = k_candidate + 1
            else:
                right = k_candidate - 1

        return left
        