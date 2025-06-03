#ATM综合案例

def init():
    print("-------主菜单------")
    print("吴彦祖,你好,欢迎来到黑马ATM,请选择操作")
    print("查询余额\t[输入1]")
    print("存款   \t\t[输入2]")
    print("取款   \t\t[输入3]")
    print("退出   \t\t[输入4]")
    return None
isExit=1
money=500000
init()
while isExit==1:
    ret=int(input("请输入您的选择:"))
    if ret==1:
        print("------查询余额------")
        print(f"吴彦祖你好，您的余额剩余为{money}")
    elif ret==2:
        ret=int(input("请输入您的存款金额:"))
        money+=ret
        print(f"吴彦祖您好，您存款{ret}元成功\n您的余额剩余为{money}")
    elif ret==3:
        ret=int(input("请输入您的取款金额:"))
        if ret>money:
            print("超出余额限制,操作失败")
            init()
        else:
            money-=ret
            print(f"吴彦祖您好，您本次的取款金额为{ret}\n您剩余的余额为{money}")
    else:
       isExit=0
    init()
print("您已经退出")