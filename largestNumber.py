class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Turn numbers into strings
        nums = list(map(str, nums))
        
        # Step 2: Sort them so the "biggest looking" combo comes first
        nums.sort(key=lambda x: x*10, reverse=True)
        
        # Step 3: Join them into one big number
        result = ''.join(nums)
        
        # Step 4: Handle the case where it’s all zeros
        return '0' if result[0] == '0' else result
