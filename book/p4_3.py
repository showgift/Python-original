# tuple（） 元组 （元素不可直接更改
dimensions = (20, 200)
print(dimensions[0])

# 空元组
tuple_a = ()
print(tuple_a)
# 遍历元组
for dimension in dimensions:
    print(dimension)

# 修改元素  ———> 修改类型为列表后， 进行修改， 然后再次修改为元组
lista = list(dimensions)
lista[0] = 30
dimensions = tuple(lista)
print(dimensions)
# 或者对元组重新赋值
dimensions = (40, 30)
print(dimensions)
