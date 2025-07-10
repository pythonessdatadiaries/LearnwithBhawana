"""
Python Mini Project: PyJokes Joke Generator

This mini Python project uses the pyjokes library to generate programming-related jokes using just a few lines of code.
It’s a fun way to make your CLI apps, chatbots, or tools interactive and humorous.

Before using it, install the pyjokes library using pip:
pip install pyjokes
"""

import pyjokes

joke = pyjokes.get_joke()
print(joke)

#Fetches a single joke in the given language and category.
print(pyjokes.get_joke(language='en', category='neutral')) 

print(pyjokes.get_joke(language='en', category='all')) 



#Returns a list of jokes instead of just one.
#print(pyjokes.get_jokes(language='en', category='neutral'))