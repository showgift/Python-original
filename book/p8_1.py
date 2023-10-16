# 函数  使用def关键字定义函数
def greet_user(username):  # 函数名(形参)
    """以下代码块为函数体"""
    print(f"{username}. Hello!")


# 调用函数
greet_user("zhang")  # 函数名（实参）
greet_user(username="xue")  # 关键字实参


# （形参的）默认值  定义或调用函数时 等号两边 不留空格
def describe_pet(name, animal_type='dog'):
    """显示宠物信息"""
    print(f"\n I have a {animal_type} .")
    print(f"My {animal_type}'s name is {name}.")


describe_pet(name='pang')

# 等效调用函数
# describe_pet('pang') == describe_pet(name='pang')
# describe_pet('harry', 'hamster') == describe_pet(name='harry', animal_type='cat')
# == describe_pet(animal_type='cat', name='harry')