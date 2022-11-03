#Matrix operations
import numpy as np
a = np.matrix([[1,2,3],[1,2,3],[4,5,6]])
b = np.matrix([[1,4,7],[2,1,4],[1,2,3]])
sum = a+b
diff = a-b
p = a*b
d = a.transpose()
print('Sum =\n',sum)
print('Difference =\n',diff)
print('Product =\n',p)
print('Transpose =\n',d)

#Plotting Graph using Matplotlib
import matplotlib.pyplot as plt
x = np.arange(0, 10)
y = np.arange(11, 21)
plt.scatter(x, y, c='r')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Plotting using Matplotlib')
plt.show()

#Plotting Graph using Seaborn
import matplotlib.pyplot as plt
import seaborn as sb
from seaborn import load_dataset
x=[1,2,3,4,5]
y=[6,4,7,3,2]
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.figure()
b=sb.stripplot(x,y)
b.set(xlabel='X-axis',ylabel='Y-axis')
plt.show()
