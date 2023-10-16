"""
读取文件 --> 以任何方式使用文件都要打开文件
读取文本文件时，python将其中的文本都解读为字符串
with 关键字妥善的打开和关闭文件 / 会自动调用 close()方法
with 的作用类似于 try-except-finally
使用 with 关键字时，open()返回的文件对象只能在with代码块内可用
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(file_object.closed)  # 验证文件是否关闭


"""
创建一个包含文件各行内容的列表
由于with open()..打开的文件只能在with代码块内使用
将内容存储在列表中，令其它代码块也可以使用

"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # readlines()从文件中读取每一行，并存储在一个列表中
    print(lines)

for line in lines:
    print(line)


# with的工作原理-->https://blog.csdn.net/u012609509/article/details/72911564?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168076259316800186553555%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168076259316800186553555&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-72911564-null-null.142^v81^insert_down1,201^v4^add_ask,239^v2^insert_chatgpt&utm_term=with&spm=1018.2226.3001.4187

