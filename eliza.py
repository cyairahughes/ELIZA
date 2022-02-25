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


import re
import random
# nameUnknown is used to separate the greet method from response method, after name is captured.
nameUnknown = True
# isActive is used to allow continuous input and output between user and program
isActive = True
# default name for user
default = "You"
# sets name to "You"
name = default

# a list of regular expressions and their responses for greetings
greetingPatterns = [
                            #captures name after 'i am'
                            [tuple([r"(.*)[iI] am ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?,?).?!?(.*)",
                            #captures name after 'my name is'
                            r"(.*)[Mm]y name'?s? is ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?).?!?,?(.*)",
                            #captures name after "i'm"
                            r"(.*)[iI]'?m ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?).?!?,?(.*)",
                            #captures name after 'this is'
                            "(.*)[Tt]his is ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?).?!?,?(.*)",
                            #captures name after 'it is'
                            "(.*)[Ii]t is ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?).?!?,?(.*)",
                            #captures name after "it's"
                            "(.*)[iI]t'?s ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?).?!?,?(.*)",
                            #captures name after 'am'
                            r"am ([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?).?!?,?(.*)",
                            #captures name after 'is'
                            r"(.*)is ([a-zA-Z]+).?!?.*",
                            #captures name after "'s"
                            r"(.*)'s ([a-zA-Z]+).?!?,?(.*)"]),
                            #appropriate responses to captured name
                     tuple([r"Alright, \2 how are you today?", r"Nice to meet you, \2, how can I help you?",
                            r"Is there anything you would like to discuss, \2?", r"How are you feeling, \2?",
                            r"A pleasure to meet you, \2, what shall we discuss?"])],
                            #sentences that do not give a name, two empty capture blocks are used to prevent errors
                    [tuple(['()?()?.*[Hh]+[iI]+.*', '()?()?.*[Hh]+[Ee]+[Yy]+.*', '()?()?.*[Hh]+[Ee]+[lL][Ll]+[oO]+.*',
                            '()?()?.*[hH]+o+w+d+y+.*']),
                            #responses to unnamed sentences
                     tuple(["A pleasure to meet you, what shall we discuss?", "How are you today?",
                            "Nice to meet you, how can I help you?"])],
                            #captures name if user just enters their name
                           [[r"(\s)?([a-zA-Z]+\.?-?'?\s?[a-zA-Z]+\.?-?'?)"],
                            #appropriate response
                           [r"Hi, \2, whats going on?"]]]

