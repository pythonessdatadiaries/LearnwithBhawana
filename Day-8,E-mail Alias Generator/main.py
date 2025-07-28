from email_alias_generator import generate_alias

print("Welcome to Email Alias Generator!")

user_name = input("Enter your name:")

user_purpose = input("What is this email for ?(job,newsletter,freelance,personal,business):")

available_domains = ["gmail.com","yahoo.com","outlook.com","hotmail.com"]
print("\nAvailable domains:")

for d in available_domains:
    print(f"-{d}")

user_domain = input("enter your preferred domain without @ : ").strip()
if user_domain not in available_domains:
    print("Invalid domain selected.Defaulting to gmail.com")
    user_domain = "gmail.com"

add_number = input("Do you want to include a number in your email?(yes/no)").strip().lower()

number_choice = ""
custom_number = None

if add_number == "yes":
    number_choice = input("do you want to add number manually?(yes/no)").strip().lower()
    if number_choice == "yes":
        custom_number = input("Enter the number:").strip()

        if not custom_number.isdigit():
            print("Invalid input. Using random number instead.")
            number_choice = ""
            custom_number = None
    elif number_choice == "no":
        number_choice = "random"
        custom_number = None
else:
    number_choice = None



if __name__ == "__main__":
    print("\nYour smart email alias is:\n")
    print(generate_alias(user_name,user_purpose,user_domain,number_choice,custom_number))

