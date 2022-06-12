"""
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
"""

from itertools import combinations
import math


def isFrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    nums = list(combinations(nums, 3))
    nums = [i + j + k for i, j, k in nums]
    result = 0
    for i in nums:
        if isFrime(i):
            result += 1
    return result


# 아래 코드는 테스트 코드 입니다.
print(solution([1, 5, 2, 6, 3, 7, 4]))
# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
