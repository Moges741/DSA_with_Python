class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        i = 1
        n = len(piles)
        while i < n:
            res += piles[i]
            i += 2
            n -= 1
        return res
#that's good
