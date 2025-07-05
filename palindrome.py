class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        number = 0
        while x > number:
            number = number * 10 + x % 10
            x //= 10
        
        return x == number or x == number // 10
