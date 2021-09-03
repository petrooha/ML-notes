import random
def simulate(N):
    
    K = 0
    for e in range(1,N):
        c=random.randint(1,3)
        u=random.randint(1,3)
        if c!=u:
            K+=1

    return float(K) / float(N)

