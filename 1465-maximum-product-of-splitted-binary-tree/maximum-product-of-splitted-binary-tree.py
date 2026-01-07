# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        left_sum = defaultdict(int)
        right_sum = defaultdict(int)
        total_sum = 0
        res = 0

        def dp(node):
            nonlocal total_sum
            if not node:
                return 0 
            
            left_sum[node] = dp(node.left)
            right_sum[node] = dp(node.right)

            total_sum += node.val

            return (left_sum[node] + right_sum[node] + node.val)
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            if node.left:
                curr = left_sum[node] * (total_sum - left_sum[node])
                res = max(curr, res)
                dfs(node.left)
            
            if node.right:
                curr = right_sum[node] * (total_sum - right_sum[node])
                res = max(curr, res)
                dfs(node.right)
        
        dp(root)
        dfs(root)

        return res % (10**9 + 7)