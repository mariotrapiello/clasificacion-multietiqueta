## IMPORTS ##
import scipy.sparse
import numpy as np

## IMPORTS ##

X_tr = scipy.sparse.load_npz('../Datasets/dataset/X_tr.npz')
X_tst = scipy.sparse.load_npz('../Datasets/dataset/X_tst.npz')
y_tr = np.load('../Datasets/dataset/y_tr.npy')
y_tst = np.load('../Datasets/dataset/y_tst.npy')
print (np.shape(y_tr))
print (y_tr[1345])