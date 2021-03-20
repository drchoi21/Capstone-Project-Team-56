from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named AITA
chatbot = ChatBot("AITA")

#enable the following code to delete trained data
#chatbot.storage.drop()

trainer = ChatterBotCorpusTrainer(chatbot)

#initial training set
trainer.train(
        "chatterbot.corpus.custom.demodata"
)

#control script to control when to end the session
i = 1
while i < 2:
    question = input("Ask away:");
    if question == "Exit":
        i=3
    else:
        response = chatbot.get_response(question)
        print(response)
