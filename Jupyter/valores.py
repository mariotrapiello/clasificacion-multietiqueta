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
    "estimator__C": [1],
    "estimator__solver": ["liblinear"],
    "estimator__tol": [0.01]
}
parameters1 = {
    "base_estimator__C": [4],
    "base_estimator__solver": ["liblinear"],
    "base_estimator__tol": [0.01],
}
parameters2 = {
    "estimator__alpha": [1e-8],
    "estimator__tol": [0.001],
    "estimator__warm_start": [False],
    "estimator__random_state" :[42],
    "estimator__learning_rate" :["invscaling"],
    "estimator__eta0":[1],
    "estimator__power_t":[0.3]
}
parameters3 = {
    "base_estimator__alpha": [1e-7],
    "base_estimator__tol": [0.01],
    "base_estimator__warm_start": [False],
    "base_estimator__random_state" :[42],
    "base_estimator__learning_rate" :["invscaling"],
    "base_estimator__eta0":[3],
    "base_estimator__power_t":[0.4]
}
parameters4 = {
    "estimator__alpha": [1e-1],
    "estimator__tol": [0.01],
    "estimator__warm_start": [False],
    "estimator__eta0":[1],
    "estimator__shuffle":[True]
}
parameters5 = {
    "base_estimator__penalty":[None],
    "base_estimator__alpha": [0.1],
    "base_estimator__tol": [0.01],
    "base_estimator__warm_start": [False],
    "base_estimator__eta0":[1],
    "base_estimator__shuffle":[True]
}
parameters6 = {
    "estimator__C":[0.1],
    "estimator__tol": [0.1],
    "estimator__warm_start": [False],
    "estimator__class_weight":[None],
    "estimator__shuffle":[True],
    "estimator__average": [False],
    "estimator__loss" : ["hinge"]
}
parameters7 = {
    "base_estimator__C":[0.1],
    "base_estimator__tol": [0.01],
    "base_estimator__warm_start": [True],
    "base_estimator__class_weight":[None],
    "base_estimator__shuffle":[True],
    "base_estimator__average": [10],
    "base_estimator__loss" : ["hinge"]
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

