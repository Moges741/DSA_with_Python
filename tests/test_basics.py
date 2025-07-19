"""
Basic tests for DSA implementations
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from 01_arrays_strings.two_sum import two_sum_hash_map, two_sum_brute_force
from 02_linked_lists.linked_list_basics import LinkedList


def test_two_sum():
    """Test two sum implementations."""
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
    
    for nums, target, expected in test_cases:
        # Test hash map approach
        result1 = two_sum_hash_map(nums, target)
        assert result1 == expected, f"Hash map failed: {result1} != {expected}"
        
        # Test brute force approach
        result2 = two_sum_brute_force(nums, target)
        assert result2 == expected, f"Brute force failed: {result2} != {expected}"
    
    print("✅ Two Sum tests passed!")


def test_linked_list():
    """Test linked list implementation."""
    ll = LinkedList()
    
    # Test append
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]
    
    # Test prepend
    ll.prepend(0)
    assert ll.to_list() == [0, 1, 2, 3]
    
    # Test find
    assert ll.find(2) == 2
    assert ll.find(5) == -1
    
    # Test delete
    assert ll.delete(2) == True
    assert ll.to_list() == [0, 1, 3]
    
    # Test reverse
    ll.reverse()
    assert ll.to_list() == [3, 1, 0]
    
    print("✅ Linked List tests passed!")


def run_all_tests():
    """Run all tests."""
    print("🧪 Running DSA Tests...")
    print("-" * 30)
    
    try:
        test_two_sum()
        test_linked_list()
        
        print("\n🎉 All tests passed! Your implementations are working correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    run_all_tests()