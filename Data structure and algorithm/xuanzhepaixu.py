##选择排序就是重复”从待排序的数据中寻找最小值，将其与序列最左边的数字进行交换“这一操作的算法。在序列中寻找最小值时使用的是线性查找。

def selectSort(arr):

    for i in range(len(arr)):
        