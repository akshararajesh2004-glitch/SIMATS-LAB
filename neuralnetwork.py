import numpy as np

sig = lambda x: 1/(1+np.exp(-x))
dsig = lambda x: x*(1-x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
W1, b1 = np.random.rand(2,2), np.random.rand(1,2)
W2, b2 = np.random.rand(2,1), np.random.rand(1,1)
lr = 0.5

for epoch in range(10000):
    # Forward
    A1 = sig(np.dot(X,W1)+b1)
    A2 = sig(np.dot(A1,W2)+b2)
    
    # Backward
    dA2 = (y-A2)*dsig(A2)
    dW2 = np.dot(A1.T,dA2); db2 = np.sum(dA2,axis=0,keepdims=True)
    dA1 = np.dot(dA2,W2.T)*dsig(A1)
    dW1 = np.dot(X.T,dA1); db1 = np.sum(dA1,axis=0,keepdims=True)
    
    # Update
    W2 += lr*dW2; b2 += lr*db2
    W1 += lr*dW1; b1 += lr*db1

    if epoch%2000==0: print(f"Epoch {epoch}, Error: {np.mean(np.abs(y-A2)):.4f}")

print("\nTrained Output:")
print(A2)
