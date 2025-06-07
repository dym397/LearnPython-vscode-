#和列表基本一样，但是元组定义好之后是不能修改的，还有元组采用(),而列表采用[]
#当元组只有一个数据元素的时候，需要添加一个 ‘,’才能保持元组类型
"""
list1=["da"]
print(list1)  ->输出["da"]
t1=("da")
print(t1)     ->输出 da,  此时的数据类型为 str而不是元组
t1=("da",)    ->输出 (da,) 此时的数据类型为元组
"""

Stu_tuple=("周杰伦",11,["music","stock exchange"])

#查询某个数据元素的下标
#查询年龄所在下标
print(f"年龄所在的下标为{Stu_tuple.index(11)}")
#这里的整个列表是元组类型，但是列表中的元素仅仅是列表类型，比如这里的“music”
print(Stu_tuple.index(["music","stock exchange"])) 

#查询元组中的内容
print(f"{Stu_tuple[0]}的数据类型为{type(Stu_tuple[0])}")

#删除学生爱好中的music
#不是说元组不能修改吗，但是哈我们可以对元组中的列表进行修改操作，
# 此时列表作为元组的一个元素是不能修改，但列表里面的内容可以更改
print(f"删除操作前的元组:{Stu_tuple}")
del Stu_tuple[2][0]
data=Stu_tuple[2].pop(0) 
#Stu_tuple[2]="da"   就是
print(f"删除操作后的元组:{Stu_tuple}")
Stu_tuple[2].append("coding")
print(f"在列表中添加coding后:{Stu_tuple}")