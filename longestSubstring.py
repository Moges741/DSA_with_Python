class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            curr_char = s[i]
            if curr_char in seen and seen[curr_char] >= start:
                start = seen[curr_char] + 1
            
            seen[curr_char] = i  # Always update the current character's index
            max_len = max(max_len, i - start + 1)  # Calculate max after update

        return max_len
