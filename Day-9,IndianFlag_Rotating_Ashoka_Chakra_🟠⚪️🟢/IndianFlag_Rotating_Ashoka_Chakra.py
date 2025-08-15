
"""
For Code Explanation, please refer the PDF : Indian Flag 🟠⚪️🟢 with Rotating Ashoka Chakra.pdf 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import sys



# Chakra parameters
num_spokes = 24
chakra_radius = 1.0
spoke_angles = np.linspace(0, 2 * np.pi, num_spokes, endpoint=False)

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-4, 4)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Draw the Indian flag stripes
def draw_flag():
    ax.fill_between([-4, 4], 1, 3, color='#FF9933')     # Saffron
    ax.fill_between([-4, 4], -1, 1, color='white')      # White
    ax.fill_between([-4, 4], -3, -1, color='#138808')   # Green

# Draw Chakra outline
chakra_lines = []
def init_chakra():
    circle = plt.Circle((0, 0), chakra_radius, color='#000080', fill=False, linewidth=2)
    ax.add_patch(circle)

# Animation update function
def update(frame):
    rotation = frame * (2 * np.pi / 100)
    for i, angle in enumerate(spoke_angles):
        rotated_angle = angle + rotation
        x = chakra_radius * np.cos(rotated_angle)
        y = chakra_radius * np.sin(rotated_angle)
        if frame == 0:
            line, = ax.plot([0, x], [0, y], color='#000080', lw=1)
            chakra_lines.append(line)
        else:
            chakra_lines[i].set_data([0, x], [0, y])
    return chakra_lines

# Draw flag and chakra
draw_flag()
init_chakra()

# Animate Chakra
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Typing effect in terminal
message = "🟠⚪️🟢 Proud to be Indian 🟠⚪️🟢 \n🟠⚪️🟢 Happy Independence Day 🟠⚪️🟢\n"

for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)

plt.show()