#regular patterns that a user may enter and their appropriate responses, list order corresponds to pattern rank order
regularPatterns = [
                    #captures bad words and tells the user to use more appropriate lanugage
                    [tuple([r'(.*([Ss][Hh][Ii][Tt]).*)', r'(.*([Ff][Uu][Cc][Kk]).*)', r'(.*([Dd][Aa][Mm][Nn]).*)',
                           r'(.*([Ss][Uu][Cc][Kk][Ss]?).*)', r'(.*(\b[Hh][Ee][Ll][Ll]\b).*)',
                           r'(.*([bB][iI][tT][Cc][hH]).*)',
                           r'(.*([Uu][Gg][Ll][Yy]).*)', r'(.*([hH][Aa][Tt][Ee]).*)']),
                   ["Let's use a better word.", r"\2 is not a very good word, try something else",
                     r"Lets use more positive words."]],
                    #captures 'yes or yeah' and gives an appropriate response
                   [[r"((.*)\s?([yY]es|[Yy]eah)\s?(.*))"], [r'Noted. What else?']],
                    #captures 'no' and gives an appropriate response
                   [[r"((.*)\s?(\b[nN]o\b)\s?(.*))"], [r'Explain it to me.']],
                    #captures 'sorry' and gives an appropriate response
                   [[r"((.*)\s?([sS]orry)\s?(.*))"], [r'It is okay. Lets talk about something else.']],
                    #captures question words and gives an appropriate response
                   [[r"((.*)\s?([Ww]hat|[Ww]hy|[Hh]ow|[Ww]hen|[Ww]ho|[Ww]here)\s?(is|are)?\s?.*)"],
                    [r'Why do you ask?']],
                    #given "my [blank] is [blank]" and outputs "why is your [blank][blank]
                   [[r"((.*)\s?([Mm]y) (.*) (is) (.*))"], [r'Why is your \4 \6?']],
                    #given "[blank] is [blank][blank]" and outputs "Do you think [blank] is [blank] [blank]"
                   [[r"((.*)([iI]s) (a|the|this)? (.*))"], [r'Do you think \2 is \4 \5']],
                    #given "[blank] is [blank] my[blank]" and outputs "Why is [blank] your [blank]"
                   [[r"((.*) (is) (.*) (my) (.*))"], [r'Why is \2 your \6?']],
                    #given "[blank] is [blank] your[blank]" and outputs "Why is [blank] my [blank]"
                   [[r"((.*) is (.*) your(.*))"], [r'Why is \2 my \3?']],
                    #given "[blank] is [blank]" and outputs "Why is [blank] [blank]"
                   [[r"((.*) is (.*))"], [r'Why is \2 \3?']],
                    #given "[blank] I feel [blank]" and outputs "Why do you [blank] feel [blank?"
                   [[r"((.*)\s?[iI] feels?\s?(.*))"], [r'Why do you \2 feel \3?']],
                    #appropriate response to happy contained in input
                   [[r"(.*\b[Hh]appy\b.*)"], [r'Tell me about your happiness.']],
                    #appropriate response to sad contained in input
                   [[r"(.*\b[Ss]ad\b.*)"], [r'Tell me about your sadness']],
                   #appropriate response to your favorite contained in input
                   [[r"(.*\b[Yy]our favorite\b.*)"], [r"I don't have any, do you?"]],
                   #appropriate response to favorite contained in input
                   [[r"(.*\bfavorite\b.*)"], [r'Thank you for telling me!']],
                   #appropriate response to your family member contained in input
                   [[
                        r"(.*(step-?)?\s?\b([Gg]randfather'?s?|[Gg]randpa'?s?|[Gg]randma'?s?|[Gg]randmother'?s?|[fF]ather'?s?|["
                        r"mM]other'?s?|[Ss]is(ter)?'?s?|[Bb]ro(ther)?'?s?|[fF]amily'?s?|[fF]amilies|[dD]ad(ddy)?'?s?|[Mm]om(mmy)?'?s?|[Mm]a(ma)?'?s?|[Pp]a("
                        r"pa)?'?s?|[Cc]ousin'?s?|[nN]iece'?s?|[nN]ephew'?s?|[Aa]unt(ie)?'?s?|[Uu]ncle'?s?)\b.*)"],
                    [r'Tell me about your \3']],
                   #appropriate response to love contained in input
                   [[r"(.*\b[lL]ove\b.*)"], [r'Tell me more about love.']],
                   #appropriate response to think contained in input
                   [[r"(.*\b[Tt]hink\b.*)"], [r'What do you think?']],
                   #appropriate response to joke contained in input
                   [[r"(.*\b[Jj]oke\b.*)"], [r"I don't like jokes."]],
                   #appropriate response to like contained in input
                   [[r"(.*\b[lL]ike\b(.*))"], [r'Why do you like \2?.']],
                   #appropriate response to more question words contained in input
                   [[r"(.*[aA]re|[Hh]ave|[Hh]ow|[Cc]an.*)"], [r'Why do you ask?']],
                   #appropriate response to always contained in input
                   [[r"(.*[Aa]lways.*)"], [r'What in particular?']],
                   #appropriate response to nothing contained in input
                   [[r"(.*[Nn]othing.*)"], [r"I'm sure you can think of something."]],
                   #appropriate response to words that mean a specific person or thing contained in input
                   [[r"((.*)\s?([Ss]omebody|[Ss]omeone|[Ee]verybody|[Ee]veryone)\s?(.*))"],
                    [r'Who in partictular are you speaking of?']],
                   [[r"((.*)[Ss]ometimes?(.*))"], [r'Tell me a specific time.']],
                   #pattern matching input that contains 'should' and their responses
                   [[r"((.*)\s?[sS]hould a ([a-zA-Z]+)\s?(.*)\s?)"], [r'Maybe a \3 should \4.?']],
                   [[r"((.*)\s?[sS]hould my ([a-zA-Z]+)\s?(.*)\s?)"], [r'Do you think your \3 should \4?']],
                   [[r"((.*)\s?[Ss]hould [iI] (.*) (her|him|them|their|his) (.*) me\s?(.*)\s?)"],
                    [r'Do you think its a good idea \3 \4 \5 you \6?']],
                   [[r"((.*)\s?[Ss]hould [iI] (.*) (her|him|them|their|his) (.*)\s?)"],
                    [r'Do you think its a good idea to \3 \4 \5?']],
                   [[r"((.*)\s?[Ss]hould [iI] (.*)\s?)"], [r'Yes! I think you should \3.']],
                   [[r"((.*)\s?[Ii] [sS]hould (.*)\s?)"], [r'Is it a good idea to \3']],
                   #pattern matching input that contains 'will' and their responses
                   [[r"((.*)\s?[wW]ill ([a-zA-Z]+) (.*) me (.*)\s?)"],
                    [r'Why do you need to know if \3 will \4 you \5?']],
                   [[r"((.*)\s?[wW]ill ([a-zA-Z]+) (.*)\s?)"], [r'Why are you curious if \3 will \4?']],
                   [[r"((.*)\s?[wW]ill you (.*) me\s?(.*)\s?)"], [r'Maybe I will \3 you \4.']],
                   [[r"((.*)\s?[wW]ill you (.*)\s?)"], [r'Maybe I will \3.']],
                   [[r"((.*)\s?[wW]ill [iI] (.*)\s?)"], [r'Is it important for you to \3?']],
                   #pattern matching input that contains 'need' and their responses
                   [[r"((.*)\s?[iI] needs? (.*) my (.*)\s?)"], [r'Why do you need \3 your \4?']],
                   [[r"((.*)\s?[iI] needs? (.*) your (.*)\s?)"], [r'Why do you need \3 my \4?']],
                   [[r"((.*)\s?[iI] needs? (.*)\s?)"], [r'Why do you need \3?']],
                   [[r"((.*)\s?(a-zA-z+) needs? (.*)\s?)"], [r'Why does \3 need \4?']],
                   [[r"((.*)\s?you needs? (.*) my (.*)\s?)"], [r'Why do I need \3 your \4?']],
                   [[r"((.*)\s?you needs? (.*)\s?)"], [r'Why do I need \3?']],
                   #pattern matching input that contains 'what' and their responses
                   [[r"((.*)\s?[wW]hat is your (.*)\s?)"], [r'What do you thing my \3 is?']],
                   [[r"((.*)\s?[wW]hat('s)? (is)? (.*)\s?)"], [r'What do you think \5 is?']],
                   [[r"((.*)\s?[wW]hat are (.*)\s?)"], [r'What do you think \3 are?']],
                   [[r"((.*)\s?[wW]hat are your (.*)\s?)"], [r'What do you think my \3 are?']],
                   #pattern matching input that contains 'am' and their responses
                   [[r"((.*)\s?[aA][Mm] [iI] (.*)\s?)"], [r'Are you \3?']],
                   [[r"((.*)\s?[iI] [aA][Mm] (.*) [yY][Oo][Uu] (.*)\s?)"], [r'Why are you \3 me \4?']],
                   [[r"((.*)\s?[iI] [aA][Mm] (.*) (her|him|them|their|his) (.*)\s?)"], [r'Why are you \3 \4 \5?']],
                   [[r"((.*)\s?[iI] [aA][Mm] (.*) (my|our) (.*)\s?)"], [r'Why are you \3 your \5?']],
                   [[r"((.*)\s?am (.*)\s?)"], [r'Why are you \3?', r'How are you \3?']],
                   #pattern matching input that contains 'i feel' and their responses
                   [[r"((.*)\s?[Ii](.*)[fF]eel (.*)\s?)"], [r'Why do you feel \4?']],
                   #pattern matching input that contains 'i want' and their responses
                   [[r"((.*)\s?[Ii](.*)[wW]ant (.*)\s?)"],
                    [r"How do you think you will get \4?", r'Why do you want \4?']],
                   #pattern matching input that contains 'cant' and their responses
                   [[r"((.*)\s?[Ii] (.*) [Cc]an'?t (.*)\s?)"], [r"Why can't you \4?", r"Are you sure you can't \4?"]],
                   [[r"((.*)\s?([a-zA-Z]+)(.*)[Cc]an'?t (.*))"], [r"Why can't \3 \5?"]],
                   #pattern matching input that contains pronouns that are not first person and their responses
                   [[r"((.*)\s?([sS]he|\b[hH]e\b|[Tt]hey) (.*))"], [r"Why does \3 \4?"]],
                   #pattern matching input that contain 'do' or 'does' and their responses
                   [[r'((.*)\s?[dD]o you (.*) me\s?)'], [r"I'm not sure if I \3 you"]],
                   [[r'((.*)\s?[dD]o you (.*)\s?)'], [r"I do not know, do you \3?"]],
                   [[r'((.*)\s?[dD]oes (a |the [a-zA-Z]+) (.*)\s?)'], [r"Why are you wondering if \3 does \4"]],
                   #pattern matching input that contains 'can' and their responses
                   [[r'((.*)\s?[Cc]an you (.*) me(.*)\s?)'], [r"Do you think I can \3 you \4?"]],
                   [[r'((.*)\s?[Cc]an you (.*)\s?)'], [r"I do not know, can I \3"]],
                   #pattern matching input that contains'i' and 'my' and their responses
                   [[r"((.*)\s?\b[Ii]\b\s?(.*)\s?my\s?(.*))"], [r'You \3 your \4?']],
                   #pattern matching input that contains 'i' and 'me' and their responses
                   [[r"((.*)\s?(\b[Ii]\b|\b[mM]e\b)\s?(.*))"], [r'\2 you \4?']],
                   #pattern matching input that contains 'you' and their responses
                   [[r"((.*)\s?[Yy]ou\s?(.*))"], [r'\2 I \3?']],
                   #pattern matching input that contains 'eliza' and their responses
                   [[r"((.*)\s?([eE][Ll][Ii][zZ][aA])\s?(.*))"], [r'Yes?']]]

