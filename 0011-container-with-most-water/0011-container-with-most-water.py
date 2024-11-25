class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0

        left = 0
        right = len(height)-1
        width = len(height)-1
        while left < right:
            water = width * min(height[left],height[right])
            answer = max(answer,water)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            
            width-=1
        
        return answer
        