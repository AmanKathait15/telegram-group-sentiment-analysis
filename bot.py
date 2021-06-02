
################################# imported modules ###################################

import telebot , telepot , re , os

import text2emotion as te

import pandas as pd

from textblob import TextBlob 

#from googletrans import Translator

from config import *

from matplotlib import pyplot as plt 

from random import random,randint

from time import localtime , strftime , sleep

from math import sqrt , ceil

#from flask import Flask, request,render_template,url_for


############################# End of imported modules ###########################################

"""
################# docstring for Application Class #################

######### class attributes ##########

varibale    		type            use to

index       		integer         unique number for each message fetch

bot 				telebot 		use to read chat message from chat

translator_flag		boolean			if true then translate the text else not

sentiment_flag 		boolean 		if true then bot reply sentiment result back in chat 

calculator_flag 	boolean 		if true then arithmetic expression are evaluated using eval

################# non-class function #################

function           work / task                             		run/call

send_welcome       welcome user with welcome message			run when /start command type in chat

send_report        this function send report of user  			run when /my_report or /mr command type in chat
		       	   (+ve,-ve) sentiment % and message
		       	   also send different graph images and
		       	   csv file of user


send_group_report  this function send report of each user		run when /group_report or /gr command type in chat
				   (+ve,-ve) sentiment % and message
		       	   also send different graph images and
		       	   csv file of group

show_status	       this function display list of all bot		run when /status or /help command type in chat
		       	   commands

read_chat          this is the main function it read group      call each time when text message type in chat
				   message and classify them and stored
				   them in csv file
"""

bot = telebot.TeleBot(TOKEN)

#server = Flask(__name__)

translator_flag = False

sentiment_flag  = False

calculator_flag = False

index = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):

	bot.reply_to(message, "Welcome to Group Enter text and Sentiment bot will tell the Sentiment of enter text :)")

