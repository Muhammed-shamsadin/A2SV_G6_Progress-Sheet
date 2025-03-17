# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # let us create a 2 function one that check for the left side and other for the right side
        
        def leftSide(node):
            if node is None:
                return
            left = leftSide(node.left)
            right = leftSide(node.right)

            return node.val, left, right
        
        def rightSide(node):
            if node is None:
                return

            right = rightSide(node.right)
            left = rightSide(node.left)

            return node.val, right, left  

        # use both functions at the same time and check for every iteration or node if they 
        # are similar or not.

        return leftSide(root.left) == rightSide(root.right)
