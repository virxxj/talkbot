import random
import difflib

responses = {
    "hello": "Hello!",
    "hi": "Hi there!",
    "hey": "Hey!",
    "how are you": "I'm good, thank you!",
    "what's up": "Not much, just here to assist you!",
    "how's it going": "It's going well, thank you!",
    "what is your name": "My name is ChatBot.",
    "who are you": "I am an AI chatbot.",
    "what can you do": "I can answer questions, provide information, tell jokes, and more!",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the weather today": "The weather today is sunny.",
    "where are you from": "I am an AI chatbot developed by Viraaj.",
    "how old are you": "I don't have an age. I'm a computer program.",
    "what is the meaning of life": "The meaning of life is subjective and varies for each individual.",
    "what is your favorite color": "I don't have a favorite color. I'm a text-based chatbot.",
    "who is your creator": "I was created by Viraaj Kochar.",
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
    "exit": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand. Can you please rephrase or ask a different question?",
    "how can I help you": "You can ask me anything you want!",
    "tell me about yourself": "I am an AI chatbot designed to assist and provide information.",
    "what are your hobbies": "As an AI, I don't have physical hobbies, but I enjoy helping people!",
    "do you have any siblings": "No, I'm the only AI chatbot of my kind.",
    "what's your favorite food": "I don't eat, but I can help you find great recipes!",
    "tell me a fun fact": "Did you know that honey never spoils? It can last for thousands of years!",
    "what languages do you speak": "I primarily speak English, but I can understand and respond to other languages too!",
    "can you play music": "I'm sorry, I can't play music directly, but I can provide information about music.",
    "what's the capital of France": "The capital of France is Paris.",
    "where can I find good restaurants": "You can try using restaurant review websites or apps to find good restaurants in your area.",
    "tell me about the latest news": "I don't have real-time access to news, but you can check reliable news websites for the latest updates.",
    "what's your favorite movie": "As an AI, I don't have personal preferences, but I can recommend popular movies if you'd like!",
    "what's your favorite book": "I don't have personal preferences for books, but I can suggest some popular titles!",
    "what's the tallest mountain in the world": "Mount Everest is the tallest mountain in the world.",
    "can you tell me a famous quote": "Sure! Here's a quote by Albert Einstein: 'Imagination is more important than knowledge.'",
    "what's the current time": "I'm sorry, I don't have real-time access to the current time. You can check your device's clock or use an online time service.",
    "what's the population of Earth": "As of the latest estimates, the world population is over 7.9 billion people.",
    "what's the largest country in the world": "Russia is the largest country in the world by land area.",
    "how far is the moon": "The average distance from Earth to the moon is about 384,400 kilometers (238,900 miles).",
    "can you tell me a riddle": "Sure! Here's a riddle for you: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? (Answer: an echo)",
}


def get_response(message):
    message = message.lower()

    if message in responses:
        return responses[message]
    else:
        # Find the closest matching keyword using difflib
        closest_match = difflib.get_close_matches(message, responses.keys(), n=1)
        if closest_match:
            return responses[closest_match[0]]
        else:
            return responses["default"]


print("ChatBot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("ChatBot:", response)
    if user_input.lower() == "exit":
        break
