class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.average_grade = 0
    #Пусть будет возможность добавлять пройденные курсы:
  def add_finished_course(self, course):
    #(если, конечно, курс уже не закончен)
    if course not in self.finished_courses:
      self.finished_courses.append(course)
    #Тут записываем студента на курс:
  def add_course_in_progress(self, course):
    #(если он ещё не заканчивал этот курс)
    if course not in self.finished_courses:
      self.courses_in_progress.append(course)
      self.grades[course] = []
#---------------------------------------
  #Считаем среднюю оценку студента:
  def calc_average_grade(self):
    #Соберем все оценки студента в один список:
    all_grades = []
    #Для этого вынем их из словаря:
    for i in self.grades.keys():
      all_grades.extend(self.grades[i])
    self.average_grade = sum(all_grades) / len(all_grades)
#---------------------------------------
  def __str__(self):
    self.calc_average_grade()
    return f"Имя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"
#---------------------------------------
#Студент оценивает лектора:
  def rate_lecturer(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
      if course in lecturer.grades.keys():
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return('Ошибка')
#---------------------------------------
#Сравниваем среднюю оценку студента за задания с оценкой лектора за лекции:
  def __lt__(self, lecturer):
    self.calc_average_grade()
    lecturer.calc_average_grade()
    return self.average_grade < lecturer.average_grade
  def __gt__(self, lecturer):
    self.calc_average_grade()
    lecturer.calc_average_grade()
    return self.average_grade > lecturer.average_grade
#---------------------------------------
#---------------------------------------
class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
#---------------------------------------
#---------------------------------------
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}
    self.average_grade = 0
    #Возможность указывать курсы, к которым прикреплен лектор:
  def add_course(self, course):
    self.courses_attached.append(course)
    self.grades[course] = []
#---------------------------------------
  #Считаем среднюю оценку лектора:
  def calc_average_grade(self):
    all_grades = []
    for i in self.grades.keys():
      all_grades.extend(self.grades[i])
    self.average_grade = sum(all_grades) / len(all_grades)
#---------------------------------------
  def __str__(self):
    self.calc_average_grade()
    return f'Имя преподавателя-лектора: {self.name}\nФамилия преподавателя-лектора: {self.surname}\nСредняя оценка за лекции: {self.average_grade}\n'
#---------------------------------------
#---------------------------------------
class Reviewer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
  #Возможность указывать курсы, к которым прикреплен лектор:
  def add_course(self, course):
    self.courses_attached.append(course)
#---------------------------------------
#Проверяющий оценивает студента:
  def rate_student(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades.keys():
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'
  def __str__(self):
    return f'Имя преподавателя-проверяющего: {self.name}\nФамилия преподавателя-проверяющего: {self.surname}\n'
#---------------------------------------
#---------------------------------------
#---------------------------------------
#Сравниваем студента и лектора по их средним оценкам, используя магический метод:
def comparsion(student, lecturer):
  if isinstance(student, Student) and isinstance(lecturer, Lecturer):
    if student > lecturer:
      print(f'У студента {student.name} {student.surname} средняя оценка за д/з выше, чем у лектора {lecturer.name} {lecturer.surname} за его лекции\n')
    elif student < lecturer:
      print(f'У студента {student.name} {student.surname} средняя оценка за д/з ниже, чем у лектора {lecturer.name} {lecturer.surname} за его лекции\n')
    else:
      print(f'У студента {student.name} {lecturer.surname} и лектора {lecturer.name} {lecturer.surname} одинаковая средняя оценка за д/з и лекции соответственно\n')
  else:
    print('Ошибка! То ли студент не студент, то ли лектор не лектор\n')
#---------------------------------------
#---------------------------------------
#Считаем среднюю оценку всех студентов за конкретный курс:
def average_student_grade(course, students_list):
  all_grades_course = []
  for j in students_list:
    all_grades_course.extend(j.grades[course])
  print(f'Средняя оценка всех студентов от проверяющих по курсу {course}: {sum(all_grades_course) / len(all_grades_course)}')
#Считаем среднюю оценку всех лекторов за конкретный курс:
def average_lecturer_grade(course, lecturers_list):
  all_grades_course = []
  for j in lecturers_list:
    all_grades_course.extend(j.grades[course])
  print(f'Средняя оценка всех лекторов от студентов по курсу {course}: {sum(all_grades_course) / len(all_grades_course)}')
#---------------------------------------
#---------------------------------------
#---------------------------------------
#Представим студентов и преподавателей:
student_Sasha = Student('Alexandr', 'Smirnov', 'Male')
student_Nastya = Student('Anastasia', 'Ivanova', 'Female')
lecturer_Sergei = Lecturer('Sergei', 'Sarin')
lecturer_Anna = Lecturer('Anna', 'Kravchenko')
reviewer_George = Reviewer('George', 'Makarevich')
reviewer_Zlata = Reviewer('Zlata', 'Knyazeva')
#Запихаем их на курсы по Python, ну и до кучи припишем студентам пройденные курсы
student_Sasha.add_finished_course('Git')
student_Nastya.add_finished_course('Java')
student_Sasha.add_course_in_progress('Python')
student_Nastya.add_course_in_progress('Python')
lecturer_Sergei.add_course('Python')
lecturer_Anna.add_course('Python')
reviewer_George.add_course('Python')
reviewer_Zlata.add_course('Python')
#---------------------------------------
#Проверим все методы.
#Студенты оценивают лекторов:
student_Sasha.rate_lecturer(lecturer_Sergei, 'Python', 8)
student_Sasha.rate_lecturer(lecturer_Anna, 'Python', 5)
student_Nastya.rate_lecturer(lecturer_Sergei, 'Python', 4)
student_Nastya.rate_lecturer(lecturer_Anna, 'Python', 9)
#Проверяющие оценивают студентов:
reviewer_George.rate_student(student_Sasha, 'Python', 8)
reviewer_George.rate_student(student_Nastya, 'Python', 10)
reviewer_Zlata.rate_student(student_Sasha, 'Python', 4)
reviewer_Zlata.rate_student(student_Nastya, 'Python', 8)
#Сравним средние оценки:
comparsion(student_Sasha, lecturer_Anna) #тут результат "ниже"
comparsion(student_Nastya, lecturer_Sergei) #тут выше
comparsion(student_Sasha, lecturer_Sergei) #тут равно
#Тут сравним студента со студентом и получим ошибку
comparsion(student_Sasha, student_Nastya)
#---------------------------------------
#---------------------------------------
#Теперь выведем информацию о студентах:
print(student_Sasha)
print(student_Nastya)
#Это информация о лекторах:
print(lecturer_Sergei)
print(lecturer_Anna)
#Это информация о проверяющих:
print(reviewer_George)
print(reviewer_Zlata)
#Посчитаем оценки студентов и лекторов за курс Python:
average_student_grade('Python', [student_Sasha, student_Nastya])
average_lecturer_grade('Python', [lecturer_Sergei, lecturer_Anna])