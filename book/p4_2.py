# 使用列表的一部分
player = ['charles', 'martina', 'michael', 'florence', 'eli']
print(player[0:3])
print(player[:4])
print(player[-3:])

# 遍历切片
for p in player[:3]:
    print((p.title()))

# 复制列表
foods = ['pizza', 'falafel', 'carrot']
a_foods = foods[:]  # 指向列表的副本
b_foods = foods  # 二者指向同一列表
print(a_foods)
