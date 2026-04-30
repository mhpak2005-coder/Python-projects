def simple_chatbot():
    print("Chatbot: Hello! I am a simple rule-based bot. (Type 'quit' or 'bye' to exit)")

    while True:

        user_input = input("You: ").lower().strip()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a collection of code, but I'm running perfectly! How about you?")

        elif "your name" in user_input:
            print("Chatbot: You can call me PyBot.")

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {now}.")

        elif "bye" in user_input or "quit" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break

        else:
            print("Chatbot: I'm sorry, I don't understand that yet. Can you try saying 'hello'?")

if __name__ == "__main__":
    simple_chatbot()