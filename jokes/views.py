from django.shortcuts import render
from django.http import HttpResponse







# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#BestMatch responsds with best annswer that chatbot is trained on
bot = ChatBot('chatbot', read_only=False, 
              logic_adapters=[
                  {
                      'import_path':'chatterbot.logic.BestMatch',
                      'default_response': 'Sorry, I do not know what that means',
                      'maximum_similarity_threshold':0.90 # checks if response has similiary of 90 percent of user asked
                      
                      
                      
                      }
                      ])
                      


#even amount of elements

greeting_start = [
    "chatterbot.corpus.english"
]


joke_convo = [
    "hi", #question
    "hi, there", #answer
    "hello",
    "hello there buddy!",
    "how are you doing?",
    "I'm good thanks, how are you?",
    "I'm just dandy",
    "I need a joke",
    "What do dentists call their x-rays? Tooth pics! If you would like another, say 'another joke'.",
    "another joke",
    "lame",
    "You are lame",
    "not funny",
    "You are not funny",
    "that is funny",
    "Thank you, I am also funny looking",
    "What did the ocean say to the other ocean? Nothing, it just waved. Another joke? say 'next joke'.",
    "next joke",
    "How does NASA organize a party? They planet! Another joke?, type 'joke'.",
    "joke",
    "What do you get from a pampered cow? Spoiled Milk!",
    "Are these even funny jokes?",
    "yes",
    "Are these even funny jokes?",
    "no",
    "Hey they are funny to me!",
    "haha",
    "these jokes are not funny",
    "Well I tried!",
    "exit",
    "Thanks for stopping by!"
    ]


to_train = ListTrainer(bot)
to_train.train(joke_convo)
to_train.train(greeting_start)

def home(request):
    return render(request, 'home.html')

def getResponse(request):
   #key from userMessage in home.htnml
   userMessage = request.GET.get('userMessage')
   chatResponse = str(bot.get_response(userMessage))
   return HttpResponse(chatResponse)