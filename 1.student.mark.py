def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_information():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student's name: ")
    DoB = input("Enter Date of Birth: ")
    return{"id":student_id,"name": name,"DoB": DoB}

def number_of_course():
    return int(input("Enter the number of course: "))

def course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def select_a_course_and_input_marks(students, courses, marks):
    student_id = input("Enter Student's ID: ")
    course_id = input("Enter Course ID: ")
    
    if student_id in students and course_id in courses:
        mark = float(input("Enter the student's mark for the course: "))
        marks[(student_id, course_id)] = mark
        print(f"Mark {mark} added for {students[student_id]['name']} in {courses[course_id]['name']}")
    else:
        print("No such student or course ID")

def list_courses(courses):
    print("Courses list: ")
    for course_id, course_info in courses.items():
        print(f"{course_id}: {course_info['name']}")  

def list_students(students):
    print("Students:")
    for student in students.values():
        print(f"{student['id']}: {student['name']}")

def show_student_marks(students, courses, marks):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    if student_id in students and course_id in courses:
        if (student_id, course_id) in marks:
            print(f"Mark for {students[student_id]['name']} in {courses[course_id]['name']}: {marks[(student_id, course_id)]}")
        else:
            print("No marks yet")
    else:
        print("ID not found")

#Main program:
if __name__ == "__main__":
    students = {}
    courses = {}
    marks = {}

    num_students = input_number_of_students()
    student_counter = 0

    while student_counter < num_students:
        student_info = input_student_information()
        students[student_info["id"]] = student_info
        student_counter += 1

    num_courses = number_of_course()
    course_counter = 0

    while course_counter < num_courses:
        course_info = course_information()
        courses[course_info["id"]] = course_info
        course_counter += 1

    while True:
        print("\nOptions:")
        print("1. Input student marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("5. Exit")

        choice = input("Enter what you'd like: ")

        if choice == "1":
            select_a_course_and_input_marks(students, courses, marks)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_student_marks(students, courses, marks)
        elif choice == "5":
            print("Program ended")
            break
        else:
            print("Nuh uh, only 1-5")
