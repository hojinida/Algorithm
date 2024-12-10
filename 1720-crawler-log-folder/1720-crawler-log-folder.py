class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answer = 0
        for log in logs:
            if log == "../":
                answer = max(answer - 1, 0)
            elif log != "./":
                answer += 1
        return answer