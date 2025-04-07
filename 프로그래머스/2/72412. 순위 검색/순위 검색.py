import bisect

def solution(info, query):
    db = {}
    
    for record in info:
        tokens = record.split()
        lang, job, career, food = tokens[:4]
        score = int(tokens[4])
        
        keys = [lang, job, career, food]
        from itertools import product
        for mask in product([True, False], repeat=4):
            combo = []
            for i in range(4):
                combo.append(keys[i] if mask[i] else '-')
            combo_key = ' '.join(combo)
            
            if combo_key not in db:
                db[combo_key] = []
            db[combo_key].append(score)
    
    for k in db:
        db[k].sort()
    
    answer = []
    for q in query:
        parts = q.split(" and ")
        last = parts[-1].split()
        parts[-1] = last[0]
        threshold = int(last[1])
        combo_key = ' '.join(parts) 
        
        if combo_key in db:
            scores = db[combo_key]
            idx = bisect.bisect_left(scores, threshold)
            count = len(scores) - idx
        else:
            count = 0
        answer.append(count)
    
    return answer