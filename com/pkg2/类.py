# from com.pkg2.hello import y
# print(y)

class Animal(object):
    __slots__ = ('__name', 'age')
    # 用tuple定义允许绑定的属性名称, 仅对当前类实例起作用

    def run(self):
        print('animal')

    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def name(self):
        print(self.__name)

    def set_age(self,age):
        if not isinstance(age, int):
             raise ValueError('score must be an integer!')
        if age < 0 or age > 100:
             raise ValueError('score must between 0 ~ 100!')
        self.age = age

    """     @property
    def age(self):
        return self._age


    @score.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('score must be an integer!')
        if age < 0 or age > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._age = age
"""



  #TODO
class Dog(Animal):
        def run(self):
            print('dog')
        def name(self):
            print('h')

class Screen(object):
        @property
        def width(self):
            return self._width
        @width.setter
        def width(self, width):
            self._width = width
        @property
        def height(self):
            return self._height
        @height.setter
        def height(self, height):
            self._height = height
        @property
        def resolution(self):
            return self._height * self._width


Pig = Animal('Pig')
Pig.set_age(10)
print(Pig.age)
#Pig.DO = 55       由于'score'没有被放到__slots__中，
# 所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


cat = Animal('CAT')
cat.name()
if  cat.get_name() != 'CAT':
    print('no')
else:
    print('yes')


do = Dog('DO')
do.run()
do.name()
print(isinstance(do, Dog))
print(isinstance(do, Animal))
print(type(do ) == Dog )
print(dir(do))
do.DO = 66
do.DO
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：