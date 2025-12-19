# Student Grade Calculator
# Week 2 - Developers Arena Data Science Internship

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! 😊"
    elif marks >= 60:
        return "D", "You passed. Try to improve! 💪"
    else:
        return "F", "Don't give up. Keep practicing! 🔄"


# Input student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print(f"\n📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
