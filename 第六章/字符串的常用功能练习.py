#字符串也是一种容器，字符容器
#（1） char *str="abc",像这种在C语言中也是不能修改的，因为这个字符串常量存储在常量区只可读。
#（2）char str[]="abc",这种就是可以修改的，str[0]='q',因为这个定义的是数组，存在栈区


#在python中 str="abc",和上面的（1）一样都不可修改，至于原因和上面就不一样了
# str1="abc"
# str1[0]='x'   #这是不可以的   

str1="ittheima itcast boxuegu"
#统计”it“的数量 count()
print(f"字符串{str1}中一共有{str1.count("it")}个\"it\"")
#将空格替换为字符‘|’   replace()会返回一个新的字符串，而不是基于原来的修改
str2=str1.replace(' ','|')
print(f"字符串{str1}，被替换空格后：{str2}")
#将字符串按照 '|'进行分割 用split(),返回的是一个列表，而不是原来的字符串
str3=str2.split('|')#str3是一个列表
print(f"字符串{str2}按'|'进行分割后:{str3}")

#strip的使用，可以去除末尾指定的内容
str4=" 12abcd21 "
str5=str4.strip()#不传参默认去除空格
print(f"字符串{str4}去除开头和末尾的空格后:{str5},类型为{type(str5)}")
str6=str5.strip("12")
#这里我去除开头和末尾的12，但是末尾的21也被去除了
#这是因为其实并不是按照“12”整个来去除的，而是“1”和“2”来检索的,遇到非'1'和'2'就会结束检索
print(f"字符串{str5}去除开头和末尾的空格后:{str6},类型为{type(str6)}")