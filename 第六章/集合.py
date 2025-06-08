#集合相对于列表、元组来说最大的特点就是无序(没有下标)、不重复
my_list=["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"]
# myset={}  这么写有问题 定义出来是dict类型的  但是在定义一个空列表的时候是可以这么干的
#原来是这个写法 是用来定义字典的，所以是dict类型  Python中字典的使用比集合更早，{} 最初被设计用来表示字典。
myset=set(my_list)   #也可以这么直接赋值(set函数的内部自己实现逐个遍历)   或者for循环的方式一个个add()
# arry=[]
# for i in my_list:
#     myset.add(i)
print(f"myset的内容为:{myset},数据类型为:{type(myset)}")
print("-----------------------------------------------------")
myset2={"黑马程序员","dym","itcast","千锋教育","传智播客"}
#remove() 移除集合内指定元素
myset.remove("传智播客")
print(f"myset删除'传智播客后的集合':{myset}")
print("-----------------------------------------")
#集合1.difference_update(集合2) 修改集合1，在集合1中把集合2中有的去除
print(f"myset为:{myset}")
print(f"myset2为:{myset2}")
myset.difference_update(myset2)
print(f"myset执行difference_update(myset2)后：{myset}")
print("-----------------------------------------")
myset.add("黑马程序员")
myset2.add("best")
#集合1.difference(集合2) 得到一个新的集合，新集合中就是集合1比集合2多的内容
print(f"myset为:{myset}")
print(f"myset2为:{myset2}")
myset3=myset2.difference(myset)
print(f"myset2执行difference_update(myset)后生成新的集合：{myset3}")
myset3=myset.difference(myset2)
print(f"myset执行difference_update(myset2)后生成新的集合：{myset3}")
print("-----------------------------------------")

#集合1union集合2    产生新的集合(合并两个集合）
print(f"myset为:{myset}")
print(f"myset2为:{myset2}")
print(myset.union(myset2))
print("-----------------------------------------")
#len()  集合中元素的数量
print(f"myset为:{myset}")
print(f"myset2为:{myset2}")
print(f"myset集合中的元素数量为:{len(myset)}")
print(f"myset2集合中的元素数量为:{len(myset2)}")
print("-----------------------------------------")

#pop() 从集合中随机移除一个元素
print(f"myset为:{myset}")
myset.pop()
print(f"myset执行随机清除后的结果为:{myset}")
#clear()  将集合清空
myset.clear()
myset2.clear()
print(f"myset和myset2都被clear\nmyset:{myset},myset2:{myset2}")