#continue  跳过当前这一轮的循环
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
print("----------------------------")
#break 终止循环
for i in range(1,11):
    if i==8:
        break;
    print(i)