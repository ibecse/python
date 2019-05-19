# CalBMIV2.py
height, weight = eval(input("请输入身高（米）和体重（公斤）（使用逗号隔开）："))
BMI = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(BMI))
nat = ""
if BMI < 18.5:
    nat = "偏瘦"
elif 18.5 <= BMI < 24:
    nat = "正常"
elif 24 <= BMI < 28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI指数为：国内'{0}'".format(nat))
