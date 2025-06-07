test_list=[1,2,3,4,5,6]
#len() 获取列表的长度
length=len(test_list)
#for循环
for i in range(0,length):
    print(test_list[i],end=" ")
print("\n--------------------------")
#我的第一个想法是上面这种通过range实现遍历,但是python也能这样遍历
for element in test_list:
    print(element,end=" ")
print("\n--------------------------")
#while循环
index=0
while index<length:
    print(test_list[index],end=" ")
    index+=1
print("\n--------------------------")
odd_list=[]
even_list=[]  #空列表
for element in test_list:
    if element%2==0:
        even_list.append(element)
    else:
        odd_list.append(element)
print(even_list)
print(odd_list)
    
