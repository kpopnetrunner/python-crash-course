# 28_archived_messages.py

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the orignal list has
# retained its messages.

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

send_messages(messages[:], sent_messages)
print_messages(messages)
print_sent_messages(sent_messages)
