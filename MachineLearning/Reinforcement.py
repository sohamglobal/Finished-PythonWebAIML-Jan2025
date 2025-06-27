import numpy as np

# Simple patient data: [age, risk_factor]
patients = np.array([
    [30, 0.2],
    [60, 0.8],
    [45, 0.5],
    [70, 0.9],
    [50, 0.4]
])

# Actions: 0 = No Surgery, 1 = Surgery
actions = [0, 1]

# Rewards: +1 for correct decision, -1 for wrong
def get_reward(patient, action):
    age, risk = patient
    # If risk > 0.6, surgery is better
    if risk > 0.6 and action == 1:
        return 1
    elif risk <= 0.6 and action == 0:
        return 1
    else:
        return -1

# Q-table: rows for patients, columns for actions
Q = np.zeros((len(patients), len(actions)))
print("Initial Q-table:")
print(Q)
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
episodes = 100

for episode in range(episodes):
    for i, patient in enumerate(patients):
        #print("i=", i, "Patient Data:", patient)
        # Choose action (random for exploration)
        action = np.random.choice(actions)
        #print("Patient Data:", patient)
        #print("Chosen Action:", action)
        reward = get_reward(patient, action)
        #print("Reward:", reward)
        # Q-learning update
        Q[i, action] = Q[i, action] + alpha * (reward + gamma * np.max(Q[i]) - Q[i, action])

print("\nFinal Q-table after training:")
print(Q)
# Show learned policy
print("Patient Data (age, risk) | Recommended Action (0=No Surgery, 1=Surgery)")
for i, patient in enumerate(patients):
    #print(np.argmax(Q[i]))
    best_action = np.argmax(Q[i])
    print(f"{patient} | {best_action}")