# Indian Flag with Rotating Ashoka Chakra (Independence Day Special 🇮🇳)

This Python project draws the Indian National Flag using **NumPy** and **Matplotlib** and animates the Ashoka Chakra to rotate, along with a typing effect message in the terminal.

Perfect for beginners who want to explore Python graphics and animations.

---

## Features
- Three-colored Tiranga (Saffron, White, and Green) using `fill_between`
- Rotating Ashoka Chakra with 24 spokes
- Smooth animation using `FuncAnimation` from Matplotlib
- Typing effect message in the terminal for a patriotic feel

---

## Requirements
Make sure you have Python 3 installed, and then install the required libraries:

```bash
pip install numpy matplotlib
```

## How to Run
	1.	Save the Python script as tiranga.py
	2.	Open a terminal in the script’s folder.
	3.	Run the script:
 
```python
python IndianFlag_Rotating_Ashoka_Chakra.py
```

	4.	Watch the flag animation and enjoy the message in your terminal.

## Code Overview
	•	draw_flag() — Draws the three horizontal stripes of the flag.
	•	init_chakra() — Draws the circular outline of the Ashoka Chakra.
	•	update(frame) — Rotates the spokes of the chakra frame-by-frame.
	•	Typing effect — Prints a patriotic message letter by letter.

## Example Output

When you run the script, you’ll see:
	1.	The Indian flag with the rotating Ashoka Chakra at the center.
	2.	A message in the terminal:

```bash
 🟠⚪️🟢 Proud to be Indian 🟠⚪️🟢
🟠⚪️🟢 Happy Independence Day 🟠⚪️🟢
```
