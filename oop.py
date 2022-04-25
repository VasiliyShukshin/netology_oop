class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def raiting(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.students_rating:
                lecturer.students_rating[course] += [grade]
            else:
                lecturer.students_rating[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self, grades):
        i=0
        for course, grade in grades.items():
            i += sum(grade)/len(grade)
        k = i/len(grades)
        # text = f"{k}"
        return k


    def __str__(self):

        text = (f"Имя: {self.name}\n" 
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {self.avg_grade(self.grades)}\n"
                f"Курсы в процссе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: Введение в программирование\n\n")
        return text

    def sravni(self, enemy):
        if not isinstance(enemy, Student):
            return

        if self.avg_grade(self.grades) > enemy.avg_grade(enemy.grades):
            return f"У студента {self.name} {self.surname} средняя оценка выше"
        elif self.avg_grade(self.grades) == enemy:
            return f"У студентов средние оценки равны"
        else:
            return f"У студента {self.name} {self.surname} средняя оценка меньше"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, students_rating = {}):
        super().__init__(name, surname)
        self.students_rating = students_rating

    def avg_grade(self, students_rating):
        i=0
        for course, grade in students_rating.items():
            i += sum(grade)/len(grade)
        k = i/len(students_rating)
        # text = f"{k}"
        return k

    def sravni(self, enemy):
        if not isinstance(enemy, Lecturer):
            return

        if self.avg_grade(self.students_rating) > enemy.avg_grade(enemy.students_rating):
            return f"У лектора {self.name} {self.surname} средняя оценка выше"
        elif self.avg_grade(self.students_rating) == enemy:
            return f"У лекторов средние оценки равны"
        else:
            return f"У лектора {self.name} {self.surname} средняя оценка меньше"

    def __str__(self):
        text = (f"Имя: {self.name}\n" 
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекцию: {self.avg_grade(self.students_rating)}\n\n")
        return text

class Reviewer(Mentor):
    # def __init__(self):
    #     super().init(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = (f"Имя: {self.name}\n" 
                f"Фамилия: {self.surname}\n\n")
        return text


def avg_all_students(list_students, course_students):
    if type(list_students) == list:
        i = 0
        for student in list_students:
            if course_students in student.courses_in_progress:
            # if course_students
                i += student.avg_grade(student.grades)
        avg_all = i/len(list_students)
        print(f"средняя оценка студентов на курсе {avg_all}")
            # print(course_students)
        # print("Variable is a list.")
    else:
        print("пожалуйста передайте список студентов")


def avg_all_lecturers(list_lecturers, course_lecturers):
    if type(list_lecturers) == list:
        i = 0
        for lecturer in list_lecturers:
            if course_lecturers in lecturer.courses_attached:
            # if course_students
                i += lecturer.avg_grade(lecturer.students_rating)
        avg_all = i/len(list_lecturers)
        print(f"средняя оценка лекторов на курсе {avg_all}")
            # print(course_students)
        # print("Variable is a list.")
    else:
        print("пожалуйста передайте список студентов")
# best_student = Student('Ruoy', 'Eman', 'man')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['Git']



student_one = Student('Пётр', 'Петров', 'man')
student_one.courses_in_progress += ['Python']
student_one.courses_in_progress += ['Git']

student_two = Student('Мария', 'Кукушника', 'woman')
student_two.courses_in_progress += ['Python']
student_two.courses_in_progress += ['Git']

lecture_one = Lecturer('Ivan', 'Ivanov')
lecture_one.courses_attached += ['Python']

lecture_two = Lecturer('Darya', 'Jukova')
lecture_two.courses_attached += ['Git']

reviewer_one = Reviewer('Василий', 'Шукшин')
reviewer_one.courses_attached += ['Python']
reviewer_one.rate_hw(student_one, 'Python', 5)
reviewer_one.rate_hw(student_two, 'Python', 7)

reviewer_two = Reviewer('Андрей', 'Свиридов')
reviewer_two.courses_attached += ['Python']
reviewer_two.rate_hw(student_one, 'Python', 7)
reviewer_two.rate_hw(student_two, 'Python', 9)


student_one.raiting(lecture_one, 'Python', 9)
student_one.raiting(lecture_two, 'Python', 9)
student_two.raiting(lecture_one, 'Python', 8)
student_two.raiting(lecture_two, 'Python', 8)


# some_reviewer = Reviewer('Василий', 'Шукшин')
# some_reviewer.courses_attached += ['Python']
# some_reviewer.rate_hw(best_student, 'Python', 5)
# some_reviewer.rate_hw(best_student, 'Python', 7)

print(student_one)
print(lecture_one)
print(reviewer_one)
print(student_two)
print(lecture_two)
print(reviewer_two)

print(lecture_one.sravni(lecture_two))
print(student_one.sravni(student_two))

test_list = [student_one, student_two]
avg_all_students(test_list, 'Python')

test_list2 = [lecture_one, lecture_two]
avg_all_lecturers(test_list2, 'Python')