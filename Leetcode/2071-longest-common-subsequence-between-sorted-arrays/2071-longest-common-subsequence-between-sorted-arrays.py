class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        answer = arrays[0]
        for arr in arrays[1:]:
            i = 0
            j = 0
            n = len(answer)
            m = len(arr)
            temp = []
            while i<n and j<m:
                if answer[i] == arr[j]:
                    temp.append(answer[i])
                    i+=1
                    j+=1
                elif answer[i] < arr[j]:
                    i+=1
                else:
                    j+=1
            answer = temp

        return answer