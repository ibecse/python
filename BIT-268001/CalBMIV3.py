# CalBMIV3.PY
height, weight = eval(input("请输入身高（米）和体重（公斤）（使用逗号分隔开）："))
bmi = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5<= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 27:
    who, nat = "偏胖", "偏胖"
elif 27 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI标准为：国际'{0}'，国家'{1}'".format(who, nat))
