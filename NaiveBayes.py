from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
irisData = load_iris()
x = irisData.data
y = irisData.target
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train,y_train)
y_pred = gnb.predict(x_test)
from sklearn.metrics import confusion_matrix, accuracy_score,recall_score,precision_score
ac = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy (in%) =",ac*100)
print("Confusion matrix:")
print(cm)
#from sklearn.metrics import recall_score,precision_score
recall=recall_score(y_test, y_pred, average='macro')
precision=precision_score(y_test, y_pred, average='macro')
print("Recall (in%) = ",recall*100)
print("Precision (in%) = ",precision*100)
