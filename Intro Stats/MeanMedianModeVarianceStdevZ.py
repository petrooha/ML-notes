def mean(data):
    return 1.0 * sum(data) / len(data)

def median(data):
    sd=sorted(data)
    if len(sd)%2==0:
        return (1.0*sd[len(sd)/2] + 1.0*sd[len(sd)/2 -1])/2
    else:
        return sd[len(sd)/2]

def mode(data):
    m=data[0]
    c=data.count(data[0])
    for e in data:
        if data.count(e)>c:
            m=e
            c=data.count(e)
    if c==1:
        return False
    else:
        return m

def variance(data):
    v=0
    m=mean(data)
    for e in data:
        v=v+(m-e)**2
    return v / len(data)

def stdev(data):
    return (variance(data))**0.5

def zscore(n, data):
    return (n - mean(data)) / stdev(data)
