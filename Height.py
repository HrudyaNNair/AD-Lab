import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

file=pd.read_csv("weight-height.csv")
height=file.Height
weight=file.Weight
print(height.head())
slope, intercept, r, p, std_err = stats.linregress(height,weight)
def y_value(x):
    return slope * x + intercept
model =list(map(y_value,height))
print()
print(model[1])
plt.title("Height and Weight relation of a person")
plt.scatter(height,weight,color='yellow')
plt.plot(height,model,color='r')
plt.xlabel("height in cm")
plt.ylabel("weight in cm")
plt.legend()
plt.show()
x=float(input("Enter Value of Height for predict of weight\t"))
print("The Predicted Values=",y_value(x))
