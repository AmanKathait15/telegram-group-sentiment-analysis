
import telebot , re

import pandas as pd

from textblob import TextBlob 

#from googletrans import Translator

from config import *

from random import random,randint

from time import localtime , strftime


bot = telebot.TeleBot(bot_token)

translator_flag = False

sentiment_flag  = False

calculator_flag = False

index = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):

	bot.reply_to(message, "Welcome to Sentiment bot enter text and this bot will tell the Sentiment of enter text :)")

@bot.message_handler(commands=['my_report','mr'])
def send_report(message):

	fn = message.from_user.first_name

	ln = message.from_user.last_name

	name = fn

	if(ln!=None):

		name += " "+ln

	df = pd.read_csv('files/Compare All.csv')

	usernames = list(df['Username'])

	i = usernames.index(name)

	output = "\n" + str(df.loc[i]) + "\n"

	df = pd.read_csv('files/'+name+'.csv')

	df = df.sort_values('polarity',ascending=False)

	output += "\nPositive Messages :\n\n"

	pol = list(df['polarity'])

	msg = list(df['message'])

	for i in range(0,10):

		if(pol[i]>0):

			output += msg[i] + "\n"

	output += "\nNegative Messages :\n\n"

	for i in range(1,11):

		if(pol[-i]<0):

			output += msg[-i] + "\n"

	print(output)

	bot.reply_to(message, output)

@bot.message_handler(commands=['group_report','gr'])
def send_group_report(message):

	df = pd.read_csv('files/Compare All.csv')

	n = len(df['Username'])

	output = "\n"

	for i in range(0,n):

		output += str(df.loc[i]) + "\n\n"

	df = pd.read_csv('files/Group.csv')

	df = df.sort_values('polarity',ascending=False)

	output += "\nPositive Messages :\n\n"

	pol = list(df['polarity'])

	msg = list(df['message'])

	for i in range(0,10):

		if(pol[i]>0):

			output += msg[i] + "\n"

	output += "\nNegative Messages :\n\n"

	for i in range(1,11):

		if(pol[-i]<0):

			output += msg[-i] + "\n"

	print(output)

	print(output)

	bot.reply_to(message, output)

@bot.message_handler(commands=['OnLiveSentiemnt', 'ols'])
def show_sentiment(message):

	global sentiment_flag

	sentiment_flag = True

	bot.reply_to(message, "from now on all message live sentiment score will reply by bot \n to off this use /OffLiveSentiment or /OLS command")

@bot.message_handler(commands=['OffLiveSentiemnt', 'OLS'])
def hide_sentiment(message):

	global sentiment_flag

	sentiment_flag = False

	bot.reply_to(message, "Successfully off Live Sentiemnt")

@bot.message_handler(commands=['OnCalculator', 'oc'])
def on_calculator(message):

	global calculator_flag

	calculator_flag = True

	bot.reply_to(message, "try expression like (a*b)+(c/d) and bot will give answer \n to off this use /OffCalculator or /OC command")

@bot.message_handler(commands=['OffLiveSentiemnt', 'OC'])
def off_calculator(message):

	global calculator_flag

	calculator_flag = False

	bot.reply_to(message, "Successfully off Calculator")

@bot.message_handler(commands=['OnTranslator', 'ot'])
def on_Translator(message):

	global translator_flag

	translator_flag = True

	bot.reply_to(message, "now all message which are not type in english ar translated to english \n to off this use /OffCalculator or /OC command")

@bot.message_handler(commands=['OffTranslator', 'OT'])
def off_Translator(message):

	global translator_flag

	translator_flag = False

	bot.reply_to(message, "Successfully off Translator")


@bot.message_handler(commands=['off'])
def turnON(message):

	global sentiment_flag,calculator_flag,translator_flag

	calculator_flag = False

	translator_flag = False

	sentiment_flag  = False

	bot.reply_to(message, "All active commands are turn off")

@bot.message_handler(commands=['on'])
def turnOFF(message):

	global sentiment_flag,calculator_flag,translator_flag

	calculator_flag = True

	translator_flag = True

	sentiment_flag  = True

	bot.reply_to(message, "All commands are turn on")

