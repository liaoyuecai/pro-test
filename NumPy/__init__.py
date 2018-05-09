# -*- coding: utf-8 -*-
import numpy as np

# a = np.array([1, 2, 0], dtype=np.bool)
# print a
# [ True  True False]

# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print a['age']
# [10 20 30]

# student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])
# print student
# [('name', 'S20'), ('age', 'i1'), ('marks', '<f4')])

# student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])
# a = np.array([('abc',  21,  50),('xyz',  18,  75)], dtype = student)
# print a
# [('abc', 21, 50.) ('xyz', 18, 75.)]

# 这会调整数组大小
# a = np.array([[1, 2, 3], [4, 5, 6]])
# a.shape = (3, 2)
# print a
# a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape(3,2)
# print b


# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print  '我们的数组是：'
# print x
# print  '\n'
# # 切片
# z = x[1:4, 1:3]
# print  '切片之后，我们的数组变为：'
# print z
# print  '\n'
# # 对列使用高级索引
# y = x[1:4, [1, 2]]
# print  '对列使用高级索引来切片：'
# print y
#
# x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print  '我们的数组是：'
# print x
# print  '\n'
# # 现在我们会打印出大于 5 的元素
# print  '大于 5 的元素是：'
# print x[x >  5]


# a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
# b = np.array([1.0, 2.0, 3.0])
# print  '第一个数组：'
# print a
# print  '\n'
# print  '第二个数组：'
# print b
# print  '\n'
# print  '第一个数组加第二个数组：'
# print a + b
# a = np.array([[78, 34, 87, 25, 83], [25, 67, 97, 22, 13], [78, 43, 87, 45, 89]])
# print(a.max(axis=0))
# print(a.max(axis=1))

# import numpy as np
#
# a = np.arange(8).reshape(2, 2, 2)
#
# print '原数组：'
# print a
# print '\n'
# # 将轴 2 滚动到轴 0（宽度到深度）
#
# print '调用 rollaxis 函数：'
# print np.rollaxis(a, 2)
# # 将轴 0 滚动到轴 1：（宽度到高度）
# print '\n'
#
# print '调用 rollaxis 函数：'
# print np.rollaxis(a, 2, 1)
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

# 对 y 广播 x
b = np.broadcast(x, y)
# 它拥有 iterator 属性，基于自身组件的迭代器元组
print(b)
print '对 y 广播 x：'
r, c = b.iters
# print r.next(), c.next()
# print r.next(), c.next()
for i in r:
    print(i)
print('\n')
for i in c:
    print(i)
