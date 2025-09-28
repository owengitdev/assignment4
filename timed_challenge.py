# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#Group 4: Last-In, First-Out Logic
# 13. Balanced Symbols
# Check if the brackets in a string are balanced.
# Input: "{[()]}"
# Output: True
# Input: "{[(])}"
# Output: False

def symbols(symbol):
    symbol = set()
    for element in symbol:
        if element in symbol:
            return True
        symbol.add(element)
        symbol.pop(element)
    return False
