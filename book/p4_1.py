# 操作列表  数字列表

# 遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"the value is{magician}")

# 创建数值列表 --> range()函数  ,range(a,b) 取值a-b但不取b
for value in range(1, 5):
    print(value)
# 使用range()函数建列表
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 对数字列表的 简单统计计算
digits = list(range(1, 6))
min(digits)
max(digits)
sum(digits)
