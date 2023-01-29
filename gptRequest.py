# Credit to https://github.com/acheong08/

from revChatGPT.ChatGPT import Chatbot
import json

with open('config.json', 'r') as file:
	contents = file.read()
	data = json.loads(contents)

PROMPT_OPENER = "Follow these instructions precisely: Make up a completely random Reddit username unrelated to the text and write it after labeling it 'USERNAME:'. Then, based on the text provided, make up an Ask Reddit style question and write it after labeling it 'QUESTION:'. Then, based on the text provided, create a funny and interesting human-like very long reply to the question and write it after labeling it 'REPLY:'. Here is the text: "

chatbot = Chatbot(
		{
		"session_token": data['session_token']
		}, 
		conversation_id=None, 
		parent_id=None
	) # You can start a custom conversation

#response = chatbot.ask("Say hello", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

#print(response)
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }

def get_gpt_response(prompt):
	response = chatbot.ask(prompt, conversation_id=None, parent_id=None)
	return response['message']