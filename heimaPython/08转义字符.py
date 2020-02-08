print('hello')
print('world')

print('hello\nworld')
print('hello\tworld')

print('hell world' , end='\t')# 这里end默认值被替换掉了
print('hello python')


print('hell world' , end='+++')# 这里end默认值还可以被非转义字符替代
print('hello python')