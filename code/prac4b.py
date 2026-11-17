# Simple Rule-Based Chatbot

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")
    elif user == "how are you":
        print("Chatbot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Chatbot: I am a simple AI Chatbot.")
    elif user == "who created you":
        print("Chatbot: I was created using Python programming.")
    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot: Sorry, I don't understand that.")
