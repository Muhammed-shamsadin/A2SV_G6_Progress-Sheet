# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)

        smallest, maxim = 0, float('-inf')
        level = 1

        while queue:
            length = len(queue)
            cnt = 0

            for i in range(length):
                node = queue.popleft()
                cnt += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if maxim < cnt:
                maxim = cnt
                smallest = level

            level += 1
        
        return smallest 