import random

# Define states and actions
states = ['young_low', 'young_high', 'old_low', 'old_high']
actions = ['admit', 'dont_admit']

# Initialize Q-table
Q = {state: {action: 0 for action in actions} for state in states}

# Define rewards manually
rewards = {
    'young_low': {'admit': -1, 'dont_admit': 2},
    'young_high': {'admit': 5, 'dont_admit': -5},
    'old_low': {'admit': 0, 'dont_admit': 1},
    'old_high': {'admit': 5, 'dont_admit': -10},
}

# Parameters
alpha = 0.1     # learning rate
gamma = 0.9     # discount factor
epsilon = 0.2   # exploration rate
episodes = 500

# Training
for _ in range(episodes):
    state = random.choice(states)

    # Exploration vs exploitation
    if random.uniform(0, 1) < epsilon:
        action = random.choice(actions)
    else:
        action = max(Q[state], key=Q[state].get)

    reward = rewards[state][action]
    #print(f"State: {state}, Action: {action}, Reward: {reward}")
    print(Q)
    old_value = Q[state][action]
    #print(f"Old Value: {old_value}")
    next_max = max(Q[state].values())  # no real transition, so reuse same state

    # Q-learning update
    Q[state][action] = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)

#print("\nFinal Q-table after training:",Q)
# Show learned policy
print("Learned policy (best action per state):")
for state in states:
    best = max(Q[state], key=Q[state].get)
    print(f"{state}: {best}")
