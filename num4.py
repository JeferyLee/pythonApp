import numpy as np

# 4.6伪随机数的生成
# numpy.random模块对Python内置的random进行了补充，
# 增加了一些用于高效生成多种概率分布的样本值的函数

samples=np.random.normal(size=(4,4))
# print(samples)

from random import normalvariate
import time,timeit
N=10000
# %timeit samples=[normalvariate(0,1) for i in range(N)]
#  https://www.jianshu.com/p/20b6fb168824

# 4.7 实例：随机漫步
import random
import  matplotlib.pyplot as plt
plt.title('random walk')
position=0
walk=[position]
steps=1000
for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)
# plt.plot(walk[:100])
# plt.show()

nsteps=10000
draws=np.random.randint(0,2,size=nsteps)  #随机产生0，1.
steps=np.where(draws>0,1,-1)
print('----------')
walk=steps.cumsum()
# print(walk.min())
# print(walk.max())
# 随机漫步过程中第一次到达某个特定值的时间
# 用argmax返回的是该布尔型数组第一个最大值的索引
# print((np.abs(walk)>=10).argmax())
# print(np.random.rand(10))
print(random.randint(0,1))
steps=10
for i in range(steps):
    c=random.randint(0,1)
    # print('c=%d'%c)
    # print('--------')
    step=1 if c else -1
    # print(step)

import random
import matplotlib.pyplot as plt

position=0
walk=[position]
print(walk)
steps=1000
for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)

plt.plot(walk[:500])
plt.title('random walk')
# plt.show()

nwalks=10
nsteps=5
draws=np.random.randint(0,2,size=(nwalks,nsteps))
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1)
print(walks)
hits3=(np.abs(walks)>=3).any(1)   #计算达到3的最小穿越时间。使用any函数统计所有的值。
print(hits3)
