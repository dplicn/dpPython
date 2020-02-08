# int > float
num1 = 1
num2 = float(num1)
print('int > float:',num2,type(num2))

#eval() 计算字符串内的表达式，并返回对象

str1 = '1.1'
str2 = '1'

str3 = '(1,2,3)'
e1 = eval(str1)
e3 = eval(str3)
print(type(e3),e3)

 