class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # all vowels
        s = list(s)  # convert string to list (mutable)
        left, right = 0, len(s) - 1

        while left < right:
            # Move left until we find a vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right until we find a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)  # convert list back to string
