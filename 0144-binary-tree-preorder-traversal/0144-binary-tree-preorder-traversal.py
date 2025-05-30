# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # use Recursion
        # preorderTraversal -> PLR
        if root == None:
            return []
        parent = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return parent + left + right
