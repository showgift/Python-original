# while循环           tip: ctrl+C停止运行中的程序

# 利用break（）跳出循环
current_num = 1
while current_num:
    print(current_num)
    current_num +=1
    if current_num > 10:
        break

# 利用变量控制循环
active = True
while active:
    message = input('quit or other')
    if message == 'quit':
        active = False
    else:
        print(message)

# 在循环中使用continue
while current_num < 20:
    current_num += 1
    if current_num % 2 ==0:
        continue
    print(current_num)
print(current_num)
