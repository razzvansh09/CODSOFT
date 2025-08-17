import random
import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def chatbot():
    print(f"{get_greeting()} I am a chatbot. How can I assist you today?")
    
    greetings_responses = [
        "Hello! How can I help you?",
        "Hi there! What can I do for you?",
        "Hey! How’s your day going?"
    ]
    
    unknown_responses = [
        "I'm not sure I understood that. Could you try again?",
        "Hmm, I didn’t get that. Can you rephrase?",
        "Sorry, I’m still learning. Could you say that differently?"
    ]
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if "hello" in user_input or "hi" in user_input:
            print(f"Chatbot: {random.choice(greetings_responses)}")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm always ready to help!")
        
        elif "what is your name" in user_input:
            print("Chatbot: I am an upgraded chatbot created to assist you.")
        
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: The current time is {current_time}.")
        
        elif "creator" in user_input:
            print("Chatbot: I was created by a Python enthusiast just like you!")
        
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        
        elif "help" in user_input:
         print("Chatbot: Sure! What do you need help with?")
         
        else:
            print(f"Chatbot: {random.choice(unknown_responses)}")

if __name__ == "__main__":
    chatbot()
