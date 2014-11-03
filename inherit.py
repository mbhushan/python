class SchoolMember:

    members = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized school member: {})'.format(self.name)

    def tell(self):
        '''Tell my details'''
        print 'Name:"{}", Age:"{}"'.format(self.name, self.age)

class Teacher(SchoolMember):
    ''' Represents a teacher '''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        SchoolMember.members += 1
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        SchoolMember.members += 1
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.marks)

t = Teacher('Mr. Mani Bhushan', 32, 500000)
s = Student('Shreyansh',2,90)

#print a blank line
print

members = [t,s]
for m in members:
    m.tell()

print 'Total School Members: ', SchoolMember.members

