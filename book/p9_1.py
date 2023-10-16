# 类 class
# 类中的函数称为 方法

class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):  # 一个特殊方法，创建类时会自动运行 --> 类的属性 /
        # 头尾各两个下划线旨在避免默认方法与普通方法名称冲突
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗打滚"""
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
my_dog.sit()
your_dog.sit()
my_dog.roll_over()
your_dog.roll_over()
