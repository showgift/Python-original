# 列表[] (可修改
list1 = ['a', 'b', 'c']
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
bicycles.count('redline')  # 统计该元素出现的次数
bicycles.extend(list1)  # 在表尾用新列表扩展原列表
len(bicycles)  # 长度
bicycles.index('trek')  # 找出与值相等的索引位置
bicycles.copy()  # 复制列表

# 下标访问，从0开始, 也可以从-1开始
print(bicycles[0])
message = f"i have a {bicycles[-1].title()}"

#  修改列表
bicycles[0] = 'ducati'
# 添加元素
bicycles.append('honda')  # append()末尾添加
bicycles.insert(1, 'suzuki')  # insert()插入到指定位置

# 删除元素
del bicycles[0]  # del 删除指定位置的元素
last_value = bicycles.pop(0)  # pop() 删除指定位置元素，并保留它.默认为表尾元素
print(last_value)
bicycles.remove('honda')  # 删除指定值的元素
# bicycles.clear()  # 清空列表

# 组织列表 (排序)
bicycles.sort()  # sort()默认升序即revers=False）  sort(key=None,revers=False)reverse=True为降序
sorted(bicycles)   # sorted()临时排序  升降：revers=False / revers=True
