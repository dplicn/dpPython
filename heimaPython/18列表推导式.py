'''
列表推导式
1,由for循环创建的列表
2,由列表推导式创建的列表
3,带if的列表推导式
4,多for推导式 实现[(1,0),(1,1),(1,2),(2,0),(,2,1),(2,2)]
'''
# 1,由for循环创建的列表
# l1 = []
# for i in range(10):
#     l1.append(i)
# print(l1)

# 2,由列表推导式创建的列表
# l1 = [i for i in range(10)]
# print(l1)
# 3,带if的列表推导式
l1 = []
# for i in range(10):
#     if(i%2==0):
#         l1.append(i)
# print(l1)

# l1 = [i for i in range(10) if i%2==0]
# print(l1)

# 4,多for推导式 实现[(1,0),(1,1),(1,2),(2,0),(,2,1),(2,2)]
# l1 = []
# for i in range(1,3):
#     for j in range(3):
#         l1.append((i,j))
    
# print(l1)


l1 = [(i,j) for i in range(1,3) for j in range(3)]
print(l1)

d = {}
