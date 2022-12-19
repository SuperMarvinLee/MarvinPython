import operator

#
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：


#字典
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("tinydict['Name']: ", tinydict['Name'])

# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 