class InvalidGradeError(Exception):
    pass

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def add_course(self, course_name, grade):
        if course_name not in self.courses:
            self.courses[course_name] = []
        if grade < 0 or grade > 100:
            raise InvalidGradeError(f"Invalid grade: {grade} (must be between 0 and 100)")
        self.courses[course_name].append(grade)

    # gpa for grade points average
    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0

        for course, grades in self.courses.items():
            credits = len(grades)
            total_credits += credits
            total_grade_points += sum(grades)

        if total_credits == 0:
            return 0.0
        else:
            return total_grade_points / total_credits

    def get_courses(self):
        return list(self.courses.keys())

    def get_grades(self, course_name):
        if course_name in self.courses:
            return self.courses[course_name]
        else:
            return []

    def get_name(self):
        return self.name

if __name__ == "__main__":
    # Erstellen einer Studenteninstanz
    student1 = Student("Alice")

    # Kurse hinzufügen
    student1.add_course("Math", 85)
    student1.add_course("Math", 90)
    student1.add_course("Physics", 75)
    student1.add_course("History", 80)

    # Kurse und Noten abrufen
    print(f"Student: {student1.get_name()}")
    print(f"Courses: {student1.get_courses()}")
    print(f"Grades in Math: {student1.get_grades('Math')}")
    print(f"Grades in Physics: {student1.get_grades('Physics')}")
    print(f"Grades in History: {student1.get_grades('History')}")

    # GPA berechnen
    print(f"GPA: {student1.calculate_gpa()}")
