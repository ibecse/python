# CalBMIV2.py
height, weight = eval(input("请输入身高（米）和体重（公斤）（使用逗号分隔开）："))
bmi = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(bmi))
nat = ""
if bmi < 18.5:
    nat = "偏瘦"
elif 18.5 <= bmi < 24:
    nat = "正常"
elif 24 <= bmi < 27:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI标准为:国家'{0}'".format(nat))
