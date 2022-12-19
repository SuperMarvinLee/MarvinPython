#幂
print(2**3)
print(7/3)
#整除
print(7//3)

#Python3.8 版本新增运算符;海象运算符，可在表达式内部为变量赋值。
a='helloworld'
if (n := len(a)) >= 10:
    print(f"List is too long ({n} elements, expected <= 10)")

# 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
# 一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#
name = 'Runoob'
print('Hello %s' % name)

#f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。
name = 'Runoob'
f'Hello {name}'  # 替换变量
f'{1+2}'         # 使用表达式
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
f'{w["name"]}: {w["url"]}'

#Unicode 字符串; 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，
#这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。在Python3中，所有的字符串都是Unicode字符串。 

#将字符串的第一个字符转换为大写
print('marvin'.capitalize())
print(str.capitalize('marvin'))
#返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
marvin = 'marvin'
print(marvin.center(10,'*'))
#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print('marvinm'.count('m',0,len('marvinm')))

#end关键字
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

#range() 函数
for i in range(6, 10):
    print(i)

for i in range(0, 10, 3) :#3为步长
    print(i)

#读取键盘输入
# str = input("请输入：")
# print ("你输入的内容是: ", str)

#输出格式美化
s = 'Hello, Runoob'
#str()： 函数返回一个用户易读的表达形式。 
print(str(s))
#repr()： 产生一个解释器易读的表达形式
print(repr(s))