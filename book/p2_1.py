name = " ada lovelace "
# 修改字符串大小写
# 首字母大写
print(name.title())
# 全大写
print(name.upper())
# 全小写
print(name.lower())
# 剔除字符右边空白
print(name.rstrip())
# 剔除字符左边空白
print(name.lstrip())
# 剔除字符两边空白
print(name.strip())

# format()
name1 = "zhang x"
full_name = f"{name}{name1}"
# or print(f"hello,{full_name}")
print(full_name)
message = f"hello ,{full_name}"
print(message)
# 制表符、换行符
print("python\tpython\njava")

# 数 --> 整数、浮点数
a = 2 + 3
# 值为浮点数的情况
b = 3 / 2  # 除法均为浮点数
c = 2 * 0.1  # 一操作数是浮点数，结果是浮点数
d = 3.0 ** 2

# 多变量赋值
a, n, v = 1, 1, 2
