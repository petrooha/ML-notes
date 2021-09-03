weight=[80.,85,200,85,69,65,68,66,85,72,85,82,65,105,75,80,
    70,74,72,70,80,60,80,75,80,78,63,88.65,90,89,91,1.00E+22,
    75,75,90,80,75,-1.00E+22,-1.00E+22,-1.00E+22,86.54,67,70,92,70,76,81,93,
    70,85,75,76,79,89,80,73.6,80,80,120,80,70,110,65,80,
    250,80,85,81,80,85,80,90,85,85,82,83,80,160,75,75,
    80,85,90,80,89,70,90,100,70,80,77,95,120,250,60]

def mean(data):
    return 1.0 * sum(data) / len(data)

def median(data):
    sd=sorted(data)
    if len(sd)%2==0:
        return (1.0*sd[len(sd)/2] + 1.0*sd[len(sd)/2 -1])/2
    else:
        return sd[len(sd)/2]

def variance(data):
    v=0
    m=mean(data)
    for e in data:
        v=v+(m-e)**2
    return v / len(data)

def stdev(data):
    return (variance(data))**0.5

def zscore(data, z):#doesnt produce z but the value with score z
    return z*stdev(data) + mean(data)

def quart(data):
    d=[]
    sd=sorted(data)
    if len(data)%4==0:
        for e in range(len(sd)/4 ,len(sd)*3/4):
            d.append(sd[e])
    else:
        for e in range(len(sd)/4 ,len(sd)*3/4 + 1):
            d.append(sd[e])
    return d
#this is Sebastian's way of calculating Quartiles (same result):
def quart2(data):
    d=[]
    sd=sorted(data)
    qb=(len(sd)-3)/4
    qe=qb*3+3
    for e in range(qb,qe):
        d.append(sd[e])
    return d

def calculate_weight(data, z):

    d = quart(data)
    return zscore(d, z)

def factor(l):
    return 1.96


def conf(l):
    return factor(l) * ((variance(l) / len(l))**.5)


def test(l, h):
    if h>(mean(l)+conf(l)) or h<(mean(l)-conf(l)):
        return False
    else:
        return True

age=[21,21,21,21,24,24,24,24,24,24,26,26,26,26,26,26,26,29,29,29,29,29,29,29,29,29,29,29,40,40]
