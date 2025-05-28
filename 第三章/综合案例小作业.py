#随机产生一个数字  猜三次
import random
num=random.randint(1,10)
guess_num=int(input("请你猜一个数字:"))
if guess_num!=num:
    if guess_num>num:
        print("猜大了")
    else:
        print("猜小了")
    guess_num=int(input("再给你一次机会:"))
    if guess_num!=num:
        if guess_num>num:
            print("猜大了")
        else:
            print("猜小了")
    else:
        print("恭喜你第二次猜对了！！")
    if int(input("最后一次一次机会:")) !=num:
        print("猜错了,Game Over!!!")
    else:
        print("恭喜你第三次猜对了！！")
    print(f"最终的答案为:{num}")
else:
    print("恭喜你第一次就猜对了")
