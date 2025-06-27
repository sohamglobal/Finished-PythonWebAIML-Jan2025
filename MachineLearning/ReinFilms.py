import random

# Define states (movie genres)
states = ['action', 'romantic', 'comedy']

# Define actions
actions = ['watch', 'skip']

# Initialize Q-table
Q = {state: {action: 0 for action in actions} for state in states}
print("Initial Q-table:",Q)
# RL Parameters
alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.2    # exploration rate
episodes = 1000

# Define simulated reward function
def get_reward(state, action):
    if action == 'skip':
        return 0
    elif state == 'action':
        return 5
    elif state == 'comedy':
        return 3
    elif state == 'romantic':
        return -2

# Training loop
for episode in range(episodes):
    # Randomly pick a movie genre
    state = random.choice(states)
    
    # Choose action (explore vs exploit)
    if random.uniform(0, 1) < epsilon:
        action = random.choice(actions)
    else:
        action = max(Q[state], key=Q[state].get)
    
    # Get reward
    reward = get_reward(state, action)
    
    # Since we have no next state logic, use same state for simplicity
    old_value = Q[state][action]
    next_max = max(Q[state].values())

    # Q-Learning update rule
    new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
    Q[state][action] = new_value

# Print final Q-table
print("Learned Q-values:")
for state in states:
    for action in actions:
        print(f"Genre: {state}, Action: {action}, Value: {Q[state][action]:.2f}")

# Suggest best action per genre
print("\nBest action for each genre:")
for state in states:
    best_action = max(Q[state], key=Q[state].get)
    print(f"{state.title()}: {best_action}")
# This code simulates a reinforcement learning scenario where a user learns to choose movies based on genre preferences.
# The Q-table is updated based on rewards received for actions taken in different states (genres).