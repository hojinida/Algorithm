"""
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
"""


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        measure = 1
        for j in range(1, i//2+1):
            if i % j == 0:
                measure += 1
        if measure % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


# 아래 코드는 테스트 코드 입니다.
print(solution(13, 17))
# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
