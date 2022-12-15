from sklearn import tree
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
plt.figure(figsize=(18,8))
tree.plot_tree(clf)
pred = clf.predict(X_test)
print("Accuracy =", accuracy_score(pred, y_test)*100, "%")
