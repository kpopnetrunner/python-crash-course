# 27_sending_messages.py

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it's printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

messages = [
    'I like TWICE.', 'I also like Itzy.', 'I like NMIXX.',
    'I also like BLACKPINK.', 'I also like fromis_9', 'I like FIFTY FIFTY too.'
]

sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Move messages to sent mesages."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def print_messages(messages):
    print("This is what is in the messages list.")
    print(messages)

def print_sent_messages(sent_messages):
    print("This is what is in the sent_messages list.")
    print(sent_messages)

send_messages(messages, sent_messages)
print_messages(messages)
print_sent_messages(sent_messages)
