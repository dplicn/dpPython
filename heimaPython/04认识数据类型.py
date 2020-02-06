'''
1,不同的变量存储不同的数据类型
2,验证这些数据类型 -- type()
'''

# 数字型
# int -- 整型
num1 = 1
# float -- 浮点型
num2 = 1.1

# str -- 字符型

s = 'python'

# bool 布尔型
b = True

# list 列表型
l1 = [1,2,3]

# tuple
t = (1,2,3)

# dict 字典
d = {'宗小程':14,'刘荞':12}

#set 集合--数据唯一性,不重合

s1 = set([3,4,5,4,5,6])
print(s1)
print(type(s1))