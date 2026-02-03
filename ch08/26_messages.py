# 26_messages.py

# 8-9. Messages: Make a list containing a series of short text messages. Pass
# the list to a funciton called show_messages(), which prints each text message.

messages = [
    'I like TWICE.', 'I also like Itzy.', 'I like NMIXX.',
    'I also like BLACKPINK.', 'I also like fromis_9', 'I like FIFTY FIFTY too.'
]

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)
