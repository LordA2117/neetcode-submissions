class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        string = s.replace(" ", "").lower()
        string = re.sub('[^0-9a-zA-Z]+', '', string).lower()
        #rint(string)
        return string == string[::-1]
        