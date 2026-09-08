import numpy as np

marks = np.array([[85, 78, 92],
                  [70, 65, 80],
                  [90, 88, 95],
                  [60, 72, 68],
                  [75, 80, 85]])

totalMarks = marks.sum(axis=1)
averageMarks = marks.mean(axis=1)

print("Marks of 5 students in 3 subjects:")
print(marks)
print("Total marks per student:", totalMarks)
print("Average marks per student:", averageMarks)
