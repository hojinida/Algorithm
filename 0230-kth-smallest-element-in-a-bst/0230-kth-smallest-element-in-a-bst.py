# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []
        def dfs(node):
            if not node:
                return

            heapq.heappush(q,node.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        return heapq.nsmallest(k, q)[-1]

            
        
        