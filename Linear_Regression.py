import matplotlib.pyplot as plt
from scipy import stats
from sklearn import datasets
iris=datasets.load_iris()
y=iris.data[0:,1:2]
x=iris.data[:,:1]
a=x.reshape(-1)
b=y.reshape(-1)
X=list(a)
Y=list(b)
slope, intercept, r, p, std_err = stats.linregress(X,Y)

def y_value(X):
    return slope * X + intercept

model = list(map(y_value, X))
plt.title("Iris Data")
plt.scatter(X, Y)
plt.plot(X, model)
plt.xlabel("sepal length in cm")
plt.ylabel("sepal width in cm")
plt.show()

v=int(input("Enter Value of Sepal length for predict the Sepal width\t"))
print("The Predicted Values=",y_value(v))
