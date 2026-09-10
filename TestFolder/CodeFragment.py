def add_student(students, name):
    students[name] = []
    return students

def add_grade(students, name, grade):
    if name in students:
        students[name].append(grade)
    return students

def get_average(students, name):
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    return 0