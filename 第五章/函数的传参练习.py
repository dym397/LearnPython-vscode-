#自动查核酸
def examin(temp):
    if temp<=37.5:
        print(f"您的体温为{temp},正常!!")
    else:
        print(f"您的体温为:{temp},体温异常")
for i in range(1,11):
    examin(int(input("请输入您的体温:")))
