# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        def find(node, depth, ans):
            if node is None:
                return ans

            if depth == len(ans) :
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)

            find(node.left, depth + 1, ans) 
            find(node.right, depth + 1, ans)

            return ans

        
        ans = []
        find(root, 0, ans)

        return ans