from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

url='https://blog.csdn.net/g090909/article/details/50878066'
html=urlopen(url)
bsobj=BeautifulSoup(html,'lxml')
bs_div=bsobj.find('div',class_='markdown_views')
bs_text=bs_div.text.replace('\xa0'*8,'')
print(type(bs_text))
# with open('c:/users/jefery/desktop/abc.doc','w',encoding='utf-8')as f:
#     f.write(bs_text)
arr=np.array([[1.,2.,3.],[4.,5.,6.]])
# print(arr)
print(type(arr*arr))
arr2=np.array([[1,2,3],[4,5,6]])   #这两种写法都是可以的
# print(type(arr2*arr2))
# print(arr2==arr)

#基本的索引和切片

arr3=np.arange(10)
# print(arr3)
print(arr3[5:8])   #左闭右开
arr3[5:8]=1   #赋值
# print(arr3)
arr_slice=arr3[5:8]
# print(arr_slice)
arr_slice[1]=123
print(arr2[0])

