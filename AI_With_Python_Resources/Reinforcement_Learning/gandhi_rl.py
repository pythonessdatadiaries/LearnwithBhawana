import random

# Possible actions Gandhi ji can take
actions = ["violence", "non_violence"]

# Q-values (initially zero)
q_values = {"violence": 0, "non_violence": 0}

# Reward system:
# - Violence → -10 (logon ka support kam, protest fail)
# - Non-Violence → +10 (support badhta hai, unity milti hai)
def get_reward(action):
    if action == "non_violence":
        return 10
    else:
        return -10

print("🕊 Training Gandhi-Style RL Model...\n")

# Train for few iterations (episodes)
for episode in range(10):
    action = random.choice(actions)   # try actions randomly (trial and error)
    reward = get_reward(action)       # receive feedback
    q_values[action] = q_values[action] + 0.5 * (reward - q_values[action])  # learn

    print(f"Episode {episode + 1}: Action = {action}, Reward = {reward}")

print("\n✅ Final Learned Q-Values:", q_values)
best_action = max(q_values, key=q_values.get)
print(f"\nGandhi-style RL ke hisaab se best policy: '{best_action}'")