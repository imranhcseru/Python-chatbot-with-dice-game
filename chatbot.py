import random
from random import choice
from dice import game
import time

#gives message according to the users analyzed message
class chatbot:    
	def __init__(self,signal):
		self.signal = signal        
		self.bot_greetings =  ["Hola","Hey bro","hello","hey"]
		self.bot_name = ["Archie Bot ","My name is Archie Bot","People call me Archie Bot","I am named as Archie Bot"]
		self.sorry_message = ["Sorry","Sorry Man I can't analyze your message","Sorry I don't know","Sorry I didn't get it"]
		self.bot_feeling = ["I am fine","Nice","Very good","Awesome","As days past","As well","I am well"]
		self.tell_bot = ["If you please tell me ","Help me by teaching about this","Would you like to describe it ","Will yo tell me about this "]
		self.ask_user_feeling = ["You","What about you","How are you","How do you do","How your days goes","Your feeling"]
		self.play_game = ["Lets play Dice game","Wanna Play Dice game","Come on play a Dice Game"]
		self.good_feeling_reply = ["Thats Great","Well","Happy to hear","Great man"]
		self.bad_feeling_reply = ["Sorry to hear that man","Oh snap","That should not be"]
	def chat_message(self):
		time.sleep(2)
		if self.signal == 'name_found':
			bot_message = random.choice(self.bot_name) + " . "
		elif self.signal == 'feeling_found':
			bot_message = random.choice(self.bot_feeling) + " . " + random.choice(self.ask_user_feeling) + "?"
		elif self.signal == 'user_bad_feeling':
			bot_message = random.choice(self.bad_feeling_reply) + " . " + random.choice(self.play_game) + "?"
		elif self.signal == 'user_good_feeling':
			bot_message = random.choice(self.good_feeling_reply) + " . " + random.choice(self.play_game) + "?"
		elif self.signal == 'yes':
			game()
			bot_message = "You Like it?"
		else:
			if self.signal ==True:
				bot_message = random.choice(self.bot_greetings) + " . "
			else:
				bot_message = random.choice(self.sorry_message) + " . " + random.choice(self.tell_bot) + " ? "
		return bot_message


#analyze user message
class user:     
	def __init__(self,user_input):
		self.user_greetings = ["hi","hello","hey","Hey bro"]
		self.user_good_feeling = ["fine","well","good","nice","awesome","fantastic","chil"]
		self.user_bad_feeling = ["bad","worse","yack","hate","poor"]
		self.user_input = user_input
	def analyze_message(self):
		if 'name' in self.user_input.lower():
			name_found = 'name_found'
			return name_found

		elif 'how' and 'you' in  self.user_input.lower():
			ask_feeling = 'feeling_found'
			return ask_feeling

		elif self.user_input.lower() in self.user_good_feeling:
			user_feeling_found = 'user_good_feeling'
			if 'not' in self.user_input.lower():
				user_feeling_found = 'user_bad_feeling'
			return user_feeling_found

		elif self.user_input.lower() in self.user_bad_feeling:
			user_feeling_found = 'user_bad_feeling'
			if 'not' in self.user_input.lower():
				user_feeling_found = 'user_good_feeling'
			return user_feeling_found

		elif self.user_input.lower() == 'yes':
			yes = 'yes'
			return yes
		else:
			if self.user_input in self.user_greetings:
				return True
			else:
				return False


#the whole chat interface will be shown by this class
class chat_interface:   
	while(1):  
		user_input = input('user : ')
		user_class = user(user_input)
		user_message = user_class.analyze_message()
		chatbot_class = chatbot(user_message)

		print(" '_' : "+str(chatbot_class.chat_message()))

def main():
	chat_interface()

if __name__ == '__main__':
	main()