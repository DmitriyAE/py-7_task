class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return result

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating == other.average_rating

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating <= other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating == other.average_rating

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating <= other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


student_1 = Student('Anton', 'Antonov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Boris', 'Borisov')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Victor', 'Victorov')
student_3.courses_in_progress += ['Python', 'Git']
student_3.finished_courses += ['Введение в программирование']


lecturer_1 = Lecturer('Gleb', 'Glebov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Denis', 'Denisov')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Ermak', 'Ermakov')
lecturer_3.courses_attached += ['Python']


reviewer_1 = Reviewer('Ivan', 'Ivanov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Konstantin', 'Konstantinov')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']


student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_1.rate_hw(lecturer_2, 'Python', 5)
student_1.rate_hw(lecturer_2, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Python', 8)

student_1.rate_hw(lecturer_1, 'Python', 7)
student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_1, 'Python', 9)

student_2.rate_hw(lecturer_2, 'Git', 10)
student_2.rate_hw(lecturer_2, 'Git', 8)
student_2.rate_hw(lecturer_2, 'Git', 9)

student_3.rate_hw(lecturer_3, 'Python', 5)
student_3.rate_hw(lecturer_3, 'Python', 6)
student_3.rate_hw(lecturer_3, 'Python', 4)
student_3.rate_hw(lecturer_2, 'Git', 1)
student_3.rate_hw(lecturer_2, 'Git', 2)
student_3.rate_hw(lecturer_2, 'Git', 3)


reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_3, 'Git', 5)
reviewer_2.rate_hw(student_3, 'Git', 9)
reviewer_2.rate_hw(student_3, 'Git', 8)

reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 7)
reviewer_2.rate_hw(student_3, 'Python', 9)


print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print(f'Результат сравнения студентов (по средним оценкам за домашнее задание): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 < student_2}')
print(f'Результат сравнения студентов (по средним оценкам за домашнее задание): '
      f'{student_1.name} {student_1.surname} <= {student_2.name} {student_2.surname} = {student_1 <= student_2}')
print(f'Результат сравнения студентов (по средним оценкам за домашнее задание): '
      f'{student_1.name} {student_1.surname} != {student_2.name} {student_2.surname} = {student_1 != student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} >= {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 >= lecturer_2}')
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} == {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 == lecturer_2}')
print()

student_list = [student_1, student_2, student_3]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка для всех студентов по курсу {'Git'}: {student_rating(student_list, 'Git')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {lecturer_rating(lecturer_list, 'Git')}")