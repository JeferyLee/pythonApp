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
# print(data)
# print(names=='Bob')
# print(data[names=='Bob'])
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
# print(data)

# 花式索引
arr=np.empty((8,4))
print('----------------')
for i in range(8):
    arr[i]=i
print(arr[[1]])
# 一次传入多个索引数组会有一点特别。它返回的是一个一维数组，其中的元素对应各个索引元组
# arr=np.arange(32).reshape(8,4)
# print(arr)
# print('---------')
# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

# 数组转置和轴对换
arr=np.arange(15).reshape(3,5)
print(arr)
print(arr.T)
arr=np.random.randn(6,3)

# 4.2 通用函数：快速的元素级数组函数
# 通用函数（即ufunc）是一种对ndarray中的数据执行元素级运算的函数。你可以将其看做简单函数
# （接受一个或多个标量值，并产生一个或多个标量值）的矢量化包装器。

# arr=np.arange(10)
# print(arr)
# print(np.sqrt(arr))

arr=np.random.randn(7)*5
print(arr)
remainder,whole_part=np.modf(arr)
print('abc')
print(remainder)
print(whole_part)   #modf()函数返回数组的小数和整数部分。

