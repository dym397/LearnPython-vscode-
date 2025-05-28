#简单的嵌套
"""
if int(input("你的身高是多少"))>120:
    print("身高超出了,但是如果VIP等级>3可以买免费")
    if int(input("你的VIP等级是是多少:"))>=3:
        print("你可以进入！！")
    else:
        print("Sorry you need buy ticket!!")
else:
    print("you are children,you are free!!")
"""

#python 没有括号  全靠缩进识别层次关系  这和C语言是不一样的 (c语言乱缩进都没事)
#公司发礼物
age=int(input("please enter your age:"))
if age>=18 and age<30 :
    if int(input("请输入你的工龄:"))>=2 or int(input("请输入你的职级:"))>3:
        print("Congratulations!youhave delicate gift!!!!")
    else:
         print("Sorry you are none gift!!")
else:
    print("Sorry you are none gift!!")