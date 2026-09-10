def add_student(students, name):
    students[name] = []
    return students

def add_grade(students, name, grade):
    if name in students:
        students[name].append(grade)
    return students