# Simple Rule-Based Chatbot
# This chatbot replies based on keywords it finds in what the user types.
# It doesn't "understand" language like an AI model — it just matches patterns.

def chatbot_response(user_input):
    # Convert input to lowercase and remove extra spaces
    # This way "Hello", "HELLO", and " hello " are all treated the same
    user_input = user_input.lower().strip()

    # Lists of keywords the bot will look for
    greetings = ["hi", "hello", "hey"]
    goodbyes = ["bye", "goodbye", "exit", "quit"]

    # Check if any greeting word is present in what the user typed
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    # Check if the user wants to end the conversation
    elif any(word in user_input for word in goodbyes):
        return "Goodbye! Have a great day!"

    # Check if user is asking the bot's name
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot built for my CodSoft AI internship!"

    # Check if user is asking how the bot is doing
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! How about you?"

    # Check if user wants help/instructions
    elif "help" in user_input:
        return "You can greet me, ask my name, ask how I am, or say bye to exit."

    # Personalized response — makes it clearly your own project
    elif "college" in user_input:
        return "I study CSE, final year, and built this chatbot as part of my internship."

    # Default fallback response if nothing matches
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"


def main():
    # Print a welcome message when the program starts
    print("Chatbot: Hi! Type 'bye' to exit.")

    # Keep asking for input until the user says bye/exit/quit
    while True:
        user_input = input("You: ")               # Get input from user
        response = chatbot_response(user_input)    # Get bot's reply
        print("Chatbot:", response)                # Show the reply

        # Stop the loop if user wants to exit
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


# This makes sure main() only runs when this file is run directly
# (not when imported into another file)
if __name__ == "__main__":
    main()