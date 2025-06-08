#lambda匿名函数  临时使用的函数  和def定义的不一样，def定义的是一直存在
#虽然不知道有什么用，但是随着后面的深入学习和应用肯定会经常碰到的，到时候就熟悉和理解了
def add(x,y):
    return x+y

def test(func):
    print(func(1,2))
    print(f"func的类型为{type(func)}")


test(lambda x,y:x+y)#这样就可以代替add的定义 