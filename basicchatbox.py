from nltk.chat.util import Chat, reflections

pairs = [
    [
    [
        r"(.*)my name is (.*)",
        ["Hello :), How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["No i can't ",]
    ],
     [
        r"(.*) your name ?",
        ["I don't have one, but you can just call me maniac and I'm a chatbot .",]
    ],
    [
        r"can i call you (.*)",
        ["Noooo, i'ts a horrible name"]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well!"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Mr ghost created me using a forbiden magic from the 1278","witchcraft;)",]
    ],
    [
        r"(.*) (city) ?",
        ['Lucknow',]
    
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health, how is yours",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of all kind of sports",]
    ],
    [
        r"who (.*) (Idol)?",
        ["Hueningkai"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['ok goo away']
    ],
]
]
#default message at the start of chat
print("Hi, I'm maniac, I can help you with every question you ask. Type quit to leave and leaving me in peace ")
chat = Chat(pairs, reflections)
chat.converse()