"""学习 lstm autoencoder"""
from keras.models import Sequential
from numpy import array
from keras.models import Model
from keras.layers import Input
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from keras.utils import plot_model

# "首先是recreate sequence"
# # define input sequence
# sequence = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# # reshape input into [samples, timesteps, features]
# n_in = len(sequence)
# sequence = sequence.reshape((1, n_in, 1))
# # define model
# model = Sequential()
# model.add(LSTM(100, activation='relu', input_shape=(n_in, 1)))
# model.add(RepeatVector(n_in))
# model.add(LSTM(100, activation='relu', return_sequences=True))
# model.add(TimeDistributed(Dense(1)))
# model.compile(optimizer='adam', loss='mse')
# print(model.summary())
# # fit model
# model.fit(sequence, sequence, epochs=300, verbose=2)
# plot_model(model, show_shapes=True, to_file='reconstruct_lstm_autoencoder.png')
# # demonstrate recreation
# yhat = model.predict(sequence, verbose=0)
# print(yhat[0, :, 0])

# "然后是使用autoencoder预测"
# # lstm autoencoder predict sequence
# # define input sequence
# seq_in = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# # reshape input into [samples, timesteps, features]
# n_in = len(seq_in)
# seq_in = seq_in.reshape((1, n_in, 1))
# # prepare output sequence
# seq_out = seq_in[:, 1:, :]
# n_out = n_in - 1
# # define model
# model = Sequential()
# model.add(LSTM(100, activation='relu', input_shape=(n_in, 1)))
# model.add(RepeatVector(n_out))
# model.add(LSTM(100, activation='relu', return_sequences=True))
# model.add(TimeDistributed(Dense(1)))
# model.compile(optimizer='adam', loss='mse')
# plot_model(model, show_shapes=True, to_file='predict_lstm_autoencoder.png')
# # fit model
# model.fit(seq_in, seq_out, epochs=300, verbose=2)
# # demonstrate prediction
# yhat = model.predict(seq_in, verbose=2)
# print(yhat[0, :, 0])

# "然后是使用autoencoder重构+预测"
# # lstm autoencoder reconstruct and predict sequence
# # define input sequence
# seq_in = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# # reshape input into [samples, timesteps, features]
# n_in = len(seq_in)
# seq_in = seq_in.reshape((1, n_in, 1))
# # prepare output sequence
# seq_out = seq_in[:, 1:, :]
# n_out = n_in - 1
# # define encoder
# visible = Input(shape=(n_in, 1))
# encoder = LSTM(100, activation='relu')(visible)
# # define reconstruct decoder
# decoder1 = RepeatVector(n_in)(encoder)
# decoder1 = LSTM(100, activation='relu', return_sequences=True)(decoder1)
# decoder1 = TimeDistributed(Dense(1))(decoder1)
# # define predict decoder
# decoder2 = RepeatVector(n_out)(encoder)
# decoder2 = LSTM(100, activation='relu', return_sequences=True)(decoder2)
# decoder2 = TimeDistributed(Dense(1))(decoder2)
# # tie it together
# model = Model(inputs=visible, outputs=[decoder1, decoder2])
# model.compile(optimizer='adam', loss='mse')
# plot_model(model, show_shapes=True, to_file='composite_lstm_autoencoder.png')
# # fit model
# model.fit(seq_in, [seq_in, seq_out], epochs=300, verbose=2)
# # demonstrate prediction
# yhat = model.predict(seq_in, verbose=0)
# print(yhat)

# Keep Standalone LSTM Encoder
# define input sequence
sequence = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# reshape input into [samples, timesteps, features]
n_in = len(sequence)
sequence = sequence.reshape((1, n_in, 1))
# define model
model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(n_in, 1)))
model.add(RepeatVector(n_in))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(TimeDistributed(Dense(1)))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(sequence, sequence, epochs=300, verbose=2)
# connect the encoder LSTM as the output layer
model = Model(inputs=model.inputs, outputs=model.layers[0].output)
plot_model(model, show_shapes=True, to_file='lstm_encoder.png')
# get the feature vector for the input sequence
yhat = model.predict(sequence)
print(yhat.shape)
print(yhat)
