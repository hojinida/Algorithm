# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer = 0

        def cal(node):
            if not node:
                return
            
            if node.val >= low and node.val <= high:
                self.answer+=node.val
    
            if node.val >= low:
                cal(node.left)
    
            if node.val <=high:
                cal(node.right)
        
        cal(root)
        return self.answer