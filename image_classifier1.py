from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

np.random.seed(0)

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
train, test = df[df['is_train'] == True], df[df['is_train'] == False]
print('Number of training data:', len(train))
print('Number of test data:', len(test))

features = df.columns[:4]

y = pd.factorize(train['species'])[0]
y_test = pd.factorize(test['species'])[0]

clf = svm.SVC(kernel='rbf')
clf.fit(train[features], y)

preds = clf.predict(test[features])
print(accuracy_score(y_test, preds) * 100, '%')