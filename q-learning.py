import gymnasium as gym
import numpy as np
import random

# Environment
env = gym.make("FrozenLake-v1", is_slippery=False)
Q = np.zeros((env.observation_space.n, env.action_space.n))

# Parameters
alpha, gamma, epsilon, episodes = 0.8, 0.95, 1.0, 5000

# Training
for _ in range(episodes):
    state, _ = env.reset()
    done = False
    while not done:
        action = env.action_space.sample() if random.random() < epsilon else np.argmax(Q[state])
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state
    epsilon = max(0.01, epsilon * 0.995)

# Show minimal output
print("Optimal actions for each state (0=Left,1=Down,2=Right,3=Up):")
print(np.argmax(Q, axis=1))

# Test agent path
state, _ = env.reset()
done = False
path = [state]
while not done:
    action = np.argmax(Q[state])
    state, _, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    path.append(state)

print("Path taken by agent:", path)
