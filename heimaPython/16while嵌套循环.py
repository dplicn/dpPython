'''
1,用星号打印正方形5x5
2,用星号打印三角形5x5
3,打印99乘法表

算法
1,输入,内层while输出横向的5个*,外侧while控制换行
'''
# 1,打印正方形

j = 0
while j<5:
    i = 0
    while i<5:
        print('*',end='')
        i += 1
    print('\n')
    j +=1

# 2,打印三角形
j = 0
while j<5:
    j +=1
    i = 0
    while i<j :
        print('*',end='')
        i+=1
    print('\n')

# 3,乘法表
'''
1x1=1
2x1=2   2x2=4
3x1=3   3x2=6   3x3=9
.......
竖向while输出行号
横向while输出行号依次乘以1~本身

'''
#行号
i =0
while i < 9:
    
    i +=1
    
    # 1~9序号
    j = 1
    while j <= i:
        print(f'{i}x{j}={i*j}',end='\t') 
        j +=1

    print('\n')