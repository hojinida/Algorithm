class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        pattern = {}
        items.sort(key=lambda x:x[1],reverse = True)
        
        for student, score in items:
            if student in pattern:
                if pattern[student][1] ==5:
                    continue
                pattern[student][0] += score
                pattern[student][1] += 1
            else:
                pattern[student] = [score,1]
       
        answer = []
        for student, score in pattern.items():
            answer.append([student,score[0]//score[1]])

        answer.sort(key = lambda x:x[0])
        return answer