import sys
sys.setrecursionlimit(10**7)

def solution(n, info):
    global best_diff, candidates
    best_diff = 0  
    candidates = []  
    
    def dfs(remain, lion_arrows, index):
        global best_diff, candidates
        if index == -1:
            lion_arrows[10] += remain  
            
            lion_score = 0
            apeach_score = 0
            
            for i in range(11):
                if lion_arrows[i] == 0 and info[i] == 0:
                    continue
                if lion_arrows[i] > info[i]:
                    lion_score += (10 - i)
                else:
                    apeach_score += (10 - i)
            diff = lion_score - apeach_score
            
            if diff > best_diff:
                best_diff = diff
                candidates = [lion_arrows[:]]
            elif diff == best_diff:
                candidates.append(lion_arrows[:])
                
            lion_arrows[10] -= remain  
            return
        
        dfs(remain, lion_arrows[:], index-1)
        
        arrows_needed = info[index] + 1
        if arrows_needed <= remain:
            new_arrows = lion_arrows[:]
            new_arrows[index] = arrows_needed
            dfs(remain - arrows_needed, new_arrows, index-1)
    
    dfs(n, [0]*11, 10)
    
    if best_diff <= 0:
        return [-1]
    
    candidates.sort(key=lambda arr: arr[::-1], reverse=True)
    return candidates[0]