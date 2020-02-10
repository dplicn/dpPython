# 1,定义洗衣机类


class XiYiJi():
    '''洗衣机类'''
    def xiYiFu(self):
        '''洗衣服'''
        print("洗衣服")
    def tuoShui(self):
        '''脱水'''
        print('脱水')
    def piaoXi(self):
        pass
# 2,创建洗衣机

haier = XiYiJi()

# 3,验证洗衣机功能

haier.xiYiFu()
haier.width = 100

print(haier.width)