import os
file_path = input("请输入所在目录: ")
# 切换目录
os.chdir("py/"+file_path)
# 列出文件名称
all_file = os.listdir()
#print(all_file)
# 修改名称
# 1 获取.的索引进行切片处理
for old_file in all_file:
    index = old_file.rfind(".")
    new_file = old_file[:index] + "[复件]" + old_file[index:]
    os.rename(old_file,new_file)

