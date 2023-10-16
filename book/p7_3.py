# 所有删除列表中特定的值
player = ['eli', 'charles', 'martina', 'michael', 'florence', 'eli']
while 'eli' in player:
    player.remove('eli')

# 使用用户输入来填充字典
responses = {}
flag = True
while flag:
    name = input("\n What is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("\n Would you like to let anther person respond?(yes/no) ")
    if repeat == 'no':
        flag = False
print("\n -----Poll Result-----")
for name, resp in responses.items():
    print(f"{name} would like to climb {resp}")
