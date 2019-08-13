class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bob = Student('bob',98)
print(bob.score)
bob.score = 77
print(bob.score)
bob.coc = 99
print(bob.coc)
bob.print_score()