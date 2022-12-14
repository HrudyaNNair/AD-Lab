import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

heart = pd.read_csv('heart_dis.csv')
heart.head()

labels= np.array(heart.loc[:, 'target'])
features= np.array(heart.iloc[:, :13]) # selecting from 'age' to 'thal'

X_train, X_test, y_train, y_test = train_test_split(features, labels,
test_size=0.3, random_state=123)

svm_linear = SVC(kernel='linear', C=0.01).fit(X_train, y_train)
print("Accuracy:", svm_linear.score(X_train, y_train)*100)
