import re
import random
import spacy
import testAPI
import extractopent

nlp = spacy.load('en_core_web_sm')

# Template
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Keyword for each intent
keywords =  {
            'description' : ['description', 'information', 'about'],
            'high' : ['highest', 'high'],
            'low' : ['loweset', 'low'],
            'open' : ['open'],
            'volume' : ['volume', 'total', 'amount'],
            'sector' : ['business', 'sector'],
            }

# Response for each intent
responses = {
            'description' : ['Here are some information about {0}:',
                            'Ok, I find something about {0}:'],
            'high' : ['Today\'s highest price of {0} is:'],
            'low' : ['Today\'s lowest price of {0} is:'],
            'open' : ['Today\'s open stock price of {0} is:'],
            'volume' : ['The total volume of {0} is:'],
            'sector' : ['The business sector of {0} is:'],
            'greet' : ['Hello! I\'m here to help you. Just say the word.'],
            'goodbye': ['Bye! See you next time.',
                       'Ok, see ya!'],
            'default' : ['Sorry, I cannot answer your question. I can search the description and business sector of a company, check the total volume of a stock, and check the high/low stock price of that stock.']
            }

# Define a dictionary for patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))
# end for

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    intent = testAPI.interpreter.parse(message)['intent']['name']
    if intent in ('greet', 'goodbye'):
        matched_intent = intent
    else:
        for intent, pattern in patterns.items():
            # Check if the pattern occurs in the message
            if re.search(pattern, message):
                matched_intent = intent
    return matched_intent
# end def

# Define a respond function
def respondf(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = 'default'
    if intent in responses:
        key = intent
    if key in ('default', 'greet', 'goodbye'):
        return random.choice(responses[key])
    else: 
        if testAPI.respondI(message) != None:
            organization = extractopent.extractent(message)
            return random.choice(responses[key]).format(organization) + ' ' + testAPI.respondI(message)
        else:
            return random.choice(responses['default'])
# end def

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    #print(user_template.format(message))
    # Get the bot's response to the message
    response = respondf(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
# end def


# Print introduction message at beginning
introduction = 'Hello master, I am your stock manager, I can do following services for you:\n    1. Get the description of a company.\n    2. Show the bussiness sector of a company.\n    3. Check the stock total volume of a company.\n    4. Check today\'s high or low stock price of a company.\n    5. Check today\'s open stock price of a company.'
#company = 'Here are the companies that we can search for you:\n    Advanced Micro Devices, Inc.          AMZN                  Apple\n    BABA            Cronos Group, Inc.    Facebook              GE\n    GPRO            Micron Technology     Microsoft             NFLX\n    NVIDIA          Tesla, Inc.           The Walt Disney Co.   Twitter, Inc.' 
company = 'Here are the companies that we can search for you:\n    Advanced Micro Devices, Inc.\n    AMZN\n    Apple\n    BABA\n    Cronos Group, Inc.\n    Facebook\n    GE\n    GPRO\n    Micron Technology\n    Microsoft\n    NFLX\n    NVIDIA\n    Tesla, Inc.\n    The Walt Disney Co.\n    Twitter, Inc.'
question = 'What can I do for you today?'
'''
print()
print (bot_template.format(introduction))
print()
print (bot_template.format(company))
print()
print (bot_template.format(question))

# Loop to get input from user and answer the question
while(1):
    # Get input from user
    print()
    message = input("USER: ")
    #message = 'Would you like to show me the total volume of Cronos Group, Inc.'

    # Get the entity from extractopent
    organization = extractopent.extractent(message)
    
    # Answer the question from user
    send_message(message)

    # Check if user want to leave
    if match_intent(message) == 'goodbye':
        break;
# end while
'''
