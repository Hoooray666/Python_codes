from matplotlib import pyplot as plt
import numpy as np

x = range(2, 27, 2)
# print (x)

y = [15, 13, 5, 14, 17, 20, 25, 26, 26, 24, 22, 18, 15]
plt.plot(x, y)
plt.show()

a = np.array([1, 2, 3, 4, 5], ndmin=3)
print(a)
dt = np.dtype(np.int32)
print(dt)
dt = np.dtype('i4')
print(dt)
dt = np.dtype([('age', np.int64)])
print(dt)

student = np.dtype([('name', 'U20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a[...,0:])
print(a)
b = np.arange(24)
c = b.reshape(2,3,4)
d= np.array([[1,2,3],[4,5,6]])
print (d.shape)

x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z[0])

x =  (1,2,3)
a = np.asarray(x)
a = a.reshape(1,3)
print (a)

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print  ('这个数组的四个角元素是：')
print (y)

# s =  b'Hello World'
# a = np.frombuffer(s, dtype =  'S1')
# print (a)
# # b = np.frombuffer(b,'U1')

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  #全部行，列是从第二列开始左右
