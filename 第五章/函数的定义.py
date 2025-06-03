# 函数的定义  def函数名():
def func():
    for i in range(1,10):#控制总的层数:9层  1~9
        for j in range(1,i+1):
             print("%d*%d=%-2d "%(j,i,j*i),end="")
        print()
    return
def calc(a,b):
    print(f"{a}+{b}的和为{a+b}")
def welcome():
    print("欢迎来岛黑么程序员！")
    print("请出示您的健康码以及72小时核酸证明")
    return
func()
calc(4,5)
welcome()