#确实灵活  返回类型不必统一，随便返回什么都可以
def CheckAge(age):
    if age>=30:
        return "SUCCESS"
    if age>=18:
        return 2
    else:
        return None


ret=CheckAge(30)
print(f"返回值是{ret},返回类型是{type(ret)}")


#这里的not就相当于c的!(取非)
# if not CheckAge(int(input("输入您的年龄:"))):
#     print("您是未成年")
# else:
#     print("您是成年人")
