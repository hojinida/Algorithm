# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        class Data:
            def __init__(self, dia, hei):
                self.dia =dia
                self.hei = hei

        def cul(root: Optional[TreeNode]) -> Data:
            if not root:
                return Data(0,0)
            leftData = cul(root.left)
            rightData = cul(root.right)

            curDia = max(leftData.hei+rightData.hei,max(leftData.dia,rightData.dia))
            curHei = max(leftData.hei,rightData.hei)+1

            return Data(curDia,curHei)
        
        data= cul(root)

        return data.dia