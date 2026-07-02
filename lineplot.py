import matplotlib.pyplot as plt
students=["Sasi","Sai","Hema","Neelima","Sravya"]
cgpa=[8.5,9.6,7.5,9.3,9.5]
plt.plot(students,cgpa)
plt.title("student data")
plt.xlabel("students")
plt.ylabel("cgpa")
plt.grid()
plt.show()