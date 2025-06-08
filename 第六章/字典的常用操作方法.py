#字典通过key来获取对应的Value
dict1={"dym":99,"wxy":87,"dxz":76,"fhw":91}
print(f"dym的成绩为{dict1["dym"]}")
#新增键值对   假如你添加的key原来的字典中存在，那么会更新该字典的value.若原来的字典中没有才是新增
dict1["dym"]=77#修改dym的value
print(dict1)
dict1["fddd"]=100 #新增key fdddd ,以及value 100
print(dict1)
#取出指定key的value，并删除
value=dict1.pop("dym")
print(f"使用pop()取出dym关键字的value为{value},字典为{dict1}")

#获取字典的全部key
keys=dict1.keys()#返回值类型是 dict_key  
print(f"keys()的返回值类型是{type(keys)},返回的内容是{keys}")

#遍历字典
#(1)先获取字典中的所有key之后再遍历
for key in keys:
    print(f"{key}:{dict1[key]}")
print("-----------------------------")
#(2)直接用for遍历 
for key in dict1:
    #这里key 取到的是关键字，再根据关键字取得value
    print(f"{key}:{dict1[key]}")
#字典的长度  len()  长度是指键值对的个数
print(f"dict1字典的长度为{len(dict1)}")
#清空字典
dict1.clear()
print(f"清空后的dict1为:{dict1}")