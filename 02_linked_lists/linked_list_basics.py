"""
Linked Lists - Foundation
=========================

A linked list is a linear data structure where elements are stored in nodes,
and each node contains data and a reference (link) to the next node.

Advantages:
- Dynamic size
- Efficient insertion/deletion at beginning (O(1))
- No memory waste

Disadvantages:
- No random access (O(n) to access element)
- Extra memory for pointers
- Not cache-friendly
"""

class ListNode:
    """Definition for a singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


class LinkedList:
    """Singly Linked List implementation with common operations."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """Add element to end of list. Time: O(n), Space: O(1)"""
        new_node = ListNode(val)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, val):
        """Add element to beginning of list. Time: O(1), Space: O(1)"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, val):
        """Insert element at specific index. Time: O(n), Space: O(1)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        
        # Navigate to position index-1
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, val):
        """Delete first occurrence of value. Time: O(n), Space: O(1)"""
        if not self.head:
            return False
        
        # If head needs to be deleted
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, val):
        """Find index of first occurrence. Time: O(n), Space: O(1)"""
        current = self.head
        index = 0
        
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, index):
        """Get element at specific index. Time: O(n), Space: O(1)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.val
    
    def reverse(self):
        """Reverse the linked list in-place. Time: O(n), Space: O(1)"""
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next  # Save next node
            current.next = prev       # Reverse the link
            prev = current           # Move prev forward
            current = next_temp      # Move current forward
        
        self.head = prev
    
    def to_list(self):
        """Convert to Python list for easy visualization."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if not self.head:
            return "Empty LinkedList"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.val))
            current = current.next
        
        return " -> ".join(result) + " -> None"


def demo_linked_list():
    """Demonstrate linked list operations."""
    print("🔗 LINKED LIST DEMO")
    print("=" * 40)
    
    # Create linked list
    ll = LinkedList()
    print(f"Initial list: {ll}")
    
    # Append elements
    print("\n📝 Appending elements: 1, 2, 3")
    for val in [1, 2, 3]:
        ll.append(val)
        print(f"After appending {val}: {ll}")
    
    # Prepend element
    print("\n📝 Prepending 0")
    ll.prepend(0)
    print(f"After prepending 0: {ll}")
    
    # Insert at index
    print("\n📝 Inserting 1.5 at index 2")
    ll.insert(2, 1.5)
    print(f"After insertion: {ll}")
    
    # Find element
    print("\n🔍 Finding elements:")
    for val in [0, 1.5, 5]:
        index = ll.find(val)
        if index != -1:
            print(f"Found {val} at index {index}")
        else:
            print(f"{val} not found")
    
    # Get element by index
    print("\n📖 Getting elements by index:")
    for i in range(len(ll)):
        print(f"Index {i}: {ll.get(i)}")
    
    # Delete element
    print("\n🗑️ Deleting element 1.5")
    success = ll.delete(1.5)
    print(f"Deletion successful: {success}")
    print(f"After deletion: {ll}")
    
    # Reverse list
    print("\n🔄 Reversing list")
    print(f"Before reverse: {ll}")
    ll.reverse()
    print(f"After reverse: {ll}")
    
    # Convert to Python list
    print(f"\n📋 As Python list: {ll.to_list()}")


def solve_common_problems():
    """Solve common linked list problems."""
    print("\n" + "=" * 50)
    print("🧩 COMMON LINKED LIST PROBLEMS")
    print("=" * 50)
    
    # Problem 1: Remove duplicates from sorted list
    def remove_duplicates(head):
        """Remove duplicates from sorted linked list."""
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
    # Problem 2: Find middle element
    def find_middle(head):
        """Find middle element using two pointers (tortoise and hare)."""
        if not head:
            return None
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.val
    
    # Problem 3: Detect cycle
    def has_cycle(head):
        """Detect if linked list has cycle using Floyd's algorithm."""
        if not head or not head.next:
            return False
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    # Test problems
    print("\n1️⃣ Remove Duplicates Test:")
    ll1 = LinkedList()
    for val in [1, 1, 2, 3, 3, 3, 4]:
        ll1.append(val)
    print(f"Before: {ll1}")
    remove_duplicates(ll1.head)
    print(f"After: {ll1}")
    
    print("\n2️⃣ Find Middle Test:")
    ll2 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll2.append(val)
    print(f"List: {ll2}")
    middle = find_middle(ll2.head)
    print(f"Middle element: {middle}")
    
    print("\n3️⃣ Cycle Detection Test:")
    ll3 = LinkedList()
    for val in [1, 2, 3, 4]:
        ll3.append(val)
    print(f"List: {ll3}")
    print(f"Has cycle: {has_cycle(ll3.head)}")
    
    # Create cycle for testing
    if ll3.head:
        current = ll3.head
        while current.next:
            current = current.next
        current.next = ll3.head.next  # Create cycle
    print(f"After creating cycle, has cycle: {has_cycle(ll3.head)}")


if __name__ == "__main__":
    # Run demo
    demo_linked_list()
    
    # Solve common problems
    solve_common_problems()


"""
🎯 KEY TAKEAWAYS:

1. LINKED LIST PATTERNS:
   - Two Pointers (slow/fast): Find middle, detect cycle
   - Dummy Node: Simplify edge cases in manipulation
   - Previous Pointer: Track previous node for deletion
   - Recursive: Many problems have elegant recursive solutions

2. COMMON TECHNIQUES:
   - Floyd's Cycle Detection (Tortoise and Hare)
   - Reverse in groups
   - Merge sorted lists
   - Convert to array for easier manipulation

3. TIME COMPLEXITIES:
   - Access: O(n)
   - Search: O(n)  
   - Insertion: O(1) at beginning, O(n) at end
   - Deletion: O(1) if you have reference to node

4. PRACTICE PROBLEMS:
   - Reverse Linked List
   - Merge Two Sorted Lists
   - Remove Nth Node From End
   - Add Two Numbers
   - Copy List with Random Pointer
"""