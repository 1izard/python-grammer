import weakref

class Grade(object):
    def __init__(self):
        self._values = weakref.WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

def main():
    exam1 = Exam()
    print('exam1.math_grade =', exam1.math_grade)
    exam1.math_grade = 10
    print('exam1.math_grade =', exam1.math_grade)
    print()

    grade1 = Grade()
    print('grade1.__get__()', grade1.__get__(None, Grade))
    print()

    exam2 = Exam()
    exam2.math_grade = 20
    print('exam1.math_grade =', exam1.math_grade)
    print('exam2.math_grade =', exam2.math_grade)
    print()


if __name__ == '__main__':
    main()