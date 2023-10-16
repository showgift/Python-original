# 抛出异常
# 使用 raise 语句 抛出一个指定的异常
# raise 异常类型（reason）

# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))


try:
    raise NameError('HiThere')  # 模拟一个异常。
except NameError:
    print('An exception flew by!')
    raise  # 如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出


