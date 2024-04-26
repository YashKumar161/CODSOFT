import nltk
from nltk.tokenize import word_tokenize
from responses import responses

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    
    for key, value in responses.items():
        if all(token in key.split() for token in tokens):
            return value
    
    return responses["default"]


def main():
    print("Welcome to the Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print(chatbot_response(user_input))
                break
            else:
                print("Bot:", chatbot_response(user_input))
        except KeyboardInterrupt:
            print("\nUser interrupted the conversation.")
            break
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    nltk.download('punkt')
    main()