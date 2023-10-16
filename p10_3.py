# 错误 与 异常
"""
遗漏冒号后运行程序
code: while True
        print("a")
out --> SyntaxError（语法错误）: invalid syntax
"""

# 异常
"""
异常 即语法正确时报错
当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行
使用 try：
        可能出现错误的代码
    except 异常类型：
        产生错误的处理方法
    else：  (可以加else 作为没有捕获异常的返回)
        如果没有捕获异常则 do sth 
    finally:   # 它定义了无论在任何情况下都会执行的清理行为
        无论有没有异常都执行的代码
    
    # 可以是 try-except // try-except-else // try-except-else-finally 三种组合方式
"""
# ZeroDivisionError: division by zero -->  0 做除数
# a = 5/0
# print(a)

try:
    a = 5 / 1
except ZeroDivisionError:
    pass               # 静默异常
else:
    print(a)

# FileNotFoundError: [Errno 2] No such file or directory: '1213.txt'  --> 找不到文件
# with open('1213.txt', 'r') as f:
#     contents = f.read()

# NameError: name 'num' is not defined --> 变量名错误
# a = num*3

# TypeError: can only concatenate str (not "int") to str -->类型错误
# a = 'str'
# b = 12
# print(a+b)

# 获取 异常的信息
#     args：返回异常的错误编号和描述字符串；
#     str(e)：返回异常信息，但不包括异常信息的类型；
#     repr(e)：返回较全的异常信息，包括异常信息的类型。
try:
    1/0
except Exception as e:
    # 访问异常的错误编号和详细信息
    print(e.args)
    print(str(e))
    print(repr(e))

