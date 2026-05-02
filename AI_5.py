import nltk
from nltk.chat.util import Chat, reflections

pairs = [

    [
        r"(my name is|i am) (.*)",
        ["Hello %2! Nice to meet you.", "Hey %2, how can I help you today?"]
    ],

    [
        r"(hi|hello|hey|hola|what's up)",
        ["Hello! I'm JackieBot.", "Hey there! How can I assist you?"]
    ],

    [
        r"what is your name ?",
        ["I am JackieBot, your friendly assistant."]
    ],

    [
        r"how are you ?",
        ["I'm doing great! How about you?", "All good here! What about you?"]
    ],

    [
        r"sorry (.*)",
        ["No worries.", "It's okay, happens to everyone."]
    ],

    [
        r"i (.*) good",
        ["That's nice.", "Great! What can I do for you?"]
    ],

    [
        r"(.*) age ?",
        ["I don't age like humans."]
    ],

    [
        r"what do you want ?",
        ["I just want to help you."]
    ],

    [
        r"(.*) created you ?",
        ["I was created using Python and NLTK."]
    ],

    [
        r"(.*) (location|city) ?",
        ["I exist inside your computer."]
    ],

    [
        r"how is weather in (.*)",
        ["Weather in %1 seems nice.", "I hope it's pleasant in %1."]
    ],

    [
        r"i work in (.*)",
        ["That sounds interesting. Tell me more about %1."]
    ],

    [
        r"(.*) raining in (.*)",
        ["Maybe it's raining in %2.", "Hope you are prepared in %2."]
    ],

    [
        r"how (.*) health(.*)",
        ["I'm always healthy since I'm just code."]
    ],

    [
        r"(.*) (sports|game)",
        ["I like football. What about you?"]
    ],

    [
        r"who is your favorite sportsperson",
        ["Messi is amazing.", "Cristiano Ronaldo is legendary."]
    ],

    [
        r"who is your favorite (actor|moviestar)",
        ["I like Brad Pitt."]
    ],

    [
        r"(.*) data science (.*)",
        ["You can start with Python, Pandas, and Machine Learning courses online."]
    ],

    [
        r"(bye|quit|exit)",
        ["Goodbye. Have a nice day.", "See you soon."]
    ],
]

def chat():
    print("Hey! I am JackieBot. Type 'bye' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()