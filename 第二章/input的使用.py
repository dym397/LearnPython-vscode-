#input输入的使用
Name=input("请输入股票代码:")  #pyhton 确实简单，还能把内容写到input中间
#通过input输入的内容都是str类型，如果需要int,还需要进行转化int()
print(f"类型为{type(int(Name))},{Name}是永辉超市")