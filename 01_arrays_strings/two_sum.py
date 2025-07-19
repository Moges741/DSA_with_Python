"""
Problem: Two Sum
Difficulty: Easy
Source: LeetCode
URL: https://leetcode.com/problems/two-sum/

Problem Statement:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

def two_sum_brute_force(nums, target):
    """
    Brute Force Approach
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash_map(nums, target):
    """
    Hash Map Approach (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Algorithm:
    1. Create a hash map to store value -> index mapping
    2. For each number, calculate complement = target - num
    3. If complement exists in hash map, return indices
    4. Otherwise, add current number to hash map
    """
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in hash map
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Add current number to hash map
        num_to_index[num] = i
    
    return []


def two_sum_sorted(nums, target):
    """
    Two Pointers Approach (only if array can be sorted)
    Time Complexity: O(n log n)
    Space Complexity: O(n) for storing original indices
    
    Note: This approach changes the array order, so we need to track original indices
    """
    # Create array of (value, original_index) pairs
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    # Sort by value
    indexed_nums.sort()
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


def test_two_sum():
    """Test all approaches with multiple test cases"""
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 2, 3, 4, 5], 8, [2, 4])
    ]
    
    approaches = [
        ("Brute Force", two_sum_brute_force),
        ("Hash Map", two_sum_hash_map),
        ("Two Pointers", two_sum_sorted)
    ]
    
    for approach_name, func in approaches:
        print(f"\nTesting {approach_name} approach:")
        for nums, target, expected in test_cases:
            result = func(nums.copy(), target)  # Use copy to avoid modifying original
            status = "✅" if result == expected else "❌"
            print(f"{status} nums={nums}, target={target} -> {result}")
    
    print("\nAll test cases completed!")


if __name__ == "__main__":
    # Run tests
    test_two_sum()
    
    # Interactive example
    print("\n" + "="*50)
    print("INTERACTIVE EXAMPLE")
    print("="*50)
    
    nums = [2, 7, 11, 15]
    target = 9
    
    print(f"Input: nums = {nums}, target = {target}")
    
    # Compare all approaches
    result1 = two_sum_brute_force(nums, target)
    result2 = two_sum_hash_map(nums, target)
    result3 = two_sum_sorted(nums.copy(), target)
    
    print(f"Brute Force Result: {result1}")
    print(f"Hash Map Result: {result2}")
    print(f"Two Pointers Result: {result3}")
    
    print(f"\nVerification: nums[{result2[0]}] + nums[{result2[1]}] = {nums[result2[0]]} + {nums[result2[1]]} = {nums[result2[0]] + nums[result2[1]]}")


"""
LEARNING NOTES:

1. PATTERN RECOGNITION:
   - This is a classic "find pair with sum" problem
   - Hash map trades space for time (common optimization)
   - Two pointers work when array can be sorted

2. APPROACH COMPARISON:
   - Brute Force: Simple but inefficient O(n²)
   - Hash Map: Optimal for unsorted array O(n)
   - Two Pointers: Good for sorted array O(n log n)

3. KEY INSIGHTS:
   - Hash map stores "what we've seen" for O(1) lookup
   - Complement = target - current_number
   - Always consider space-time tradeoffs

4. VARIATIONS TO PRACTICE:
   - Two Sum II (sorted array)
   - Two Sum III (design data structure)
   - 3Sum, 4Sum
   - Two Sum BST
"""