print("欢迎来到dym的游乐园")
age=input("请输入你的年龄:")
#input return str type
age=int(age)
if age>=18:
    print("您已经成年,游玩需要补票30元")
elif age<10:
    print("抱歉您的年龄太小了,不能进入哦！！")
else:
    print("您可以免费游玩")
print("祝您游玩愉快")
