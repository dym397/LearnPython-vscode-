#列表的定义
#python的列表就是灵活，可以混合多种数据类型的，像C语言还要做区分(int float char .....)
name_list=[1,2,"dym",'a',False] # 输出 [1,2,"dym",'a'],我在想为啥不是输出 1,2,"dym",'a'
print(name_list)
print(type(name_list))

#list里面嵌套list
name_list2=[[1,2,3],"dym",[4,5,6]]
print(name_list2)
print(type(name_list2))
print("----------------------------")
#列表的下标索引 ,居然可以反向索引

name_list3=[1,2,3,4,5]
for i in range(0,5,1):
    print(name_list3[i],end=" ")
print()
#反向索引的时候最后一个元素下标为-1,其他的依次-1
for i in range(-1,-6,-1):
    print(name_list3[i],end=" ")
print()
print("----------------------------")
#嵌套list,和二维数组一模一样
name_list4=[[1,2,3],[4,5,6]]
print(name_list4[0][0])#输出的应该是1
print("----------------------------")
for i in range(0,2):
    for j in range(0,3):
        print(name_list4[i][j],end=" ")
    print()