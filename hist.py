import matplotlib.pyplot as plt

marks = [45, 55, 60, 65, 70, 75, 80, 82, 85, 90, 95]

plt.hist(marks)
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()