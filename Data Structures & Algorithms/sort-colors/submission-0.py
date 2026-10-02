class Solution:
    def merge(self, arr, left, mid, right):
        n1 = mid-left+1
        n2 = right-mid
        arr1 = arr[left:left+n1]
        arr2 = arr[mid+1:mid+1+n2]
        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1
        # Merge the remaining elements
        while i < n1:
            arr[k] = arr1[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = arr2[j]
            j += 1
            k += 1
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # We're using merge sort
        currSize = 1
        n = len(nums)
        while currSize <= n-1:
            leftStart = 0
            while leftStart < n-1:
                mid = min(leftStart+currSize-1, n-1)
                rightEnd = min(leftStart+2*currSize-1, n-1)

                self.merge(nums, leftStart, mid, rightEnd)
                leftStart += 2*currSize
            currSize = 2*currSize
        