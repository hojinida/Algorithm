from collections import deque
def solution(plans):
    def transferTime(time):
        hour,mit = time.split(":")
        return int(hour)*60 + int(mit)
    
    answer = []
    plans = sorted(plans,key = lambda x:x[1])
    plans = deque(plans)
    stack = []
    
    while plans:
        plan = plans.popleft()
        job,cur_time,solve_time = plan[0],transferTime(plan[1]),plan[2]
        
        if not stack:
            stack.append([job,cur_time,int(solve_time)])
            continue
        else:
            job_time=cur_time-stack[-1][1]
            while stack and job_time > 0:
                if stack[-1][2] <= job_time:
                    job_time -= stack[-1][2]
                    answer.append(stack.pop()[0])
                else:
                    stack[-1][2] -= job_time
                    job_time = 0
                    
        stack.append([job,cur_time,int(solve_time)])
        
    while stack:
        answer.append(stack.pop()[0])
    return answer