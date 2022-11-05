import numpy as np
a=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
b=np.where(a%2,a,0)
#print(b)
# x=np.array([[1,2,3],
#            [2,3,4],
#            [3,4,5]])
# y=np.array([10,20,30])
# print(x+y)
# print(a.shape)
# print(a.dtype)
# print(a.size)
aa=np.array([[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18]
            ])
aa=aa.reshape((2,9))
print(aa)