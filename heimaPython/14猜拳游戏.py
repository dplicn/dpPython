'''
需求
1,人和电脑各出一个数字
2,输出比较结果

步骤
1,输入,人输入,电脑随机生成
2,比较结果
3,输出结果

'''
import random

# 输入

humanNum = int(input('请输入(石头-1,剪子-2,布-3):'))
computerNum = random.randint(1,3)

# 计算
print(f'人类VS电脑,{humanNum}:{computerNum}')
if (humanNum > computerNum):
    print('人类赢了')
elif (humanNum < computerNum):
    print('电脑赢了')
elif( humanNum == computerNum):
    print('平局')