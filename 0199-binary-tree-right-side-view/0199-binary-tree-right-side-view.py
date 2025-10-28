# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
                    1
                2      3
             4   6    2   5
        
           
           [1, 3, 5, 3]
           
           
        '''
        if not root:
            return []
            
        result = []
        deq = deque([root])
        
        while deq:
            # result.append(deq[-1])
            
            length = len(deq)
            for i in range(length):
                node =  deq.popleft()
                
                if i == length - 1:
                    result.append(node.val)
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)   
                
            
        return result