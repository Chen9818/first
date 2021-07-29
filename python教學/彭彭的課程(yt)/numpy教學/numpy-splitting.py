import numpy as np
arr=np.array([
    [2,4,6,8,10,12],
    [1,3,5,7,9,11]
])    #2x6


#根據第一個維度切割
data=np.vsplit(arr,2)
print(data)
'''
1x6
    [[2,4,6,8,10,12]]
1x6
    [[1,3,5,7,9,11]]
'''


#根據第二個維度切割
data=np.hsplit(arr,2)
print(data)
'''
2x3
    [
        [2,4,6]
        [1,3,5]    
    ]
2x3
[
        [8,10,12]
        [7,9,11]    
    ]
'''

#根據第二個維度切割成3個陣列
data=np.hsplit(arr,3)
print(data)
'''
2x2
    [[2,4],[1,3]]
2x2
    [[6,8],[5,7]]
2x2
    [[10,12],[9,11]]
'''

