# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def find(node, minimum, maximum):
            if node is None:
                ans[0] = max(maximum - minimum, ans[0])
                return ans[0]

            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)

            left = find(node.left, minimum, maximum)
            right = find(node.right, minimum, maximum)

            return max(left, right)

        
        return find(root, root.val, root.val)

            


            