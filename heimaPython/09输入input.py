
'''
1,书写input,语法是input('提示信息')

2,观察input特点
2.1 input会中断程序,等待用户的输入
2.2 将输入信息存储到变量
2.3 输入信息被系统认为是字符串信息

'''

password = input('请输入密码:')

print(f'您输入的密码是:{password}\n类型是{type(password)}')

type(password)