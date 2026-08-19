class Human:
    def __init__(self, age, gender): # self 指的是对象本身
        self.age = age
        self.gender = gender

    def sqrt(self,x):
        return x**2


zhangfei = Human(20,"男")
zhangfei.age
zhangfei.gender
zhangfei.sqrt(10)

caocao = Human(age=36,gender="男")

