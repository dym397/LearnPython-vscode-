#python的for循环和C的完全不同，这里的for无法自己定义结束条件，只能由被处理的数据决定
#比如这里的for对name进行遍历，每一轮遍历到的每个字符都取到x中，至于遍历到什么时候结束有name的长度决定。
name="dymatshaa"
"""
for x in name:
    print(x,end='')
"""
#小练习  计算一共有几个a
count=0
for x in name:
    if x=="a":
        count+=1
print("一共有%d个a"%count)