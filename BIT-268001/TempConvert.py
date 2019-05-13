# TempConvert
TempStr = input("请输入带符号的温度：")
if TempStr[-1] in ['c','C']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("华氏温度为：{:.2f}F".format(F))
elif TempStr[-1] in ['f','F']:
    C = (eval(TempStr[0:-1])-32) / 1.8
    print("摄氏温度为：{:.2f}C".format(C))
else:
    print("输入错误！")
