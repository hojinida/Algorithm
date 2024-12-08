from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr = Counter(arr)

        for i in target:
            if i not in arr:
                return False
            else:
                arr[i]-=1
                if arr[i] == 0:
                    del(arr[i])
        return True