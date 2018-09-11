import numpy as np

# 4.6伪随机数的生成
# numpy.random模块对Python内置的random进行了补充，
# 增加了一些用于高效生成多种概率分布的样本值的函数

samples=np.random.normal(size=(4,4))
print(samples)

from random import normalvariate
import time,timeit
N=10000
# %timeit samples=[normalvariate(0,1) for i in range(N)]
#  https://www.jianshu.com/p/20b6fb168824
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))