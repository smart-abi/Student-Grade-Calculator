# grade_calculator.py

def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good job! You can do even better!"
    elif marks >= 60:
        return "D", "Nice try! Keep practicing!"
    else:
        return "F", "Don't give up! Work harder and try again!"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")


# Main Program
print("="*40)
print("STUDENT GRADE CALCULATOR")
print("="*40)

name = input("Enter student name: ").upper()
marks = get_valid_marks()

grade, message = get_grade(marks)

print("\n" + "="*40)
print(f"RESULT FOR {name}")
print("="*40)
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
print("="*40)
