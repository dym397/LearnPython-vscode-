Name="永辉超市"
StockPrice=5.06
StockCode="601933"
StockPrice_dailygrowth_factor=1.1
GrowthDays=7
print(f"公司:{Name},股票代码为:{StockCode},当前股价为{StockPrice}")
print("每日增长系数为%.1f,经过%d天的增长后,股价达到了:%.2f"%
      (StockPrice_dailygrowth_factor,GrowthDays,StockPrice*(StockPrice_dailygrowth_factor**7)))