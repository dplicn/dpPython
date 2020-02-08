'''
1,准备数据
2,输出
'''

age = 18
weight = 62.5
name = '小明'
stu_id = 1
# 1,我的年龄是x岁

print('我的年龄是%d岁' % age)

# 2,我的名字叫x
print('我的名字叫%s' % name)

# 3,我的体重是x公斤
print('我的体重是%.2f公斤' % weight)

# 4 我的学号是001
print('我的学号是%3d' % stu_id) # 试试看将0换成其他数字或者去掉

# 5 我叫x,我的今年x岁,我的体重是x公斤
print('5 我叫%s,我的今年%s岁,我的体重是%s公斤' % (name,age,weight))
print(f'5 我叫{name},我的今年{age}岁,我的体重是{weight}公斤')
print(f'6 我叫{name},我的姐姐今年{age+1}岁,她的体重是{weight-2.333}公斤')