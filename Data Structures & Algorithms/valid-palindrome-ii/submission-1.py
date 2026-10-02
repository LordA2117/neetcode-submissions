class Solution:
    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1 
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i <= j:
            if s[i] != s[j]:
                return self.is_palindrome(s, i+1, j) or self.is_palindrome(s,i,j-1)
            i += 1
            j -= 1
        

        return True