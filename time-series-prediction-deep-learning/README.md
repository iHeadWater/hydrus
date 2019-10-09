# time series prediction with deep learning
项目混合了几个出处的代码，他们主要分析了一些时间序列预测问题。

## introduction
项目中程序包括：使用1d-cnn，根据位移传感器的时间序列数据判断人体运动的形式；根据家庭用电历史数据预测未来一周的家庭用电量等。

## 文件结构

                                         | core
                                         | data
                                         | keras-demo
                                         | lstms
                                         | saved-models
    time-series-prediction-deep-learning | .gitignore
                                         | 1d-cnn-v1.0.py
                                         | config.json
                                         | README.md
                                         | requirements.txt
                                         | run.py
                              
core文件夹目前是经典的LSTM代码，未来预备作为本项目模型调用的标准结构；
data文件夹存放数据；
keras-demo是使用keras的一些示例代码；
lstms文件夹里有各类lstm模型，下文有介绍；
saved-models文件夹用来存储训练好的模型；
.gitignore文件；
1d-cnn-v1.0.py是1d-cnn模型；
config.json是core文件夹配套的配置文件；
README.md；
requirements.txt也是core文件夹配套的配置文件；
run.py是运行core文件夹模型的主程序入口。
## models
模型主要包括：1d-cnn，lstm，encoder-decoder框架下的lstm、cnn-lstm、以及conv-lstm。
### 1d-cnn
Human Activity Recognition (HAR) with 1D Convolutional Neural Network in Python and Keras

A CNN works well for identifying simple patterns within your data which will then be used to form more complex patterns within higher layers. A 1D CNN is very effective when you expect to derive interesting features from shorter (fixed-length) segments of the overall data set and where the location of the feature within the segment is not of high relevance. This applies well to the analysis of time sequences of sensor data (such as gyroscope or accelerometer data).

In this example we will train a 1D convolutional neural network (1D CNN) to recognize the type of movement (Walking, Running, Jogging, etc.) based on a given set of accelerometer data from a mobile device carried around a person's waist.

We will use the WISDM data set (Activity Prediction) for this tutorial: http://www.cis.fordham.edu/wisdm/dataset.php
### 未完待续