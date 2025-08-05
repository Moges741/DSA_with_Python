class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i] and j != i:
                    count += 1
            result.append(count)
        
        return result
