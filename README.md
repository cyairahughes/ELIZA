# Cyaira Hughes CMSC416 2/8/22

# URL used: https://www.w3schools.com/python/python_regex.asp

# The purpose of this projects was to get more familiar with Python and using regular expressions. This program uses
# regular expressions to do word spotting on user input and transform sentences from answers into questions.
# For example, an input can be "I am not feeling okay" and a response would be "Why are you not feeling okay?"
# or another input "My mother yelled at me" would yield a response "Tell me more about your mother."

# How to run:
#    1. Download file
#    2. Find file in command prompt
#    3. Type "python eliza.py" to run program

# Sample Output:
# Eliza: Hello, I am Eliza The Psychotherapist.
# Eliza: What is your name?
# You: My name is Cyaira
# Eliza: Nice to meet you, Cyaira, how can I help you?
# Cyaira: I am not doing well today
# Eliza: Why are you not doing well today?
# Cyaira: My mom hurt my feelings
# Eliza: Tell me about your mom
# Cyaira: Should i go to bed
# Eliza: Yes! I think you should go to bed.
# Cyaira: I am stressed
# Eliza: How are you stressed?
# Cyaira: I am in a live demo
# Eliza: How are you in a live demo?
# Cyaira: Do you know the muffin man
# Eliza: I do not know, do you know the muffin man?
# Cyaira: Can you help me with homework
# Eliza: Why do you ask?
# Cyaira: goodbye
# Eliza: Goodbye

# The algorithm used to approach this problem is as follows:
# 1. The variable nameUnknown is used to separate the greet method from response method, after name is captured.
# 2. isActive allows continuous input and output between user and program.
# 3. Default name is 'You'.
# 4. Upon start, greeting message is displayed and asks user their name.
# 5. userResponse variable stores default name + user input.
# 6. If user enters 'goodbye', 'bye', 'quit', or 'exit' (case-insensitive) the program exits and 'Goodbye' is printed.
# 7. Else, userResponse is input to greet method which iterates through greeting patterns list. Ex. "Hi, My name is
#    [name]!", or "I am [name]", etc are patterns searched for.
# 8. If name is found, default name is replaced with user's name. Else, default name remains the same.
# 9. If pattern is caught using re.sub(), appropriate response is displayed. Ex. "Nice to meet you, [name], how can I help you?" or
#    just "How are you today?" if name is not given.
# 10. If pattern is not caught the user's response + '?' is displayed
# 11. Once name is captured, nameUnknown variable is set to false to no longer access greet method.
# 12. User response is prompted again for respond method.
# 13. Respond method is similar to greet method, it iterates through regularPatterns list where responses can be based
#     upon keywords or patterns that give a randomization of one or more responses. Patterns can range from simple
#     to more complex. For example, a sentence that contains the word 'love' will prompt a response of
#     'Tell me more about love', the sentence 'I am hungry today' will prompt the response 'Why are you hungry today?'
#     and the sentence "Should I ask her to marry me" will yield the response "Do you think it's a good idea to ask
#     her to marry you?"
# 5. If you type in 'goodbye', 'bye', 'quit', or 'exit' (case-insensitive) the program exits and 'Goodbye' is printed.
