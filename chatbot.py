import nltk
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import string

responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! How are you feeling today?",
        "Hello! How can I assist you?"
    ],
    "feeling": [
        "I'm sorry to hear that. Can you tell me more about what's been going on?",
        "It's okay to feel that way. I'm here to listen. Tell me more.",
        "Let's talk about it. What's been troubling you?",
        "I'm here for you. It's important to express your feelings.",
        "It sounds like you're going through a tough time. I'm here to help.",
        "Feeling this way is completely normal. What has been on your mind lately?",
        "I'm here to support you. Can you share more about what you're experiencing?",
        "Sometimes talking about it can help. What's been making you feel this way?",
        "It's important to acknowledge your feelings. What has been happening recently?",
        "You are not alone. I'm here to listen. What's been going on?",
        "It sounds like you're having a hard time. Do you want to talk about it?",
        "Expressing your feelings is a good first step. Tell me more about how you're feeling.",
        "I'm here to help you work through this. Can you tell me more about your emotions?",
        "It's okay to feel overwhelmed sometimes. Let's talk about it."
    ],
    "advice": [
        "It's important to take care of yourself. Have you tried talking to a friend or a therapist?",
        "Sometimes, taking a walk or doing something you enjoy can help. Have you tried that?",
        "It's okay to ask for help. Have you considered reaching out to a professional?",
        "Practicing mindfulness or meditation can often help to manage stress. Have you tried these?",
        "Keeping a journal of your feelings can sometimes help to process them. Have you given that a try?",
        "Engaging in a hobby or activity you love can be a great way to lift your mood. What do you enjoy doing?",
        "Physical activity can improve your mood and reduce stress. Have you considered exercising?",
        "Talking to someone you trust about how you're feeling can be really helpful. Is there someone you can confide in?",
        "Sometimes, just taking a break and getting some rest can make a big difference. Have you had enough rest lately?",
        "It might help to establish a routine that includes time for relaxation and self-care. Have you tried that?",
        "Listening to your favorite music or watching a comforting show can be very soothing. What are some things that make you feel better?",
        "Have you tried reaching out to a support group or community that understands what you're going through?",
        "Setting small, manageable goals for yourself can sometimes help to build a sense of achievement. Have you set any personal goals?",
        "Reading a good book or engaging in creative activities can be very therapeutic. Have you tried these?"
    ],
    "default": [
        "I'm here for you. Tell me more.",
        "Let's talk about it. What's on your mind?",
        "I'm listening. Go ahead."
    ]
}

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# Function to generate a response
def generate_response(user_input):
    tokens = preprocess_text(user_input)
    
    if any(word in tokens for word in ["hi", "hello", "hey", "greetings", "hii"]):
        return random.choice(responses["greeting"])
    
    if any(word in tokens for word in ["sad", "depressed", "unhappy", "angry", "upset", "anxious"]):
        return random.choice(responses["feeling"])
    
    if any(word in tokens for word in ["help", "advice", "suggestion", "recommendation"]):
        return random.choice(responses["advice"])
    
    return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Mental Health Chatbot: Hello! I'm here to support you. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Mental Health Chatbot: Take care! Remember, it's always okay to ask for help.")
            break
        response = generate_response(user_input)
        print("Mental Health Chatbot:", response)

# Run the chatbot
chatbot()