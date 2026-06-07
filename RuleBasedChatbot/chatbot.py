from datetime import datetime

print("Welcome to Chatbot")
print("Type bye to exit")

while True:

    user = input("You: ")
    user = user.lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hi!")

    elif "how are you" in user:
        print("Bot: I am fine.")

    elif "your name" in user:
        print("Bot: My name is ChatBot.")

    elif "time" in user:
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif "python" in user:
        print("Bot: Python is a programming language.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    elif "study" in user:
        print("Bot: Study every day.")

    elif "thanks" in user or "thank you" in user:
        print("Bot: Welcome.")

    elif "bye" in user:
        print("Bot: Bye!")
        break

    else:
        print("Bot: I don't understand.")