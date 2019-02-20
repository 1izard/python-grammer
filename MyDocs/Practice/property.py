class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value

def main():
    homework1 = Homework()
    homework1.grade = 1
    print(homework1.grade)
    print()

    # homework1.grade = -1
    '''
        ValueError: Grade must be between 0 and 100
    '''




if __name__ == '__main__':
    main()