#Given the list motions=[1,1] which means the robot 
#moves right and then right again, compute the posterior 
#distribution if the robot first senses red, then moves 
#right one, then senses green, then moves right again, 
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
""" OR:
        if world[i] == Z:
            q.append(p[i]*pHit)
        else:
            q.append(p[i]*pMiss)"""
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        v = p[(i-U)%len(p)]*pExact + p[(i-U-1)%len(p)]*pOvershoot + p[(i-U+1)%len(p)]*pUndershoot
        q.append(v)
    return q


for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])
print p   
