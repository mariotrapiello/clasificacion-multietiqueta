from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier

clasificadores_dict ={
    0 : LogisticRegression(),
    1 : SGDClassifier(),
    2 : Perceptron(),
    3 : PassiveAggressiveClassifier()
}

parameters0 = {
    "estimator__C": [1,10,100,1000],
    "estimator__solver": ["liblinear"],
    "estimator__tol": [0.1,0.01,0.001,0.0001]
}
parameters1 = {
    "base_estimator__C": [1,4,10,100,1000],
    "base_estimator__solver": ["liblinear"],
    "base_estimator__tol": [0.1,0.01,0.001,0.0001],
    "base_estimator__max_iter":[10000]
}
parameters2 = {
    "estimator__alpha": [5e-5,1e-7,1e-8],
    "estimator__tol": [0.01,0.001,0.0001],
    "estimator__warm_start": [False,True],
    "estimator__random_state" :[42],
    "estimator__learning_rate" :["invscaling"],
    "estimator__eta0":[1,3,5,10],
    "estimator__power_t":[0.1,0.2,0.3,0.4,0.5,0.6]
}
parameters3 = {
    "base_estimator__alpha": [5e-5,1e-7,1e-8],
    "base_estimator__tol": [0.01,0.001,0.0001],
    "base_estimator__warm_start": [False,True],
    "base_estimator__random_state" :[42],
    "base_estimator__learning_rate" :["invscaling"],
    "base_estimator__eta0":[1,3,5,10],
    "base_estimator__power_t":[0.1,0.2,0.3,0.4,0.5,0.6]
}
parameters4 = {
    "estimator__penalty":[None],
    "estimator__alpha": [1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7],
    "estimator__tol": [0.01],
    "estimator__warm_start": [False],
    "estimator__eta0":[100,10,1,0.1],
    "estimator__shuffle":[False]
}
parameters5 = {
    "base_estimator__penalty":[None],
    "base_estimator__alpha": [1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7],
    "base_estimator__tol": [0.01,0.001,0.0001],
    "base_estimator__warm_start": [False, True],
    "base_estimator__eta0":[1,3,5,10],
    "base_estimator__shuffle":[True,False]
}
parameters6 = {
    "estimator__C":[0.1,1,10,100],
    "estimator__tol": [0.01,],
    "estimator__warm_start": [True,False],
    "estimator__class_weight":[None],
    "estimator__shuffle":[True],
    "estimator__average": [True],
    "estimator__loss" : ["hinge"]
}
parameters7 = {
    "base_estimator__C":[0.1,1,10,100],
    "base_estimator__tol": [0.1,0.01,0.001],
    "base_estimator__warm_start": [True,False],
    "base_estimator__class_weight":[None],
    "base_estimator__shuffle":[True,False],
    "base_estimator__average": [True,False,10,50,100],
    "base_estimator__loss" : ["hinge","squared_hinge"]
}


parametros_dict ={
    (clasificadores_dict[0],0) : parameters0,
    (clasificadores_dict[0],1) : parameters1,
    (clasificadores_dict[1],0) : parameters2,
    (clasificadores_dict[1],1) : parameters3,
    (clasificadores_dict[2],0) : parameters4,
    (clasificadores_dict[2],1) : parameters5,
    (clasificadores_dict[3],0) : parameters6,
    (clasificadores_dict[3],1) : parameters7
}

