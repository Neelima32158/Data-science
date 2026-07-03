import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=np.array(["A","B","C","D","E"])
y=np.array([70,75,80,95,90])
plt.bar(x,y,color="Red")
plt.title("Students Marks")
plt.show()