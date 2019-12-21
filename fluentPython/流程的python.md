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