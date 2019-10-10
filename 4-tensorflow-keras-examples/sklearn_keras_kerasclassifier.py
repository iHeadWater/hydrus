"""使用scikit-learn调用Keras生成的模型。
使用scikit-learn封装Keras的模型
使用scikit-learn对Keras的模型进行交叉验证
使用scikit-learn，利用网格搜索调整Keras模型的超参.

Keras在深度学习很受欢迎，但是只能做深度学习：Keras是最小化的深度学习库，目标在于快速搭建深度学习模型。
基于SciPy的scikit-learn，数值运算效率很高，适用于普遍的机器学习任务，提供很多机器学习工具，包括但不限于：
使用K折验证模型
快速搜索并测试超参
Keras为scikit-learn封装了KerasClassifier和KerasRegressor。
"""

# MLP for Pima Indians Dataset with 10-fold cross validation via sklearn
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import cross_val_score
import numpy
import pandas


# Function to create model, required for KerasClassifier
def create_model():
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:, 0:8]
Y = dataset[:, 8]
# create model
model = KerasClassifier(build_fn=create_model, nb_epoch=150, batch_size=10)
# evaluate using 10-fold cross validation
# TODO： 这个StratifiedKFold已经废弃了，所以参考 from sklearn.model_selection import StratifiedKFold
kfold = StratifiedKFold(y=Y, n_folds=10, shuffle=True, random_state=seed)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
