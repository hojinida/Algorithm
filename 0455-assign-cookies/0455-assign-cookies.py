class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        answer= 0
        for i in s:
            for j in g:
                if i >= j:
                    answer+=1
                    g.remove(j)
                    break
            if len(g) == 0:
                break
        
        return answer