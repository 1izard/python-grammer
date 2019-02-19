class Grade1(object):
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        print('__get__1')
        if instance is None: return self
        print('__get__2')
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    math_grade = Grade1()
    writing_grade = Grade1()
    science_grade = Grade1()


class MyClazz(object):
    def __init__(self):
        self.value = 0

def main():
    exam1 = Exam()
    print('exam1.math_grade =', exam1.math_grade)
    exam1.math_grade = 10
    print('exam1.math_grade =', exam1.math_grade)
    print()

    grade1 = Grade1()
    print('grade1.__get__()', grade1.__get__(None, Grade1))
    print()

    exam2 = Exam()
    exam2.math_grade = 20
    print('exam1.math_grade =', exam1.math_grade)
    print('exam2.math_grade =', exam2.math_grade)
    print()

    my_clazz1 = MyClazz()
    print('my_clazz1', my_clazz1.__dict__['value'])

if __name__ == '__main__':
    main()
