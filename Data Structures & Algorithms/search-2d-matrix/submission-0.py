class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # Do a binary search on each row
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    left = mid + 1
                if row[mid] > target:
                    right = mid - 1
        return False
        