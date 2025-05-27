num=66
#说实话这么写我确实没想到，因为还是C语言的影响吧，不太习惯在input()里面写“ ”
if int(input("请输入一个我心里所想的数字:"))==num:
    print("恭喜你第一次就猜对了!!!")
elif int(input("请猜第二次:"))==num:
    print("还不错恭喜你猜对了!!");
else:
    print(f"Sorry,我心里想的是{num}")

        
