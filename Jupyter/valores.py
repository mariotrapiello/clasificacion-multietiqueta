#from sklearn.gaussian_process.kernels import RBF
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import ClassifierChain
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

clasificadores_dict ={
    0 : LogisticRegression(),
    1 : KNeighborsClassifier(),
    2 : GaussianProcessClassifier(),
    3 : DecisionTreeClassifier(),
    4 : RandomForestClassifier(),
    5 : AdaBoostClassifier(),
    6 : GaussianNB(),
    7 : QuadraticDiscriminantAnalysis()
}

parameters0 = {
    "estimator__C": [1,10,100,1000],
    "estimator__solver": ["liblinear"],
    "estimator__tol": [0.1,0.01,0.001,0.0001]
}
parameters1 = {
    "base_estimator__C": [1,10,100,1000],
    "base_estimator__solver": ["liblinear"],
    "base_estimator__tol": [0.1,0.01,0.001,0.0001],
    "base_estimator__max_iter":[10000]
}
parameters2 = {
    "estimator__n_neighbors": [1]
}
parameters3 = {
    "base_estimator__n_neighbors": [1]
}
parameters6 = {
    "estimator__max_depth": [5,10,15]
}
parameters7 = {
    "base_estimator__splitter": ["best", "random"],
    "base_estimator__max_depth": [5,10,15],
    "base_estimator__class_with": [None, "balanced"]
}
parameters8 = {
    "estimator__n_estimators": [10,30,70,100],
    "estimator__max_depth": [5,10,15],
}
parameters9 = {
    "base_estimator__n_estimators": [10,30,70,100],
    "base_estimator__max_depth": [5,10,15],
}
parameters10 = {
    "estimator__n_estimators": [10,30,70,100],
    "estimator__algorithm": ["SAMME", "SAMME.R"]
}
parameters11 = {
    "base_estimator__n_estimators": [10,30,70,100],
    "base_estimator__algorithm": ["SAMME", "SAMME.R"]
}

parametros_dict ={
    (clasificadores_dict[0],0) : parameters0,
    (clasificadores_dict[0],1) : parameters1,
    (clasificadores_dict[1],0) : parameters2,
    (clasificadores_dict[1],1) : parameters3,
    (clasificadores_dict[3],0) : parameters6,
    (clasificadores_dict[3],1) : parameters7,
    (clasificadores_dict[4],0) : parameters8,
    (clasificadores_dict[4],1) : parameters9,
    (clasificadores_dict[5],0) : parameters10,
    (clasificadores_dict[5],1) : parameters11,
    (clasificadores_dict[6],0) : {},
    (clasificadores_dict[6],1) : {},
    (clasificadores_dict[7],0) : {},
    (clasificadores_dict[7],1) : {}
}

