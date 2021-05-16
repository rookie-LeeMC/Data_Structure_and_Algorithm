'''
汉明距离
使用^对数据的位进行异或运算
按位异或运算符：当两对应的二进位相异时，结果为1

'''
# 方法一
x = 1
y = 4

x = bin(x).replace("0b", "")
y = bin(y).replace("0b", "")

if len(x) < len(y):
    x = "0" * (len(y) - len(x)) + x
else:
    y = "0" * (len(x) - len(y)) + y

print(sum([1 for i in range(len(x)) if x[i] != y[i]]))

# 方法二
print(bin(x ^ y).count("1"))
