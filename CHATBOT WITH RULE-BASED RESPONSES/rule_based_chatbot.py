import re

def chatbot():
    print("🤖 AI Chatbot: Hello! Ask me anything about AI, ML, NLP, or Deep Learning.\n(Type 'exit' to quit.)")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['exit', 'quit', 'bye']:
            print("🤖 AI Chatbot: Goodbye! 👋")
            break

        # Rule-based responses
        elif re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
            print("🤖 AI Chatbot: Hi there! How can I help you with AI today?")
        elif re.search(r'\bmachine learning\b|\bml\b', user_input):
            print("🤖 AI Chatbot: Machine Learning is a subset of AI focused on algorithms that learn from data.")
        elif re.search(r'\bdeep learning\b|\bdl\b', user_input):
            print("🤖 AI Chatbot: Deep Learning is a type of ML that uses neural networks with many layers.")
        elif re.search(r'\bnlp\b|\bnatural language processing\b', user_input):
            print("🤖 AI Chatbot: NLP helps computers understand, interpret, and generate human language.")
        elif re.search(r'\bartificial intelligence\b|\bai\b', user_input):
            print("🤖 AI Chatbot: AI is the field of making machines intelligent like humans.")
        elif re.search(r'\bthank(s)?\b|\bthank you\b', user_input):
            print("🤖 AI Chatbot: You're welcome! Let me know if you need anything else.")
        else:
            print("🤖 AI Chatbot: I'm not sure about that. Try asking me about AI, ML, NLP, or DL.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()