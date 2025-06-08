def test(name,age,gender):
    print(f"姓名：{name},年龄：{age},性别：{gender}")
#位置参数  过去在C语言种接触到的基本都是这种
test("dym",25,"男")

#关键字传参   就是显式的指明形参，用para=value的形式传参
test(name="dym",age=25,gender="男")
test(age=25,name="dym",gender="男")#这种方式的话参数的位置顺序可以随便写，因为里面具体的写出了哪个参数传什么值

#缺省传参  ---就是可以不传递完整的参数(有一些参数可以在函数定义时直接指定，传参时就不用传)
def test2(name,age,gender="男"):#这里的gender参数先提前写入，调用该函数的时候可以不传这个参数。这个参数必须在最后的位置!!!1
    print(f"姓名：{name},年龄：{age},性别：{gender}")
test2(name="dym",age=25)
test2(name="dym",age=25,gender="女")#如果再对gender传参是可以把原来的默认参数覆盖掉的


#不定长参数(位置不定长) 用*来表示，这里可不是指针的意思
def test3(*args):#这里的args是元组类型
    print(f"不定长参数args为{args},该参数的类型为{type(args)}")
test3("dym",25,"男","单片机")

#不定长参数(关键字不定长) 用**来表示 ---也就是可以使用多个 para=value的形式
def test4(**args):#这里的args为字典类型
    print(f"不定长参数args为{args},该参数的类型为{type(args)}")
test4(name="dym",age=25,gender="男",job="single chip develop")