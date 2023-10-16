# if条件语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.upper())

# 检查特定值是否在列表中
if 'audi' in cars:
    print(f"audi is in {cars}")

# 常见结构if-else、if-elif-else
age = 12
if age < 4:
    print("you will cost 0$")
elif age < 18:
    print("you will cost 10$")
else:
    print("you will cost 20$")

# 判断列表是否为空
list_b = []
if list_b:
    print("列表非空")
else:
    print("列表为空")
