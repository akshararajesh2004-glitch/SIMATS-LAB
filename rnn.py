import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# 1. Prepare sequence data (example: predict next number)
X = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
y = np.array([4,5,6,7])

# 2. Reshape input to [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# 3. Build simple RNN model
model = Sequential([
    SimpleRNN(20, activation='relu', input_shape=(3,1)),
    Dense(1)
])

# 4. Compile and train
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=200, verbose=0)

# 5. Predict
test = np.array([5,6,7]).reshape((1,3,1))
print("Predicted next number:", model.predict(test)[0][0])
