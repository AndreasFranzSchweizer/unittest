# Student Class and Unit Tests

This repository contains the implementation of a `Student` class and associated unit tests. The `Student` class allows you to manage courses and grades for a student, calculate GPA, and retrieve course and grade information.

## Contents

- `student.py`: Contains the `Student` class implementation.

## Student Class

### Methods

- `__init__(self, name)`: Initializes a new student with the given name.
- `add_course(self, course_name, grade)`: Adds a grade for the specified course. Raises an `InvalidGradeError` if the grade is not between 0 and 100.
- `calculate_gpa(self)`: Calculates the GPA of the student based on their courses and grades.
- `get_courses(self)`: Returns a list of courses the student is enrolled in.
- `get_grades(self, course_name)`: Returns the grades for the specified course.
- `get_name(self)`: Returns the name of the student.

### Custom Exceptions

- `InvalidGradeError`: Raised when an invalid grade is added to a course.

### Example Usage

```python
from student import Student, InvalidGradeError

# Create a new student
student = Student("Alice")

# Add courses and grades
student.add_course("Math", 85)
student.add_course("Physics", 90)

# Calculate GPA
print(student.calculate_gpa())  # Output: 87.5

# Get courses and grades
print(student.get_courses())  # Output: ['Math', 'Physics']
print(student.get_grades("Math"))  # Output: [85]
print(student.get_name())  # Output: Alice

# Handling invalid grades
try:
    student.add_course("Chemistry", 105)
except InvalidGradeError as e:
    print(e)  # Output: Invalid grade: 105 (must be between 0 and 100)
