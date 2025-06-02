#发工资
import random
sum=10000
for StaffNo in range(1,21):
    grade=random.randint(1,10)#随机生成员工的绩效
    if grade<5:
        print(f"员工{StaffNo},绩效分{grade},不发工资，下一位")
        continue #如果绩效<5就不发工资
    
  
    sum-=1000
    print(f"向员工{StaffNo}发放工资1000元,账户余额还剩余{sum}元")
    if sum==0:
        print("工资发完了,下个月再领取吧")
        break;
print("-----------------------------")
