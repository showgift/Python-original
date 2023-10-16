# 写入文件
filename = 'pi_digits.txt'
# 打开模式共16种，以下四种为常用

with open(filename, 'w') as file_object:  # open(文件名, '打开模式') 常用模式--> r:读取 w:写入 r+:读写 a:附加 x:创建
    file_object.write("I love programing")  # 写入模式 当文件不存在则创建，存在则清空文件内容
    file_object.write("and you\n")        # write() 不会自动在末尾添加换行符
    file_object.write("and you\n")

# 附加到文件
with open(filename, 'a') as file_object:
    file_object.write("I love anything you love")
