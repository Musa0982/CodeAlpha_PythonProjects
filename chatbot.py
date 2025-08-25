# Task 4: Basic Chatbot

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi"]:
            print("Bot: Hi there!")
        elif user in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great, thanks for asking.")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