@bot.message_handler(commands=['help','status'])
def show_status(message):

	output ="All commands :\
			 \n /start\
			 \n /help\
			 \n /status\
			 \n /on\
			 \n /off\
			 \n /OnCalculator or /oc\
			 \n /OffCalculator or /OC\
			 \n /OnLiveSentiment or /ols\
			 \n /OffLiveSentiment or /OLS\
			 \n /OnTranslator or /ot\
			 \n /OffTranslator or /Ot\
			 \n /my_report or /mr\
			 \n /group_report or /gr\
			 \n\nStatus : \
			 \nLive Sentiment : "+str(sentiment_flag)+"\
			 \nCalculator : "+str(calculator_flag)+"\
			 \nTranslator : "+str(translator_flag)

	bot.reply_to(message,output)

@bot.message_handler(func=lambda message: True)
def echo_all(message):

	#print(type(message))

	global index

	print("\n <<<<<<<<< Telegram Bot is started .......... >>>>>>>>>>")

	fp = open('files/Group.csv','r')

	tmp_li = list(fp.readlines()[-1].split(','))

	index = int(tmp_li[0])

	index += 1

	try:
		msg_id = message.message_id

		date_time = strftime("%d/%m/%Y %H:%M:%S", localtime())

		print("message_id : "+str(msg_id))

		fn = message.from_user.first_name

		ln = message.from_user.last_name

		name = fn

		if(ln!=None):

			name += " "+ln

		fp = open('files/group_details.csv','r')

		usernames = fp.readlines()[-1].split(',')

		fp.close()

		if(name not in usernames):

			fp2 = open("files/"+name+".csv","w")

			fp2.write("index,name,date_time,message,sentiment_code,sentiment,polarity")

			fp2.close()

			usernames[0] = str(int(usernames[0])+1)

			with open('files/group_details.csv','w') as fp:

				output = ""

				for user in usernames:

					output += user + ','

				fp.write(output+name)

		print("user name : "+ name)

		orig_msg = message.text

		orig_msg = orig_msg.replace("\n"," ")

		print("original message : "+orig_msg)

		#translator = Translator(service_urls=['translate.googleapis.com'])

		trans_msg = orig_msg

		# trans_msg = translator.translate(orig_msg).text

		# print("translated message : "+trans_msg)

		# trans_msg = re.sub(r'[,]',' ',trans_msg)

		# if(translator_flag and trans_msg!=orig_msg):

		# 	bot.reply_to(message,trans_msg)

		# if(calculator_flag):

		# 	try:
				
		# 		#exp = str(eval(exp))

		# 		exp = re.sub(r'[=]','==',trans_msg)

		# 		exp = re.sub(r'[\^]','**',exp)

		# 		exp = re.sub(r'[^0-9\*\(\)-+/%]','',exp)

		# 		if(len(exp)>2):

		# 			bot.reply_to(message,str(eval(exp)))
			
		# 	except Exception as e:
				
		# 		print(str(e))

		# 		#raise e

		analysis = TextBlob(trans_msg)

		polarity = analysis.sentiment.polarity

		# with open('files/polarity.txt','w') as fp:

		# 	fp.write(str(index)+","+str(polarity)+"\n")

		sentiment = 'positive'

		sc = '0'

		if(polarity==0):
			
			sentiment = 'neutral'
		
		elif(polarity < -0.5):
			
			sentiment, sc = 'Very negative', '4'

			bot.reply_to(message,'Warning !!!!! \n you are using toxic language if you continue this you will get banned .')
		
		elif(polarity > 0.5):
			
			sentiment , sc = 'Very positive' , '2'

		elif(polarity >0 and polarity<=0.5):
			
			sentiment , sc = 'positive' , '1'

		else:
			
			sentiment , sc = 'negative' , '3'

		output = "Sentiment : "+sentiment+"\nSentiment Score : % .2f" %(polarity)

		if(sentiment_flag):

			bot.reply_to(message,output)

		print(output)

		fp = open("files/Group.csv","a")

		fp.write("\n"+str(index)+","+str(name)+","+str(date_time)+","+trans_msg+","+sc+","+sentiment+",%.2f" %(polarity))

		fp.close()

		fp = open("files/"+name+".csv","a")

		fp.write("\n"+str(index)+","+str(name)+","+str(date_time)+","+trans_msg+","+sc+","+sentiment+",%.2f" %(polarity))

		fp.close()

	except Exception as e:
		
		print(str(e))

		raise e

bot.polling()
