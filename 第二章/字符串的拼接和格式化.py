#字符串的拼接
name="董益民"
address="虹梅新苑"
roomNum=401
SharePrice=5.06
print(name,"在",address) # 董益民 在 虹梅新苑
print(name+"在"+address) # 董益民在虹梅新苑
#但是这中拼接的方法只能str和str拼接 不能和int拼接
#print(name+"在"+address+roomNum)


#格式化输出,可以把str和int拼接在一起
#像这里的rooNum的格式化输出，如果用%s，那么会直接把int转为str
print("我是%s,我在%s的%s房间\n"%(name,address,roomNum)) 

messsage="我是%s,我在%s的%d房间"%(name,address,roomNum)
print(type(messsage),messsage)

#格式化的精度控制
num1=19.99
print("19.99保留小数点2位为:%.2f"%num1)
num2=66
#%5d 右对齐  %-5d左对齐  总共占5个位置
print("66输出宽度为5:%5d"%num2)
print("66输出宽度为5:%-5d%d"%(num2,num2))

#最快速的格式化 确实是方便，不用精度控制，float都不用设置保留几位s，直接{}里填变量(占位)，一步到位
#而且不区分类型，什么类型都能直接填进去
print(f"我是{name},我住在{address},我的房间号为{roomNum},我买了永辉超市的股票，今日股价为{SharePrice}")

#表达式的格式化(有明确结果的才是表达式，赋值语句不是表达式比如s+=1)
num3=13.1
print(f"num3的数据类型为{type(num3)}")
print("num3*2的结果为%d"%(num3*2))