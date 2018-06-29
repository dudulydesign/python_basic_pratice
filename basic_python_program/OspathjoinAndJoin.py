﻿'''
 Python中有join()和os.path.join()两个函数，具体作用如下：

    join()：连接字符串数组。
    将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串

    os.path.join()：将多个路径组合后返回


1、join()函数

语法：'sep'.join(seq)

参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串(ps：开头和结尾不会有sep，即seq元素之间由sep来拼接)

返回值：返回一个以分隔符sep连接各个元素后生成的字符串

 
2、os.path.join()函数

语法：  os.path.join(path1[,path2[,......]])

返回值：将多个路径组合后返回
'''
#str.join(sequence)
s1 = "-"
s2 = ""
seq = ("r","u","n","o","o","b")
print(s1.join(seq))
print(s2.join(seq))
