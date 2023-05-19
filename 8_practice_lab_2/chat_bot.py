"""
    Chatbot:

    Steps:
    1. input/listen
    2. process/decide
    3. output/talkBack
"""

greet_words = ['hi', 'hello', 'yo', 'hey']
bye_words = ['bye', 'tata', 'ok jaga']
bad_words = ['kutta', 'khanki', 'mangir']

def listen():
    return input("Say something: ")

def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)
    for word in broken_words:
        if word in greet_words:
            talkBack("He said greeting!")
            break
        
        elif word in bye_words:
            talkBack("He said bye")
            break

        elif word in bad_words:
            talkBack("You are bad boy! Behave yourself")
            break

def talkBack(response):
    print(response)

while True:
    command = listen()
    if command == 'final' :
        break
    decide(command)