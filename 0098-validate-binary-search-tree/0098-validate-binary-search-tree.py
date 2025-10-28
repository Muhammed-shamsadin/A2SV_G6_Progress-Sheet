# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        
        def validate(node):
            nonlocal prev
            
            if not node:
                return True
            
            if not validate(node.left):
                return False
            if prev and prev.val >= node.val:
                return False
            
            prev = node
                
            if not validate(node.right):
                return False
            
            return True
        
        return validate(root)