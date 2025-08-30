class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n = len(skill)
        
        # Expected team skill (smallest + largest)
        target = skill[0] + skill[-1]
        chemistry_sum = 0
        
        left, right = 0, n - 1
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry_sum
