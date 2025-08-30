class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # pair the lightest with the heaviest
            right -= 1   # heaviest always goes
            boats += 1

        return boats
