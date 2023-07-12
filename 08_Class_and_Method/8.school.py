class Student:
    def __init__(self, name, id, clsName):
        self.name = name
        self.id = id
        self.clsName = clsName
    def __str__(self):
        return f'{self.name} {self.id}'

class Course:
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher

class Teacher:
    def __init__(self, tName, course):
        self.tName = tName
        self.course = course

class School:
    def __init__(self, name, teachers, students, courses):
        self.name = name
        self.teachers = teachers
        self.students = students
        self.courses = courses

    def get_students(self):
        for student in self.students:
            print(student.name)

    def get_teachers(self):
        for teacher in self.teachers:
            print(teacher.tName, teacher.course)


school_name = "Phitron"

ds_course = Course('Data Structure', 'Newton')
teacher_1 = Teacher('Akbar ali', ds_course)

algo_course = Course('Algorithm', 'Einstein')
teacher_2 = Teacher('Babul hossain', algo_course)

student_1 = Student('Rakib islam', 601, 6)
student_2 = Student('Ahad ali', 705, 7)
student_3 = Student('Tushar Ahammed', 803, 8)

students = [student_1, student_2, student_3]
teachers = [teacher_1, teacher_2]
courses = [ds_course, algo_course]

my_school = School(school_name, teachers, students, courses)

print(students)


# my_school.get_students()
my_school.get_teachers()



