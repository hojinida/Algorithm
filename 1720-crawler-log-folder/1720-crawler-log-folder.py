class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answer = 0

        for log in logs:
            if log == "../":
                if answer != 0 :
                    answer-=1
            elif "./":
                word = log.split("/")[0]
                if word == ".":
                    continue
                else:
                    answer+=1

        return answer