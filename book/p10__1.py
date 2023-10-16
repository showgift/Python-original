# 存储数据
import json

numbers = [1, 3, 5, 9]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)  # json.dump() 接受两个实参 要存储的数据 可用于存储数据的文件对象


filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)  # json.load() 将列表读取到内存中

print(numbers)


filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We remember you {username}")
else:
    print(f"Welcome back, {username}")