from collections import deque
    
def solution(begin, target, words):
    visited = set()
    q = deque()
    q.append([begin,0])
    visited.add(begin)
    
    while q:
        p,result = q.popleft()
        if p == target:
            return result
        for word in words:
            if word not in visited:
                diff = 0
                t = list(p)
                for o,w in zip(p,word):
                    if w != o:
                        diff+=1
                    if diff > 1:
                        break
                if diff == 1:
                    visited.add(word)
                    q.append([word,result+1])
                    
    return 0