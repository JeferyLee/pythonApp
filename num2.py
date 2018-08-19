import numpy as np

#高维数组
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2d[0])
# [1 2 3]
#对各个元素进行访问
# print(arr2d[0][2])
# 3

arr3d=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3d)   #2*2*3数组
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

#arr3d[0]是一个2*3数组
# print(arr3d[0])

#标量值和数组都可以被赋值给arr3d[0]：
# arr3d[0]=42
# print(arr3d[0])
print(arr3d[1,0])   #返回一维数组

x=arr3d[1]
print(x)

print(x[0])

#切片索引

# print(arr2d)
# print(arr2d[:2])

# [[1 2 3]
#  [4 5 6]]
# print(arr2d[:2,1:])
# [[2 3]
#  [5 6]]

# 选取第二行的前两列
# print(arr2d[1,:2])

# 第三列的前两行
# print(arr2d[:2,2])

# 布尔型索引
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
# 满足正太分布的7*4随机数
data=np.random.randn(7,4)
# print(names)
print(data)
print(names=='Bob')
print(data[names=='Bob'])
# 打印出数组中对应的索引

# [ True False False  True False False False]
# [[-0.83740036 -0.47161077  1.19516211  2.05691645]
#  [-0.24220058 -0.50527018 -0.85056822 -0.57754072]]
# 布尔型数组的长度必须跟被索引的轴长度一致

# 通过~对条件进行否定：
# print(~(names=='Bob'))
# [False  True  True False  True  True  True]

# print(names=='Bob')
# [ True False False  True False False False]

# &与 ，|或
# mask=(names=='Bob')|(names=='Will')
# [ True False  True  True  True False False]
# print(mask)
# print(data[mask])

# 将data中所有负值都赋值为0.
data[data<0]=0
print(data)

# 花式索引