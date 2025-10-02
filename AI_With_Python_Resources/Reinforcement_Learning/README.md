# Gandhi-Style Reinforcement Learning (RL) 🕊

## Project Overview
This is a beginner-friendly Python project that demonstrates the concept of **Reinforcement Learning (RL)** using **Mahatma Gandhi's principles** as an example. The idea is simple: Gandhi can choose between **violence** or **non-violence**, and the program learns, through **trial and error**, which action gives the best reward.  

## How It Works
- The program randomly tries actions (`violence` or `non_violence`) over several episodes.
- Each action has a reward:  
  - **Non-Violence → +10** (good for unity and support)  
  - **Violence → -10** (loss of support, failed protest)  
- The program **updates its knowledge** (Q-values) after each action.
- At the end, it recommends the **best action** according to learned experience.

## Learning Goals
- Understand **basic Reinforcement Learning** concepts like **actions, rewards, and Q-values**.
- Learn **trial and error** approach in a fun, relatable way.
- See how AI can **learn from feedback** to make better decisions.

## How to Run
```bash
python gandhi_rl.py
