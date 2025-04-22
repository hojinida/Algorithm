from itertools import permutations
def solution(user_id, banned_id):
    def is_match(u, b):
        if len(u) != len(b):
            return False
        for uc, bc in zip(u, b):
            if bc != '*' and uc != bc:
                return False
        return True

    result = set()
    m = len(banned_id)

    for perm in permutations(user_id, m):
        if all(is_match(perm[i], banned_id[i]) for i in range(m)):
            result.add(frozenset(perm))

    return len(result)
    
    