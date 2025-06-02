#rang的用处是生成一个序列
#用法1
for i in range(10):#生成0~9的序列
    print(i)
print("---------------------------")
#用法2
for i in range(5,10): #生成5~9
    print(i)
print("---------------------------")
#用法3
for i in range(5,10,2):#生成序列范围处于5~9，步长为2
    print(i)
print("---------------------------")
#range作为条件控制for循环的次数, 因为前面不是说这里的for和C的不同，控制不了循环次数吗。
#for(int i=0;i<10;i++)
#printf("dym");
for i in range(10):
    print("dym")     #for实现打印10次