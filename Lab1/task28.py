import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History"]
averageMarks = [78, 92, 85, 70]

highestMarks = max(averageMarks)

colors = []
for marks in averageMarks:
    if marks == highestMarks:
        colors.append("green")
    else:
        colors.append("skyblue")

plt.bar(subjects, averageMarks, color=colors)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()
