# 继承 --> 子类继承父类（超类） 在既有类的基础上编写新类
# 通常调用父类的方法 __init__() ，让子类包含其所有属性
from p9_2 import Car


class ElectricCar(Car):
    """电车"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电车特有属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()
    # def describe_battery(self):
    #     """描述电池容量"""
    #     print(f"This car as a {self.battery_size}--kwh battery")

    def update_odometer(self, mileage):  # 重写父类
        """重写父类的方法，假设电车总里程可以任改"""
        self.odometer_reading = mileage


#  将实例用作属性 例如要详细描述电池,将电池从ElectricCar中分离出并建立新的Battery类
class Battery:
    """电池类"""

    def __init__(self, battery_size=75):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """描述电池容量"""
        print(f"This car as a {self.battery_size}--kwh battery")


my_car = ElectricCar('tesla', 'model s', '2019')

print(my_car.get_descriptive_name())
my_car.battery.describe_battery()


