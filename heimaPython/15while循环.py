'''
需求:1-100累加

算法:
输入:自动从1到100
处理:每次结果都加上新的数
输出:输出最终结果
'''

i = 100

result = 0

while i>0:
    print('执行循环')
    if (i%5 == 0):
        
        continue
    print(i)
    result +=i
    i-=1

print (f'i={i},result={result}')