# 遍历字典
user = {'username': 'zhang', 'first': 'enrico', 'first': 'zhang', 'xue': 'you'}
for key, value in user.items():
    print(f"the key:value is: {key}: {value}")
print(user.items())  # dict.items() 以列表形式返回视图对象 -->key:value
print(user.keys())   # user.keys()  以列表形式返回视图对象  -->keys
print(user.values())  # user.values()  以列表形式返回视图对象  -->values
# 视图对象不是列表，不可更改，可通过list()更改为列表

# 按特定顺序遍历字典的键
for a in sorted(user.keys()):
    print(f"排序后：{a}")

# set()集合类型，集合中元素唯一不重复
# set() 剔除重复项
print(user)
for a in set(user.keys()):
    print(f"{a}a")
print(user)
for a in set(user.values()):
    print(a)
