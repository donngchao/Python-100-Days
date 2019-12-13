def hi(name="yasoob"):
    def greet():
        return "now you are in the hi.greet() function"

    def welcome():
        return "now you are in the hi.welcome() function"


    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
# outputs: <function hi.<locals>.greet at 0x00000000025BD488>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# 现在试试这个

print(a())
# outputs: now you are in the hi.greet() function

b = hi(name="chal")
print(b)  # <function hi.<locals>.welcome at 0x00000000027CD378>
print(b())
# now you are in the hi.welcome() function
'''
在 if/else 语句中我们返回 greet 和 welcome，
而不是 greet() 和 welcome()。为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；
然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。

这里是将函数作为返回值
'''