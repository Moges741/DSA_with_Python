class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i, j = 0, 0
        
        while i < len(word1) and j < len(word2):
            # Compare the remaining substrings
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        
        # Append leftovers
        merge.append(word1[i:])
        merge.append(word2[j:])
        
        return "".join(merge)


# Example
sol = Solution()
print(sol.largestMerge("cabaa", "bcaaa"))  # Output: "cbcabaaaaa"
