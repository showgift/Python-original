# 返回值
# 简单返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 返回字典
def build_person(first_name, last_name):
    person = {'first': 'first_name', 'last': 'last_name'}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# 传递列表
def greet_users(names):
    """向列表中的用户问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['zhang', 'xue', 'you']
greet_users(usernames)
