class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        palindrome = str(x)
        if palindrome == palindrome[::-1]:
            return True
        
        return False 