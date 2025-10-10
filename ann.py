import numpy as np

# Sigmoid and its derivative
def sigmoid(x): return 1/(1+np.exp(-x))
def dsigmoid(x): return x*(1-x)

# Input and Output
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])   # XOR output

# Initialize weights and bias
np.random.seed(1)
W1 = np.random.rand(2,2)
W2 = np.random.rand(2,1)

# Training
for _ in range(10000):
    # Forward Propagation
    h = sigmoid(np.dot(X,W1))
    out = sigmoid(np.dot(h,W2))
    
    # Backward Propagation
    error = y - out
    d_out = error * dsigmoid(out)
    d_h = d_out.dot(W2.T) * dsigmoid(h)
    
    # Update Weights
    W2 += h.T.dot(d_out)
    W1 += X.T.dot(d_h)

# Output
print("Final Output:\n", np.round(out,3))
 