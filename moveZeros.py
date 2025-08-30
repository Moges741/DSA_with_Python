class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker +=1
