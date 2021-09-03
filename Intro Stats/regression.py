def mean(data):
    return 1.0 * sum(data) / len(data)

def reg(x,y):
    xys=0
    xxs=0
    yys=0
    for e in range(0,len(x)):
        xys=xys+(x[e]-mean(x))*(y[e]-mean(y))
    for i in x:
        xxs=xxs+(i-mean(x))**2
    for j in y:
        yys=yys+(j-mean(y))**2

    return xys/((xxs*yys)**0.5)
# y=Bx + A find B:

def B(x,y):
    xys=0
    xxs=0
    yys=0
    for e in range(0,len(x)):
        xys=xys+(x[e]-mean(x))*(y[e]-mean(y))
    for i in x:
        xxs=xxs+((i-mean(x))**2)
    return xys/xxs

"""Zscore(x) = (x[i] - mean(x)) / stdev(x)
same for y
B / reg = stdev(y) / stdev(x)"""
