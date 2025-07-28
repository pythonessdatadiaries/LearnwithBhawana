"""
📄 For detailed code explanation and project info, please check the README.md file.
"""

import random
def generate_alias(name,purpose,domain,number_choice,custom_number) :
    name = name.lower().replace(" ","")

    keywords = {
        "job" : ["hireme","resume","recruit","cv","apply"],
        "newsletter" : ["subscribe","news","updates","digest","insight","read"],
        "freelance" : ["freelance","pro","work","dev","consultant","studio"],
        "personal" : ["me","personal","contact","info","diary","chatwithme"],
        "business":["business","company","enterprise","corp","ventures","firm"]
    }

    connectors = ["_",".","-",""]

    suffix =  random.choice(keywords.get(purpose.lower(),["connect"]))
    connector = random.choice(connectors)

    if number_choice == "random":
        number = str(random.randint(10,99))
    elif number_choice == "yes" and custom_number:
        number = str(custom_number)
    else:
        number = ""

    alias = f"{name}{connector}{suffix}{number}@{domain.lower()}"

    return alias
