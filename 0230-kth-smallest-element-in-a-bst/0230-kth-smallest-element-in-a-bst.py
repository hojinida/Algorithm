# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        currunt = root
        while True:
            while currunt:
                stack.append(currunt)
                currunt = currunt.left
            
            currunt = stack.pop()
            k-=1

            if k == 0:
                return currunt.val
            
            currunt = currunt.right
        
        