class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = ""
        i = len(s) - 1 
        while i >= 0:  
            if s[i] == '#':    
                num = int(s[i-2:i])
                l += chr(num + 96)
                i -= 3
            else:
                num = int(s[i])
                l += chr(num + 96)
                i -= 1
        return l[::-1]



        
