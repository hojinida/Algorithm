class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pattern = {i:1 for i in nums}
        
        answer = []

        for i in nums:
            result = 1
            if pattern[i] == 1:
                pattern[i] = 0
                left = i-1
                right = i+1
                while left in pattern or right in pattern:
                    if left in pattern:
                        result+=1
                        pattern[left] = 0
                        left-=1
                    if right in pattern:
                        result +=1
                        pattern[right] = 0
                        right+=1
                answer.append(result)

        return max(answer) if answer else 0
                

            

            
