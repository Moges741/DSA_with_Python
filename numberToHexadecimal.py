class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num = (1 << 32) + num  # Equivalent to num & 0xFFFFFFFF
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            digit = num & 0xF
            result.append(hex_chars[digit])
            num >>= 4
        
        return "".join(reversed(result))