@bot.message_handler(commands=['my_report','mr'])
def send_report(message):

	fn = message.from_user.first_name

	ln = message.from_user.last_name

	name = fn

	if(ln!=None):

		name += " "+ln

	df = pd.read_csv('files/'+name+'.csv')

	sentiment = list(df['sentiment_code'])

	total,very_positive,positive,neutral,negative,very_negative = len(sentiment),0,0,0,0,0

	for i in sentiment:

		if(i==0):
			neutral+=1
		elif(i==1):
			positive+=1
		elif(i==2):
			very_positive+=1
		elif(i==3):
			negative+=1
		else:
			very_negative+=1

	labels = ('Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100))

	sizes = (very_positive,positive,neutral,negative,very_negative)

	colors = ('green','lightgreen','yellow', 'orange', 'red')

	Theme = randint(0,3)

	if(Theme == 0):

	    plt.style.use('seaborn-whitegrid')

	elif(Theme == 1):

	    plt.style.use('dark_background') 

	else:

	    plt.style.use('classic')

	plt.figure(1)

	patches, texts = plt.pie(sizes, colors=colors, startangle=90)

	plt.legend(patches, labels, loc="best")

	plt.title('pie - chart')

	plt.axis('equal')

	plt.savefig('image_resource/'+name+'_pie.png',bbox_inches='tight')

	fig = plt.figure(2)

	axis = fig.add_subplot(1,1,1)

	X = list(df['index'])

	Y = list(df['polarity'])

	axis.scatter(X,Y)

	plt.xlabel('tweet number')

	plt.ylabel('polarity')

	plt.savefig('image_resource/'+name+'_scatter.png', bbox_inches='tight')

	plt.figure(3)

	plt.hist(Y,bins=randint(4,8),color=colors[randint(0,4)],histtype = 'barstacked')

	plt.ylabel('number of tweets')

	plt.xlabel('polarity of tweets')

	plt.savefig('image_resource/'+name+'_histogram.png', bbox_inches='tight')

	output = "\nUsername : "+name+"\nTotal   : "+str(total)+"\nVery +ve : "+str(very_positive)+"\nPositive : "+str(positive)+"\nNeutral  : "+str(neutral)+"\nNegative : "+str(negative)+"\nVery -Ve : "+str(very_negative)+"\n"

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

	sleep(0.5)

	bot.send_photo(group_id, photo=open('image_resource/'+name+'_pie.png', 'rb'))

	bot.send_photo(group_id, photo=open('image_resource/'+name+'_scatter.png', 'rb'))

	bot.send_photo(group_id, photo=open('image_resource/'+name+'_histogram.png', 'rb'))

	bot2 = telepot.Bot(TOKEN)

	bot2.sendDocument(chat_id=group_id, document=open('files/'+name+'.csv', 'rb'))

@bot.message_handler(commands=['group_report','gr'])
def send_group_report(message):

	fp = open('files/group_details.csv')

	username = fp.readlines()[-1].split(',')

	n = int(username[0])

	grid = ceil(sqrt(n))

	output = ""

	fig, axs = plt.subplots(grid, grid)

	x,y = 0,0

	Theme = randint(0,3)

	if(Theme == 0):

	    plt.style.use('seaborn-whitegrid')

	elif(Theme == 1):

	    plt.style.use('dark_background') 

	else:

	    plt.style.use('classic')

	for i in range(1,n+1):

		df = pd.read_csv('files/'+username[i]+'.csv')

		sentiment = list(df['sentiment_code'])

		total,very_positive,positive,neutral,negative,very_negative = len(sentiment),0,0,0,0,0

		for j in sentiment:

			if(j==0):
				neutral+=1
			elif(j==1):
				positive+=1
			elif(j==2):
				very_positive+=1
			elif(j==3):
				negative+=1
			else:
				very_negative+=1

		labels = ('Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100))
		
		sizes = (very_positive,positive,neutral,negative,very_negative)
		
		colors = ('green','lightgreen','yellow', 'orange', 'red')

		output += "\nUsername : "+username[i]+"\nTotal   : "+str(total)+"\nVery +ve : "+str(very_positive)+"\nPositive : "+str(positive)+"\nNeutral  : "+str(neutral)+"\nNegative : "+str(negative)+"\nVery -Ve : "+str(very_negative)+"\n"

		if(y == grid):

			x,y = x+1,0

		#print(x,y)

		patches,texts = axs[x,y].pie(sizes, colors=colors, startangle = 90 ) #angel[randint(0,6)])

		axs[x,y].legend(patches, labels, loc = 'lower right') #location[randint(0,4)])
		
		axs[x,y].set_title(username[i])

		y = y+1

	for ax in axs.flat:

		ax.label_outer()

	plt.savefig('image_resource/Compare_All_pie.png', bbox_inches='tight')

	fig, axs = plt.subplots(grid, grid)

	x,y = 0,0

	for i in range(1,n+1):

		df = pd.read_csv('files/'+username[i]+'.csv')

		X = list(range(0,len(df['polarity'])))

		Y = list(df['polarity'])

		if(y == grid):

			x,y = x+1,0

		axs[x,y].plot(X, Y)
		
		axs[x,y].set_title(username[i])

		y = y + 1

	# Hide x labels and tick labels for top plots and y ticks for right plots.
	for ax in axs.flat:

		ax.label_outer()

	plt.savefig('image_resource/Compare_All_scatter.png', bbox_inches='tight')

	fig, axs = plt.subplots(grid, grid)

	x,y = 0,0

	for i in range(1,n+1):

		df = pd.read_csv('files/'+username[i]+'.csv')

		p = list(df['polarity'])

		pol = []

		for j in p:

			pol.append(int(j * 10))

		if(y == grid):

			x,y = x+1,0

		#N,bins,patches = 
		axs[x,y].hist(pol,bins=5, edgecolor='white', linewidth=1,color=colors[randint(0,4)],histtype = 'barstacked')

		axs[x,y].set_title(username[i])

		y = y + 1

	for ax in axs.flat:

		ax.set(xlabel='polarity of tweets', ylabel='number of tweets')

	for ax in axs.flat:

		ax.label_outer()

	plt.savefig('image_resource/Compare_All_histogram.png', bbox_inches='tight')

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

	sleep(1)

	bot.send_photo(group_id, photo=open('image_resource/Compare_All_pie.png', 'rb'))

	bot.send_photo(group_id, photo=open('image_resource/Compare_All_scatter.png', 'rb'))

	bot.send_photo(group_id, photo=open('image_resource/Compare_All_histogram.png', 'rb'))

	bot2 = telepot.Bot(TOKEN)

	bot2.sendDocument(chat_id=group_id, document=open('files/Group.csv', 'rb'))

@bot.message_handler(commands=['OnLiveSentiment', 'ols'])
def show_sentiment(message):

	global sentiment_flag

	sentiment_flag = True

	bot.reply_to(message, "from now on all message live sentiment score will reply by bot \n to off this use /OffLiveSentiment or /OLS command")

@bot.message_handler(commands=['OffLiveSentiment', 'OLS'])
def hide_sentiment(message):

	global sentiment_flag

	sentiment_flag = False

	bot.reply_to(message, "Successfully off Live Sentiment")

@bot.message_handler(commands=['OnCalculator', 'oc'])
def on_calculator(message):

	global calculator_flag

	calculator_flag = True

	bot.reply_to(message, "try expression like (a*b)+(c/d) and bot will give answer \n to off this use /OffCalculator or /OC command")

@bot.message_handler(commands=['OffCalculator', 'OC'])
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
def read_chat(message):

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

		# translator = Translator(service_urls=['translate.googleapis.com'])

		# trans_msg = orig_msg

		# trans_msg = translator.translate(orig_msg).text

		# print("translated message : "+trans_msg)

		# trans_msg = re.sub(r'[,]',' ',trans_msg)

		# if(translator_flag and trans_msg!=orig_msg and trans_msg!=None):

		# 	bot.reply_to(message,trans_msg)

		# 	orig_msg = trans_msg

		# orig_msg = trans_msg

		if(calculator_flag):

			try:
				
				#exp = str(eval(exp))

				exp = re.sub(r'[=]','==',trans_msg)

				exp = re.sub(r'[\^]','**',exp)

				exp = re.sub(r'[^0-9\*\(\)-+/%]','',exp)

				if(len(exp)>2):

					bot.reply_to(message,str(eval(exp)))
			
			except Exception as e:
				
				print(str(e))

				#raise e

		analysis = TextBlob(orig_msg)

		polarity = analysis.sentiment.polarity

		sentiment = 'positive'

		sc = '0'

		#bot2 = telepot.Bot(TOKEN)

		if(polarity==0):
			
			sentiment = 'neutral'
		
		elif(polarity < -0.5):
			
			sentiment, sc = 'Very negative', '4'

			if(polarity < -0.8):

				bot.reply_to(message,'Warning !!!!! \n you are using toxic language if you continue this you will get banned .')

				#bot2.deleteMessage(chat_id,msg_id)
		
		elif(polarity > 0.5):
			
			sentiment , sc = 'Very positive' , '2'

		elif(polarity >0 and polarity<=0.5):
			
			sentiment , sc = 'positive' , '1'

		else:
			
			sentiment , sc = 'negative' , '3'

		output = "\n\nSentiment : "+sentiment+"\nSentiment Score : % .2f" %(polarity)

		emotion = te.get_emotion(orig_msg)

		output += "\n\n<<<<  Emotions >>>>\n\nHappy    : " + str(emotion['Happy']) + \
				  "\nAngry    : " + str(emotion['Angry']) + \
				  "\nSurprise : " + str(emotion['Surprise']) + \
				  "\nSad      : " + str(emotion['Sad']) + \
				  "\nFear     : " + str(emotion['Fear'])

		if(sentiment_flag):

			bot.reply_to(message,output)

			total = emotion['Happy'] + emotion['Angry'] + emotion['Surprise'] + emotion['Sad'] + emotion['Fear']

			labels = ('Happy {:.2f} %'.format(emotion['Happy']/total*100) , 'Angry {:.2f} %'.format(emotion['Angry']/total*100) ,'Surprise {:.2f} %'.format(emotion['Surprise']/total*100) , 'Sad {:.2f} %'.format(emotion['Sad']/total*100) ,'Fear {:.2f} %'.format(emotion['Fear']/total*100))

			sizes = (emotion['Happy'],emotion['Angry'],emotion['Surprise'],emotion['Sad'],emotion['Fear'])

			colors = ('yellow', 'red' , 'orange' , 'blue' , 'black')

			# Theme = randint(0,3)

			# if(Theme == 0):

			#     plt.style.use('seaborn-whitegrid')

			# elif(Theme == 1):

			#     plt.style.use('dark_background') 

			# else:

			#     plt.style.use('classic')

			plt.figure(1)

			patches, texts = plt.pie(sizes, colors=colors, startangle=90)

			plt.legend(patches, labels, loc="best")

			plt.title('Emotion-chart')

			plt.axis('equal')

			plt.savefig('image_resource/Emotions_pie.png',bbox_inches='tight')

			bot.send_photo(group_id, photo=open('image_resource/Emotions_pie.png', 'rb'))

		print(output)

		fp = open("files/Group.csv","a")

		fp.write("\n"+str(index)+","+str(name)+","+str(date_time)+","+orig_msg+","+sc+","+sentiment+",%.2f" %(polarity))

		fp.close()

		fp = open("files/"+name+".csv","a")

		fp.write("\n"+str(index)+","+str(name)+","+str(date_time)+","+orig_msg+","+sc+","+sentiment+",%.2f" %(polarity))

		fp.close()

	except Exception as e:
		
		print(str(e))

		raise e



bot.polling()


# @server.route('/' + TOKEN, methods=['POST'])
# def getMessage():
#     json_string = request.get_data().decode('utf-8')
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200


# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url=URL + TOKEN)
#     return "!", 200

# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))