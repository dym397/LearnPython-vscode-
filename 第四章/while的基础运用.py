#while的基础运用
"""

i=1
while i<=100:
    print(f"第{i}次说love python!")
    i+=1



#求1~100的和
num=1
sum=0
while num<=100:
    sum+=num
    num+=1
print(f"1~100的和为{sum}")
"""
#猜数字 猜对为止
import random
num=random.randint(1,100);
guess_num=int(input("请输入你猜的答案:"))
count=1
while guess_num!=num:
    count+=1
    if(guess_num<num):
        print("猜小了")
    else:
        print("猜大了")
    guess_num=int(input("请继续输入你猜的答案:"))
print(f"恭喜成功猜对！！你总共猜测了{count}次")