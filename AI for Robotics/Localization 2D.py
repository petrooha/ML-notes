def sense(p, colors, measurement, sensor_right):
    aux=[[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    s=0.0
    for i in range(len(p)):
        for j in range(len(p[0])):
            if measurement == colors[i][j]:
                aux[i][j] = p[i][j]*sensor_right
            else:
                aux[i][j] = p[i][j]*(1.0 - sensor_right)
            s+=aux[i][j]
    for i in range(len(aux)):
        for j in range(len(aux[0])):
            aux[i][j] /= s
    return aux

def move(p, motion, p_move):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

    for i in range(len(p)):
        for j in range(len(p[0])):
            aux[i][j] = (p_move*p[(i - motion[0]) % len(p)][j - motion[1] % len(p[i])] + (1-p_move)*p[i][j])
    return aux


def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    norm = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[norm for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
    for k in range(len(measurements)):
        p= move(p, motions[k], p_move)
        p= sense(p, colors, measurements[k], sensor_right)
    
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')

#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
