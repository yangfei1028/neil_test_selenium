#coding: utf-8

"""
@Author: Well
@Date: 2013-03-17
"""

# 习题39: 字典，可爱的字典_2

# 引入OrderedDict 保证按插入的顺序迭代输出
from collections import OrderedDict

# 字典例子
happy_bday1 = OrderedDict()
happy_bday1['1st'] = 'happy birthday to you'
happy_bday1['2nd'] = 'i don\'t want to get used'
happy_bday1['3rd'] = 'so i\'ll stop right there'

# 字典中查找元素
print happy_bday1['1st']
print happy_bday1['3rd']
print('')
print type(happy_bday1)
print('')
for key in happy_bday1:
    print key, happy_bday1[key]

# 判断key值是否在字典中
# has_key已淘汰
#print happy_bday1.has_key('happy')
print 'happy' in happy_bday1.keys()
print '2nd' in happy_bday1.keys()

#字典中添加元素
happy_bday1[1] = "add a line"
print happy_bday1
for key in sorted(happy_bday1.keys()):
    print key, happy_bday1[key]

# 字典中删除元素
print('')
del happy_bday1[1]
del happy_bday1['1st']
print happy_bday1


