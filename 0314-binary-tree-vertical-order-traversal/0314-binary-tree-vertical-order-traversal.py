from collections import deque
from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}

        q = deque([(root,0)])
        while q:
            p = q.popleft()
            if not p[0]:
                break
                
            if p[1] not in result:
                result[p[1]] = []
            result[p[1]].append(p[0].val)

            if p[0].left:
                q.append((p[0].left,p[1]-1))
            if p[0].right:
                q.append((p[0].right,p[1]+1))
        result = OrderedDict(sorted(result.items()))

        answer = []
        for key,value in result.items():
            answer.append(value)

        return answer

        

        
        
