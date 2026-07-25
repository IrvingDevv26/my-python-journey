# Fiftieth program: Given two parallel lists (subjects and grades), use zip to
# pair each subject with its grade and print them together. zip walks both
# lists at the same time. Along the way, accumulate the grades to compute and
# display the overall average at the end.

subjects = ["Matemáticas", "Historia", "Ciencias", "Arte"]
grades = [8.5, 7.0, 9.2, 6.8]

total = 0
for subject, grade in zip(subjects, grades):
    print(f"{subject}: {grade}")
    total += grade

average = total / len(grades)
print(f"Overall average: {average}")
