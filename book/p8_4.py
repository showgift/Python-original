# 传递任意数量的实参
# def make_pizza(*toppings):  # 形参名(*toppings) 中'*' --> 建立一个空元组
#     """创建一个元组"""
#     print(toppings)
#
#
# list_a = [1, 2, 3]
# make_pizza(list_a)
# make_pizza('mushroom', 'green peppers')


def build_profile(first, last, **user_info):  # 形参名(**user_info) 中'**' --> 建立一个空字典
    """创建一个字典"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


def make_pizza(size, *toppings):
    """概述制作披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")