# 32_sandwiches.py

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the
# sandwich that's being ordered. Call the function three times, using a
# different nubmer of arguments each time.

def make_sandwich(*items):
    """Summarize the sandwich we are about to make."""
    print(f"Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'colby-jack cheese', 'wheat bread')
make_sandwich('ham', 'cheddar cheese', 'white bread')
make_sandwich('bacon', 'lettuce', 'tomatoes', 'toasted white bread')
