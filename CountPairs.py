class Solution:
    def similarPairs(self, words: List[str]) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        for word in words:
            # Normalize the word by sorting and taking unique characters
            normalized = ''.join(sorted(set(word)))
            count[normalized] += 1
        
        total_pairs = 0
        for c in count.values():
            if c >= 2:
                total_pairs += c * (c - 1) // 2
        
        return total_pairs
