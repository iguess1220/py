
# with open("123.txt",'r',encoding='utf-8') as target:
#     context = target.read()
# with open("bak.txt",'w',encoding='utf-8') as bak:
#     bak.write(context)



# file_name = input("请输入文件名称: ")
# old_f = open(file_name,'r')
# new_file_name = '[bak]'+ file_name
# new_f = open(new_file_name,'w')
# while True:
#     context = old_f.readline()
#     if len(context) == 0 :
#         break
#     new_f.write(context)
# old_f.close()
# new_f.close()


# 文件名切片
# find() 是从字符串左边开始查询子字符串匹配到的第一个索引
# rfind()是从字符串右边开始查询字符串匹配到的第一个索引
# file_name = "123.txt"
# index = (file_name.rfind("."))
# a = file_name[:index]
# b = file_name[index:]
# print(a+"[附件]"+b)



# 文件定位问题,文件的读写都会改变光标定位
# 以下内容是错误示范：已写到结尾，所以读取不到内容

with open("123.txt",'w+') as target:
    # 查看光标位置：
    print(target.tell())
    target.write("hello,wrold")
    # 再次查看
    print(target.tell())
    # 调整光标
    # target.seek(offset,whence) offset是在whence的基础上做偏移，正数向后偏移,whence为0是移动光标到文件第一位，1为不变，2为文件末位
    target.seek(2,0) # 移动光标到文件第一位后再往后移动两个字节，注意为字节
    # 在python3里，只能对文件开头做偏移，也就是whence为1或2时，offset只能为0
    target.seek(0,1) 
    context = target.read()
print("读取的内容为%s" % context)