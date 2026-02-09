class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        
        while x_abs > 0:
            digit = x_abs % 10
            x_abs //= 10
            
            if rev > (INT_MAX - digit) // 10:
                return 0
            
            rev = rev * 10 + digit
        
        return rev * sign
