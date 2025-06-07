#方法和函数的区别   
#方法是写在一个类里面的，比如list的各种操作接口都是定义在list这个类当中，那么这些接口就叫方法
#列表中的最大数量为2^(63)-1,估计数量是64b(0~2^(63)-1)
mylist=["dym","dsz","dy","dy"]
#1.从列表中找出某个值第一个匹配项的索引位置
index=mylist.index("dy")
print(f"\"dy\"的下标位置为{index}")
#2.指定位置插入元素
mylist.insert(0,"insert")#在0的位置插入“abc”
print(mylist)
#3.追加元素到list末尾(因为只能追加到末尾，所以不需要位置参数)
mylist.append("append")
print(mylist)
#4.批量追加元素extend()
add=[1,2,3,4]
mylist.extend(add)#直接把1,2,3,4追加到mylist的最后
print(mylist)
#5.删除元素 del无返回值   ，pop有返回值
del mylist[0]
print(mylist)
"""
del mylist #直接这么写就把mylist删除了,下面进行print就直接显示undefined
print(mylist)
"""
data=mylist.pop(0) #输入下标参数
print(data)
print(mylist)
#6.统计某元素在list中出现的次数
ret=mylist.count("dy")
print(f"\"dy\"的出现次数为{ret}")
print("清空列表")
print("从前往后遍历删除第一个匹配项元素")
#7.从前往后遍历删除第一个匹配项元素
mylist.remove("dy")
print(mylist)
#8.len()统计容器中元素的数量
print(f"mylist中的元素数量为{len(mylist)}个")
print("进行清空列表")
#8.清空列表
mylist.clear()
print(mylist)

