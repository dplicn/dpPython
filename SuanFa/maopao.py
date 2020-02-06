## 冒泡算法
## bubble sort
## 思路,每一次循环,让最小的数向气泡一样,走向左侧

def bigerToRight(arr):
    count = 0

    '''
    print("移动前>>i:0  ,j:0   移动前>>  arr:",arr)
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            count = count +1 
            if arr[i] > arr[j]: #用arr[i]与i后面的所有数比较,直接和arr[j]交换位子,j不一定紧挨着i
                arr[i],arr[j] = arr[j],arr[i]
            print("第 %d 次移动后>>i:%d  ,j:%d  "% (count,i,j) ,"移动后>>  arr:",arr)
    ## '''        

    ## 正确正确冒泡的方法
    ##'''
    print("移动前>>i:0  ,j:0   移动前>>  arr:",arr)
    for i in range(1,len(arr)):# 外侧循环,为什么是从1开始?因为
        for j in range(0,len(arr)-i):
            count = count +1 
            if arr[-1-j] < arr[-2-j]:
                arr[-2-j],arr[-1-j]  = arr[-1-j] , arr[-2-j] 
            print("第 %d 次移动后>>i:%d  ,j:%d  "% (count,i,j) ,"移动后>>  arr:",arr)
    ## '''

    
def main():
    while True:

        #输入一组数字,用英文逗号分割,回车结束
        arrString = input("输入一组数字,用英文逗号分割:")

        arrStr = arrString.split(",")

        ## 第一种把字符转成数字的方式
        # print(id(arr))
        arr = [int(n) for n in arrStr]
        # print(id(arr))
        ## 第二种把字符转成数字的方式
        # print(id(arr))
        # arr = list(map(int,arr))
        # print(id(arr))

        # print(arr)
        bigerToRight(arr)

main()