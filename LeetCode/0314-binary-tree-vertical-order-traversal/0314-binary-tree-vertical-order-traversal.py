from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, col = queue.popleft()
            if col not in column_table:
                column_table[col] = []
            column_table[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        sorted_columns = sorted(column_table.items())
        
        return [val for col, val in sorted_columns]
        

        
        
