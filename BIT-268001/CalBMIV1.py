# CalBMIV1.py
height, weight = eval(input("请输入身高（米）和体重（公斤）（使用逗号隔开）："))
BMI = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(BMI))
who = ""
if BMI < 18.5:
    who = "偏瘦"
elif 18.5 <= BMI < 25:
    who = "正常"
elif 25 <= BMI < 30:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI指标为：国际'{0}'".format(who))
