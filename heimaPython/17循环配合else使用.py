
i = 0
while i<10:

    
    i+=1
    if(i%2==0):
        
        # continue
        break
    print(i)
else:
    print('exec else')

# 测试for
print('8'*8)
for i in range(10):
    if(i%2==0):
        # continue
        break
    print (i)
else:
    print('exec else')