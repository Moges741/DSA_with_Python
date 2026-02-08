# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Recursive approach
        if not root:
            return False
        
        # Check if current node is a leaf
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Subtract current node's value from targetSum and check children
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
