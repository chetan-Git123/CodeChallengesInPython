'''
The Student Records Manager manages student data using dictionaries and sets. 
Each student record includes their name, age, grades, and courses. 

Key operations include adding students, updating grades, checking course enrollment, calculating average grades, listing students by course, and filtering top students based on grade thresholds.
'''
# Variables
student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print('Student {name} already exists.')
    else:
        emptysetForGrades = set()
        courses_set = set(courses)
        student_records.update(
            {name : { 'age':age,'grades':emptysetForGrades,'courses':courses_set },
            }
        )
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]['courses']:
            return True
        else:
            return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    else:
        gradeSet = student_records[name]['grades']
        lenGradeSet = len(gradeSet)
        if( lenGradeSet==0 ):
            return 0
        else:
            gradeTotal = 0
            for element in  gradeSet:
                gradeTotal = gradeTotal+element
            return gradeTotal/lenGradeSet

def list_students_by_course(course):
    listOfStudentsInCourse = []
    for key in student_records:
        if course in student_records[key]['courses']:
            listOfStudentsInCourse.append(key)
    return listOfStudentsInCourse

def filter_top_students(threshold):
    listOfTopStudents = []
    for key in student_records:
        if calculate_average_grade(key)>threshold:
            listOfTopStudents.append(key)
    return listOfTopStudents

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list



