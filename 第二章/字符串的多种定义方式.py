#单引号定义法
name1='黑马程序员1'
print(type(name1),name1)

#双引号定义法(最常见的)
name2="黑马程序员2"
print(type(name2),name2)
#三引号定义法
name3=""" 黑马程序员3"""
print(type(name3),name3)

# \转义字符,字符串包含的内容比较复杂时(‘’ “” “”“ ”“”都包含时)
name4="\"黑马程序员4\""
print(name4) #输出"黑马程序员"
#假如输出单引号   则可采用双引号的方法
name5="'黑马程序员5'"
print("黑马程序员5") #输出'黑马程序员'
