import random



def reversal(cupTotle,selectCount):
    result = False #假定能全部口朝下的结果为假
    reversalCount = 0 #翻动次数
    cupList = [1] * cupTotle #建立杯子列表

    while result == False:

        #翻动n个杯子
        # 获取被翻动杯子的index
        indexList = random.sample(range(cupTotle),selectCount)

        #更新cupList
        for i in indexList:
            cupList[i] *= -1
            

        
        print(cupList) # 输出
        #计算cupList列表值
        sum = 0
        for k in cupList:
            sum += k


        reversalCount +=1 #计数器加1

        #如果和为0，则表示杯口全部朝下
        if sum == -1* cupTotle:
            result = True
            return result,reversalCount
        
        if reversalCount >100000:
             return result,reversalCount 






##执行入口7
def main():
    print("现在有m个杯子，杯口全部朝上，假定每次翻动n个杯子，最后能将杯口全部翻朝下吗？")
    cupTotle = int(input("请输入被子的数量m："))
    selectCount = int(input("请输入每次翻动杯子数量n："))
    tr = reversal(cupTotle,selectCount)

    print("尝试翻动",tr[1],"次后，结果为",tr[0])


main()


