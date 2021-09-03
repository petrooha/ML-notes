from __future__ import division
import numpy as np
from sklearn.preprocessing import MinMaxScaler
weights = np.array([[115], [140], [175]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print rescaled_weight
"""
SAME AS THIS

def featureScaling(arr):
    mn = min(arr)
    mx = max(arr)
    if mx - mn == 0:
        return None
    else:
        ans = list()
        for i in range(0, len(arr)):
            x= float((arr[i]-mn)/(mx-mn))
            ans.append(x)
    return ans, mn, mx, arr[1], (mx-mn), (arr[1] - mn)

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
"""
