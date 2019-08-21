from wxpy import *
import openpyxl

bot = Bot(cache_path=True)
my_friends = bot.friends()
print("好友数量：{}".format(len(my_friends)))
lis = [['NickName', 'RemarkName', 'Sex', 'Province', 'City', 'Signature']]

for friend in my_friends:
    NickName = friend.raw.get('NickName', None)
    RemarkName = friend.raw.get('RemarkName', None)
    Sex = {1: "男", 2: "女", 3: "其他"}.get(friend.raw.get('Sex', None), None)
    City = friend.raw.get('City', None)
    Province = friend.raw.get('Province', None)
    Signature = friend.raw.get('Signature', None)
    list_0 = [NickName, RemarkName, Sex, Province, City, Signature]
    lis.append(list_0)


def list_excel(filename, lis):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'WechatFriends'
    file_name = filename + '.xlsx'
    for i in range(0, len(lis)):
        for j in range(0, len(lis[i])):
            sheet.cell(row=i+1, column=j+1, value=str(lis[i][j]))
    workbook.save(file_name)
    print("写入成功！")


list_excel('wechat', lis)


