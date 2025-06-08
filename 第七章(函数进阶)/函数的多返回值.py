#python可以返回多个值，令我震惊，我按照C语言来思考的话，同时返回多个值，我只能通过传入参数把值带出来了
def test():
    return 1,2
#假如我用一个变量来接收的话，就变成一个元组类型的数据了
y=test()
print(f"{y},{type(y)}")
#正常的用两个变量来接收  x和y就都是Int类型了
x,y=test()
print(f"x的类型为{type(x)},x={x},y的类型为{type(y)},y={y}")



