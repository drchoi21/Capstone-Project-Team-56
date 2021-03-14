from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named AITA
chatbot = ChatBot("AITA")

#enable the following code to delete trained data
#chatbot.storage.drop()

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
#    'How can I help you?',
#    'When is the exam?',
#    'Have you read the syllabus?',
#    'No, I have not',
#    'This should help get you started: sakai.rutgers.edu'
        "chatterbot.corpus.custom.myown"
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
