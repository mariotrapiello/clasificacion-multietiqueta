## IMPORTS ##
import scipy.sparse
import numpy as np
import matplotlib.pyplot as pyplot
import sklearn.metrics as mtc
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MaxAbsScaler

## IMPORTS ##

X_tr = scipy.sparse.load_npz('../Datasets/dataset/X_tr.npz')
X_tst = scipy.sparse.load_npz('../Datasets/dataset/X_tst.npz')
y_tr = np.load('../Datasets/dataset/y_tr.npy')
y_tst = np.load('../Datasets/dataset/y_tst.npy')
# Se binarizan las caracteristicas 
y_tr=MultiLabelBinarizer().fit_transform(y_tr)
y_tst=MultiLabelBinarizer().fit_transform(y_tst)
# Escalado 
scaler = MaxAbsScaler().fit(X_tr)
X_tr=scaler.transform(X_tr)
X_tst=scaler.transform(X_tst)
# Clasificador
classif = OneVsRestClassifier(LogisticRegression())
classif.fit(X_tr, y_tr)
y_pred=classif.predict(X_tst)
accuracy=mtc.accuracy_score(y_tst,y_pred)
hamming=mtc.hamming_loss(y_tst,y_pred)
print(accuracy)
print(hamming)


