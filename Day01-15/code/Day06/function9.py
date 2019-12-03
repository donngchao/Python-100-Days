def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


doSomethingBeforeHi(hi)
# outputs:I am doing some boring work before executing hi()
#        hi yasoob!


def funnyAtHome():
    return "cheer up, forget the upset things in your life !"

doSomethingBeforeHi(funnyAtHome)


def lonely(reason="alone"):
    print("the reason why I feel lonely is because I am", reason)


doSomethingBeforeHi(lonely)

print(lonely())
print(hi())