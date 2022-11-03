import statistics
lst=[1,2,6,5,3,4,2]
import numpy as np
import matplotlib.pyplot as plt
a=statistics.mean(lst)
b=statistics.median(lst)
c=statistics.mode(lst)
d=statistics.stdev(lst)
print("mean =",a)
print("median =",b)
print("mode =",c)
print("SD =",d)
print("percentile =",np.percentile(lst,25))
x = np.linspace(1,10,100)
def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
mean = np.mean(x)
sd = np.std(x)
pdf = normal_dist(x,mean,sd)
plt.plot(x,pdf , color = 'blue')
plt.title('Distribution Graph')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.show()
