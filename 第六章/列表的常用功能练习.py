StudentAge=[21,25,21,23,22,20]
def init():
    print("欢迎来到学生管理系统")
    print(StudentAge)
    print("指定位置添加学生年龄:请按输入1")
    print("批量增加学生年龄请输入2")
    print("查找指定年龄请输入3")
    print("取出指定位置学生年龄请输入4")
    print("退出系统请输入666")
def Display():
    print(StudentAge)
init()
isexit=0;
while isexit==0:
    result=int(input("请输入您的操作:"))
    if result==1:
        pos=int(input("请输入您需要插入的位置:"))
        age=int(input("请输入您需要插入的年龄:"))
        StudentAge.insert(pos,age)
    elif result==2:
        num=int(input("请输入您需要增加的数量:"))
        for i in range(0,num):
            age=int(input("请输入您需要插入的年龄:"))
            StudentAge.append(age)
    elif result==3:
        age=int(input("请输入您需要查找的年龄:"))
        index=StudentAge.index(age)
        print(f"查询到的下标结果是:{index}")
    elif result==4:
        pos=int(input("请输入您需要查询的位置:"))
        print(f"查询结果为:{StudentAge[pos]}")
    else:
        isexit=1
    print("操作成功")
    if   not isexit:
        Display()
        print("-------------------------")
        init()

        



    
    
    
