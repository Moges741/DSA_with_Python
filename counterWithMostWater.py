class Solution:
    def maxArea(self, height: List[int]) -> int:
        right, left = len(height) - 1, 0
        maxarea = 0
        while right > left:
            heigh = min(height[right], height[left])
            width = right - left

            area = heigh * width

            maxarea = max(area, maxarea)
            
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return maxarea

