# 流畅的python

## 第一章 python数据模型

### 1.1 一摞python风格的纸牌

+ 用一个非常简单的例子来实现"特殊方法" `__getitem__` 和 `__len__`

+ 迭代 就是 `for...in...`

+ Python 语言参考手册中的“Data Model”（https://docs.python.org/3/reference/datamodel.html）一章列 出了 83 个特殊方法的名字，其中 47 个用于实现算术运算、位运算和比较操作。

## 第二章 序列构成的数组

### 2.1 内置序列类型概览

+ > 容器序列

`list`,`tuple` 和 `collections.deque` 这些序列能存放不同类型的数据.

+ > 扁平序列

`str`,`bytes`,`bytearray`,`memoryview` 和 `array.array`,这类序列只能容纳一种类型.

+ > 容器序列存放的是它们所包含的任意类型的对象的引用，而扁平序列里存放的是值 而不是引用。换句话说，扁平序列其实是一段连续的内存空间。由此可见扁平序列 其实更加紧凑，但是它里面只能存放诸如字符、字节和数值这种基础类型

> 序列类型还能按照能否被修改来分类。 

+ 可变序列`list`、`bytearray`、`array.array`、`collections.deque` 和 memoryview。 

+ 不可变序列 `tuple`、`str` 和 `bytes`。

### 2.2 列表推导和生成器表达式

#### 2.2.1 列表推导和可读性

> 把一个字符串变成 Unicode 码位的列表

+ 常规写法

```
>>> symbols = '$¢£¥€¤' 
>>> codes = [] 
>>> for symbol in symbols: 
        codes.append(ord(symbol))

>>> codes 
[36, 162, 163, 165, 8364, 164]
```
+ 另一种写法

```
>>> symbols = '$¢£¥€¤' 
>>> codes = [ord(symbol) for symbol in symbols] 

>>> codes 
[36, 162, 163, 165, 8364, 164]
```
> 通常的原则是，只用列表推导来创建新的列表，并且尽 量保持简短。如果列表推导的代码超过了两行，你可能就要考虑是不是得用 for 循 环重写了


> 示例 2-4 使用列表推导计算笛卡儿积
```
>>> colors = ['black', 'white'] 
>>> sizes = ['S', 'M', 'L'] 
>>> tshirts = [(color, size) for color in colors for size in sizes] ➊ 
>>> tshirts 
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')] 

>>> for color in colors: ➋ 
...     for size in sizes: 
...         print((color, size)) 
... 
('black', 'S') 
('black', 'M') 
('black', 'L') 
('white', 'S') 
('white', 'M') 
('white', 'L') 

>>> tshirts = [(color, size) for size in sizes ➌ 
...                          for color in colors] 
>>> tshirts 
[('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]
```
> 列表推导的作用只有一个：生成列表。如果想生成其他类型的序列，生成器表达式 就派上了用场。

#### 2.2.4 生成器表达式

+ 生成器表达式 示例

> 示例2-5用生成器表达式初始化元组和数组
```
>>> symbols = '$¢£¥€¤' 
>>> tuple(ord(symbol) for symbol in symbols) 
(36, 162, 163, 165, 8364, 164) >>> import array

>>> array.array('I', (ord(symbol) for symbol in symbols)) 
array('I', [36, 162, 163, 165, 8364, 164])
```
> 示例 2-6 使用生成器表达式计算笛卡儿积

```
>>> colors = ['black', 'white'] 
>>> sizes = ['S', 'M', 'L'] 
>>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): ➊ 
... print(tshirt) 
... 
black S 
black M 
black L 
white S 
white M 
white L
```
示例 2-6 则是利用生成器表达式实现了一个笛卡儿积，用以打印出上文中我们提到 过的 T 恤衫的 2 种颜色和 3 种尺码的所有组合。与示例 2-4 不同的是，用到生 成器表达式之后，内存里不会留下一个有 6 个组合的列表，因为生成器表达式会在 每次 for 循环运行时才生成一个组合。如果要计算两个各有 1000 个元素的列表 的笛卡儿积，生成器表达式就可以帮忙省掉运行 for 循环的开销，即一个含有 100 万个元素的列表。

> 这里只是简单看看如何用生成器来初始化 除列表之外的序列，以及如何用它来避免额外的内存占用。

#### 2.3 元祖

> 拆包:把元组里面的数据提取出来,拆包有很多种,常用的有平行赋值,还有用*把元组拆包成函数的参数
+ 用 * 拆包
```
>>> divmod(20, 8)
(2, 4) 
>>> t = (20, 8) 
>>> divmod(*t) 
(2, 4) 
>>> quotient, remainder = divmod(*t) 
>>> quotient, remainder 
(2, 4)
```
下面是另一个例子，这里元组拆包的用法则是让一个函数可以用元组的形式返回多 个值，然后调用函数的代码就能轻松地接受这些返回值。比如 os.path.split() 函数就会返回以路径和最后一个文件名组成的元组 (path, last_part):

```
>>> import os 
>>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub') 
>>> filename 'idrsa.pub'
```

在进行拆包的时候，我们不总是对元组里所有的数据都感兴趣，_ 占位符能帮助处 理这种情况，上面这段代码也展示了它的用法。

+ 用 * 来处理剩下的元素

在 Python 中，函数用 *args 来获取不确定数量的参数算是一种经典写法了。 于是 Python 3 里，这个概念被扩展到了平行赋值中：

```
>>> a, b, *rest = range(5) 
>>> a, b, rest 
(0, 1, [2, 3, 4]) 

>>> a, b, *rest = range(3) 
>>> a, b, rest 
(0, 1, [2]) 

>>> a, b, *rest = range(2) 
>>> a, b, rest 
(0, 1, [])
```

在平行赋值中，* 前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表 达式的任意位置：

```
>>> a, *body, c, d = range(5) 
>>> a, body, c, d 
(0, [1, 2], 3, 4) 

>>> *head, b, c, d = range(5) 
>>> head, b, c, d 
([0, 1], 2, 3, 4)
```

#### 2.3.4 具名元组
> collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组 和一个有名字的类——这个带名字的类对调试程序有很大帮助。

示例 2-9 定义和使用具名元组
```
>>> from collections import namedtuple 
>>> City = namedtuple('City', 'name country population coordinates') ➊ 
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) ➋ 

>>> tokyo 
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667)) 

>>> tokyo.population ➌ 
36.933 

>>> tokyo.coordinates 
(35.689722, 139.691667) 

>>> tokyo[1] 
'JP'

```