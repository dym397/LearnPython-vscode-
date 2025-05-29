#九九乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        #print(f"{j}*{i}={i*j}",end=" ")
        print("%d*%d=%-2d "%(j,i,i*j),end="")#end=""是让末尾输出空格，否则默认输出'\n'
        j+=1
    print("\n",end="");
    i+=1#最外层,控制总共有九层打印数据