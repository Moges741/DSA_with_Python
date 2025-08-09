class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []

        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                result.append(i)
        return result


