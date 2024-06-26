import heapq
from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        
        # 각 학생의 점수를 최소 힙에 저장하여 상위 5개만 유지
        for student, score in items:
            heapq.heappush(scores[student], score)
            if len(scores[student]) > 5:
                heapq.heappop(scores[student])
        
        # 최종 평균 계산 및 결과 정렬
        result = []
        for student, score_heap in scores.items():
            average_score = sum(score_heap) // 5
            result.append([student, average_score])
        
        result.sort(key=lambda x: x[0])
        return result
