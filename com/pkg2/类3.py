"""from com.pkg2.hello import Z as k

y = 20
print(y)
print(k)
"""
class Student(object):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
         return self.__name
    def __str__(self):
        return '%s' % self.__name
dsf = Student('DSF')
print(dsf.get_name())

print(Student('Michael'))