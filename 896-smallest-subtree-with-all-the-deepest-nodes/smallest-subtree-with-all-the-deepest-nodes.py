# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #  check for the deepest nodes
        store = defaultdict(int)

        def dfs(node, level):
            if not node:
                return

            store[node] = level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

            return 

        dfs(root, 0)

        deepest_nodes = set()
        maxim = 0
        for key, val in store.items():
            maxim = max(maxim, val)
        
        for key in store:
            if store[key] == maxim:
                deepest_nodes.add(key)
        
        count = len(deepest_nodes)
        flag = False
        sm = root
        def lca(node):
            nonlocal count, flag, sm
            
            if not node:
                return 0
            left = lca(node.left)
            right = lca(node.right)

            if left + right + (node in deepest_nodes) == count and not flag:
                flag = True
                sm = node
            
            return left + right + (node in deepest_nodes)
        
        lca(root)

        return sm





        