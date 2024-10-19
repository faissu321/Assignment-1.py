subjects = ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Computer']
total_marks = 0

for subject in subjects:
    marks = float(input(f"Enter marks for {subject}: "))
    total_marks += marks

percentage = (total_marks / 500) * 100
print(f"Percentage: {percentage}%")

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f"Grade: {grade}")







      




