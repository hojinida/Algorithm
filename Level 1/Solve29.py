"""
카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.

다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

입력 형식
"점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
예) 1S2D*3T

점수는 0에서 10 사이의 정수이다.
보너스는 S, D, T 중 하나이다.
옵선은 *이나 # 중 하나이며, 없을 수도 있다.
"""


def solution(dartResult):
    dartResult += " "
    mylist = list()
    s = ""
    answer = 0
    for i in dartResult:
        if i == "*" or i == "#":
            mylist.append(s + i)
            s = ""
        elif i == "S" or i == "D" or i == "T":
            mylist.append(int(s))
            s = i
        else:
            if s == "1" and i == '0':
                s = '10'
            elif s != "":
                mylist.append(s)
                s = ""
                s += i
            else:
                s += i
    temp = 0
    before = 0
    for i in mylist:
        if type(i) is int:
            temp = i
        elif i == 'S*':
            answer += before
            before = temp * 2
            answer += before
        elif i == 'D*':
            answer += before
            before = (temp ** 2) * 2
            answer += before
        elif i == 'T*':
            answer += before
            before = (temp ** 3) * 2
            answer += before
        elif i == 'S#':
            before = temp * -1
            answer += before
        elif i == 'D#':
            before = (temp ** 2) * -1
            answer += before
        elif i == 'T#':
            before = (temp ** 3) * -1
            answer += before
        elif i == 'S':
            before = temp
            answer += before
        elif i == 'D':
            before = (temp ** 2)
            answer += before
        elif i == 'T':
            before = (temp ** 3)
            answer += before

    return answer


"""
최적화 한 코드
import re
def solution(dartResult):
    bonus={'S':1,'D':2,'T':3}
    options={'':1,'*':2,'#':-1}
    
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i>0:
            dart[i-1]*=2
        dart[i]=int(dart[i][0])**bonus[dart[i][1]]*options[dart[i][2]]
    
    return sum(dart)
"""

# 아래 코드는 테스트 코드 입니다.
print(solution("1S*2T*3S"))

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
