#身份运算符is
a=b=3
print(a is b)
print(id(a))
print(id(b))
b*=2
print(a is b)
print(id(a))
print(id(b))