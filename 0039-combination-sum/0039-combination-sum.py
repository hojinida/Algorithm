class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(current,start,target):
            if target == 0:
                result.append(list(current))
                return
            if target < 0:
                return 
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                current.append(candidates[i])
                back(current, i, target - candidates[i])
                current.pop()

        result = []
        candidates.sort()
        back([], 0, target)
        return result
                
            
                