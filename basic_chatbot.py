def chatbot():
    print("Hello! I am a simple chatbot. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        elif user_input in ["how are you?", "how's it going?"]:
            print("Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")
        elif user_input in ["what is your name?", "who are you?"]:
            print("Chatbot: I am a simple chatbot created to assist you.")
        elif user_input in ["bye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
