import pandas as pd
yelp = pd.read_csv('yelp.csv')
yelp.head(4)
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14
feature_cols=['cool', 'useful', 'funny']
yelp['length'] = yelp.text.apply(len)
yelp['love'] = yelp.text.str.contains('love', case=False).astype(int)
yelp['hate'] = yelp.text.str.contains('hate', case=False).astype(int)
sns.pairplot(yelp, x_vars=feature_cols, y_vars='stars',kind='reg', size=5, aspect=0.7)
print(yelp.groupby('stars').mean())
print(sns.heatmap(yelp.corr()))
print(yelp.corr())
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np
def train_test(feature_cols) : 
    X=yelp[feature_cols]
    y=yelp.stars
    linreg=LinearRegression()
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=1)
    lr=linreg.fit(X_train,y_train)
    y_pred=lr.predict(X_test)
    er=np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    print(y_pred)
    return er
print(train_test(['cool', 'useful', 'funny', 'length', 'love', 'hate']))
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=50)
X1=yelp[feature_cols]
y1=yelp.stars
linreg1=LinearRegression()
X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,random_state=1)
lr1=linreg1.fit(X1_train,y1_train)
knn1=knn.fit(X1_train,y1_train)
y1_pred=knn1.predict(X1_test)
y2_pred=lr1.predict(X1_test)
er1=np.sqrt(metrics.mean_squared_error(y1_test, y1_pred))
print(' This is with KNN%f'%er1)
y_pred_class=y2_pred.round()
print (metrics.accuracy_score(y1_test, y_pred_class))
print (metrics.accuracy_score(y1_test, y1_pred))




