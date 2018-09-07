# 4.3 利用数组进行数据分析

# NumPy数组使你可以将许多种数据处理任务表述为简洁的数组表达式（否则需要编写循环）。用数组表达式代替循环的做法，通常被称为矢量化。
# 一般来说，矢量化数组运算要比等价的纯Python方式快上一两个数量级（甚至更多），尤其是各种数值计算。
#
#
# 作者：SeanCheney
# 链接：https://www.jianshu.com/p/a380222a3292
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

import numpy as np
points=np.arange(-5,5,0.1)
# print(points)

xs,ys=np.meshgrid(points,points)
# print(ys)
z=np.sqrt(xs**2+ys**2)
# print(z)

import matplotlib.pyplot as plt
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.title('matplotlib demo')
# plt.show()

# 将条件逻辑表述为数组运算
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])

result=[(x if c else y)
        for x,y,c in zip(xarr,yarr,cond)]
# print(result)
# 这种处理方式速度比较慢，且无法用于多为数组。
# 更加具有效率的方式是使用np.where
result=np.where(cond,xarr,yarr)
print(result)
arr=np.random.randn(4,4)
# print(arr)

# print(arr>0)
# print(np.where(arr>0,2,-2))
# 使用np.where,可以将标量和数组结合起来。

# 数学和统计方法
# sum、mean以及标准差std等聚合计算（aggregation，通常叫做约简（reduction））
# 既可以当做数组的实例方法调用，也可以当做顶级NumPy函数使用。
arr=np.random.randn(5,4)
# print(arr)
# print(arr.mean())
# print(arr.sum())

# mean和sum这类的函数可以接受一个axis选项参数，
# 用于计算该轴向上的统计值，最终结果是一个少一维的数组：
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.size(arr))
# print(arr.mean(1))   计算行的平均值
# print(arr.sum(0))  计算每列的和
# 在多维数组中，累加函数（如cumsum）返回的是同样大小的数组，
# 但是会根据每个低维的切片沿着标记轴计算部分聚类：

# print(arr.cumsum(axis=0))

#用于布尔型数组的方法
arr=np.random.randn(10)
# print(arr)
# print((arr>0).sum())
# any用于测试数组中是否存在一个或多个True，
# 而all则检查数组中所有值是否都是True.

# 排序
# NumPy数组也可以通过sort方法就地排序.
arr=np.random.randn(6)
c=arr
# print(c)
# print(sorted(c))
arr=np.random.randn(5,3)
# print(arr)
# print(arr.sort(axis=1))

large_arr=np.random.randn(100)
# print(sorted(large_arr))
# print(large_arr[int(0.05*len(large_arr))])
# np.unique()函数用于找出数组中的唯一值并返回已排序的结果.
names=np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

# np.in1d()函数得到一个“X的元素是否包含于Y”的布尔型数组
values=np.array([1,2,3,4,5,6])
arr1=[2,3,5]
# print(np.in1d(values,arr1))

# 4.5线性代数
x=np.array([[1., 2., 3.], [4., 5., 6.]])
y=np.array([[6., 23.], [-1, 7], [8, 9]])
# print(x.dot(y))
# x.dot(y)等价于np.dot(x, y)：
# dot 矩阵乘法
#  diag以一维数组的形式返回仿真的对角线元素，或将一维数组
# 转换为方阵
#  trace 计算对角线元素的和
#  det 计算矩阵行列式
#  eig 计算方阵的特征值和特征向量
#  inv   计算方阵的逆
# https://www.jianshu.com/p/a380222a3292

