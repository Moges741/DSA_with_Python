class Solution:
    def partitionLabels(self, s: str):
        # Step 1: record last index of each char
        last = {c: i for i, c in enumerate(s)}
        
        res = []
        start = end = 0
        
        # Step 2: scan and cut partitions
        for i, c in enumerate(s):
            end = max(end, last[c])  # extend end to last occurrence
            if i == end:             # partition found
                res.append(end - start + 1)
                start = i + 1        # start new partition
                
        return res
