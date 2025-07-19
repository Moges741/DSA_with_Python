"""
Problem: [Problem Title]
Difficulty: [Easy/Medium/Hard]
Source: [LeetCode/HackerRank/GeeksforGeeks/etc.]
URL: [Problem URL]

Problem Statement:
[Paste the problem statement here]

Examples:
Input: 
Output: 
Explanation: 

Constraints:
- 

Algorithm Approach:
[Describe your approach here]

Time Complexity: O()
Space Complexity: O()
"""

def solution(input_param):
    """
    Args:
        input_param: Description of input parameter
    
    Returns:
        Return type: Description of return value
    """
    # Step 1: Handle edge cases
    if not input_param:
        return []  # or appropriate default
    
    # Step 2: Initialize variables
    
    # Step 3: Main logic
    
    # Step 4: Return result
    pass


def test_solution():
    """Test cases for the solution"""
    # Test case 1: Basic case
    assert solution([]) == []
    
    # Test case 2: Edge case
    assert solution([1]) == [1]
    
    # Test case 3: Normal case
    # assert solution([input]) == expected_output
    
    print("All test cases passed!")


if __name__ == "__main__":
    # Run tests
    test_solution()
    
    # Example usage
    example_input = []
    result = solution(example_input)
    print(f"Input: {example_input}")
    print(f"Output: {result}")


"""
PROBLEM-SOLVING CHECKLIST:

□ Read problem carefully and understand requirements
□ Identify input/output types and constraints
□ Think of edge cases (empty input, single element, etc.)
□ Start with brute force approach
□ Optimize if needed
□ Trace through examples
□ Consider time/space complexity
□ Write clean, readable code
□ Test with multiple examples
□ Think of alternative approaches

COMMON PATTERNS TO CONSIDER:
- Two pointers
- Sliding window
- Hash map for O(1) lookup
- Sorting for easier processing
- Binary search for O(log n)
- Dynamic programming for optimization
- Recursion with memoization
- Greedy approach
- Graph traversal (DFS/BFS)
"""