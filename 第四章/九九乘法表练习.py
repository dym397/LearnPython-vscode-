#九九乘法表


#while循环版本
"""
i=1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%-2d "%(j,i,i*j),end="")    #end=""是让末尾输出空格，否则默认输出'\n'
        j+=1
    print("\n",end="");
    i+=1#最外层,控制总共有九层打印数据
"""
#for循环版本
for i in range(1,10):#控制总的层数:9层  1~9
    for j in range(1,i+1):
        print("%d*%d=%-2d "%(j,i,j*i),end="")
    print()
#pyhthon的for循环中定义的局部变量 在外部也能访问到，但是尽量不要这么做