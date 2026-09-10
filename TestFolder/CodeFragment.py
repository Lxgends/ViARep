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

def get_highest(students, name):
    if name in students and students[name]:
        return max(students[name])
    return None

def get_lowest(students, name):
    if name in students and students[name]:
        return min(students[name])
    return None

def print_report(students):
    for name, grades in students.items():
        avg = get_average(students, name)
        highest = get_highest(students, name)
        lowest = get_lowest(students, name)
        print(f"{name}: grades={grades}, avg={avg:.2f}, highest={highest}, lowest={lowest}")

def main():
    students = {}
    add_student(students, "Anna")
    add_student(students, "Juris")

    add_grade(students, "Anna", 8)
    add_grade(students, "Anna", 9)
    add_grade(students, "Juris", 6)
    add_grade(students, "Juris", 7)

    print_report(students)
