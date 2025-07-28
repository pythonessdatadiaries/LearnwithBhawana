Email Alias Generator 📧 

This is a beginner-friendly Python project to help users create smart and unique email aliases based on the purpose of the email—such as job applications, newsletters, freelance work, personal use, or business.

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

Features ✅ 
	- Generates an email alias based on your name, purpose, and domain.
	- Adds a relevant keyword depending on your selected email purpose.
	- Gives you the choice to add:
	- a random number
	- a custom number or no number at all
	- Helps you create a professional or fun alias based on your need.

How It Works✅ 
	- You run the program via main.py, which interacts with the user.
	- It takes user inputs and passes them to generate_alias() (from email_alias_generator.py).
	- generate_alias() selects a relevant keyword and connector, and constructs the final alias in this format:

name + connector + keyword + number (optional) + @domain
Example: bhawanasaxenacv@yahoo.com

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

Code Structure 🛠 
	1.	main.py
This file handles user interaction (input/output). It’s the entry point of the project and keeps logic separate from the core alias generation logic, which is best practice in real-world coding.
It:
	- Displays domain choices
	- Takes user input
	- Validates the input
	- Calls the generate_alias() function with user data
 
	2.	email_alias_generator.py
Contains the function generate_alias():
	- Cleans and formats the name
	- Selects a keyword from a predefined list based on the email’s purpose
	- Optionally adds a number
	- Constructs the email alias

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

Sample Scenario : 
Welcome to Email Alias Generator!
Enter your name: Sam
What is this email for ?(job,newsletter,freelance,personal,business): newsletter

Available domains:
- gmail.com
- yahoo.com
- outlook.com
- hotmail.com

enter your preferred domain without @ : yahoo.com
Do you want to include a number in your email?(yes/no): yes
do you want to add number manually?(yes/no): yes
Enter the number: 098

Your smart email alias is:
sam-subscribe098@yahoo.com

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

Why Separate main.py?

In Python, separating the logic (in email_alias_generator.py) from the script that interacts with the user (main.py) follows modular programming. This helps:
	•	Reuse the logic in other apps (like a web or mobile app)
	•	Keep code organized and readable
	•	Easier to test or expand later

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

Requirements ✅ 

This project runs on any system with Python 3 installed. No external libraries required.

 

