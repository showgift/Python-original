# 字典 dictionary{ 键 : 值}
alien = {'color': 'green', 'points': '5', 'speed': 'fast', }
print(alien['color'])

# 添加键值对
alien['num'] = 23
print(alien)

# 修改字典中的值
alien['color'] = 'yellow'

# 删除键值对
del alien['color']
print(alien)

# 使用get() 访问值
# get() 第一个参数用于指定键(必不可少)， 第二个参数为指定键不存在是返回的值
point_value= alien.get('color', 'No point Value assigned')
print(point_value)
