Num = input("请输入一个整数：")
Num = eval(Num)
Str = 'Hello World'
if Num == 0:
    print("Hello World")
elif Num > 0:
    for i in range(2,len(Str),2):
        print(Str[i-2:i])
else:
    for i in range(len(Str)):
        print(Str[i])