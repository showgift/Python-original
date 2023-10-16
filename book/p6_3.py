# 嵌套
# 用列表储存字典
alien0 = {'color': 'green', 'points': '5'}
alien1 = {'color': 'blue', 'points': '3'}
alien2 = {'color': 'red', 'points': '1'}
alien = [alien0, alien1, alien2]
print(alien)

# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")