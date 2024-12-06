class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        index = 0
        num = 1
        while count != k:
            if index >= len(arr):
                num+=1
                count+=1
            else:
                if arr[index] > num:
                    num+=1
                    count+=1
                elif arr[index] == num:
                    index+=1
                    num+=1
                else:
                    index+=1
        
        return num-1
                