#response method that recieves a sentence, searches for pattern in regularPatterns list and possible sub-list, if a match
#is found an appropriate response is output. If not a question mark is added to the end of the sentence.

def respond(sentence):
    for patterns, answers in regularPatterns:
        for patternOptions in patterns:
            match = re.match(patternOptions, sentence)
            if match:
                result = re.sub(patternOptions, random.choice(answers), sentence)
                return result
    return sentence + "?"

#gree method that recieves a sentence, searches for pattern in greetPatterns list and possible sub-list, if a match
#is found, the possible name is saved and an appropriate response is output. If not a question mark is added to the
#end of the sentence.

def greet(sentence):
    for patterns, answers in greetingPatterns:
        for patternOptions in patterns:
            match = re.match(patternOptions, sentence)
            if match:
                match1 = re.search(patternOptions, sentence)
                if match1.group(2) == '':
                    global name
                    name = default
                else:
                    name = match1.group(2)

                result = re.sub(patternOptions, random.choice(answers), sentence)
                return result
    return sentence + "?"


# loop while isActive is not false
while isActive:
#print greeting and question to ask name
    if nameUnknown:
        print('Eliza: Hello, I am Eliza The Psychotherapist.')
        print('Eliza: What is your name?')
#get user input
        userResponse = input(name + ': ')
#if user input ends the program allow that to happen
        if userResponse.lower() in ['goodbye', 'bye', 'quit', 'exit']:
            isActive = False
#Eliza says goodbye
            print("Eliza: Goodbye")
            break
#else go to greet method
        print("Eliza: " + greet(userResponse))
        nameUnknown = False
#if name is known get user response
    userResponse = input(name + ': ')
#check if user wants to end program
    if userResponse.lower() in ['goodbye', 'bye', 'quit', 'exit']:
        isActive = False
        print("Eliza: Goodbye")
        break
#else go to respond method
    print("Eliza: " + respond(userResponse))
