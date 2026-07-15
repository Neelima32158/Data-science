import matplotlib.pyplot as plt
experience=[1,5,6,8]
salary=[10000,20000,35000,45000]
plt.scatter(experience,salary)
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid()
plt.show()