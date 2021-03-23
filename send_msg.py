
################################ module used to run program #############################

import bs4,requests
import pandas as pd

from config import *
from time import sleep , localtime , strftime
from random import randint , random
from textblob import TextBlob 

'''
def get_short_url(url):

	response = requests.put("https://api.shorte.st/v1/data/url", {"urlToShorten":url}, headers={"public-api-token": "839bce2956f3ca8d51c4a8f7c8d1bccf"})
	
	print(response.content)

	decoded_response = json.loads(response.content)
	
	return decoded_response['shortenedUrl']
'''

# def telegram_bot_sendtext(bot_message,token):
    
#     try:

#     	#bot_chatID = '872939229'

#     	chat_id = group_id

#     	send_text = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+bot_message

#     	response = requests.get(send_text)

#     	#print(response.json())

#     except Exception as e:

#     	print(str(e))


def write_data(msg,index,name):

	#global sentiment_list

	analysis = TextBlob(msg)

	date_time = strftime("%d/%m/%Y %H:%M:%S", localtime())

	polarity = analysis.sentiment.polarity

	# with open('files/polarity'+str(number)+'.csv','a') as fp:

	# 	fp.write("\n"+str(index)+",%.2f" %(polarity))

	# with open('files/polarity0.csv','a') as fp:

	# 	fp.write("\n"+str(index)+",%.2f" %(polarity))

	sentiment = 'positive'

	if(polarity==0):
		
		sentiment = 'neutral'

		# sentiment_list[2][0]+=1
		# sentiment_list[2][number]+=1
	
	elif(polarity < -0.5):
		
		sentiment = 'Very negative'

		# sentiment_list[4][0]+=1
		# sentiment_list[4][number]+=1
	
	elif(polarity > 0.5):
		
		sentiment = 'Very positive'

		# sentiment_list[0][0]+=1
		# sentiment_list[0][number]+=1

	elif(polarity >0 and polarity<=0.5):
		
		sentiment = 'positive'

		# sentiment_list[1][0]+=1
		# sentiment_list[1][number]+=1

	else:
		
		sentiment = 'negative'

		# sentiment_list[3][0]+=1
		# sentiment_list[3][number]+=1

	Dict = {'neutral':0 , 'positive':1 , 'Very positive':2, 'negative':3 , 'Very negative':4}

	fp = open("files/group.csv","a")

	fp.write("\n"+str(index)+","+name+","+date_time+","+msg+","+str(Dict[sentiment])+","+sentiment+",%.2f" %(polarity))

	fp.close()

	fp = open("files/"+name+".csv","a")

	fp.write("\n"+str(index)+","+name+","+date_time+","+msg+","+str(Dict[sentiment])+","+sentiment+",%.2f" %(polarity))

	fp.close()


if __name__ == '__main__':

	df = pd.read_csv('files/data.csv',encoding='latin-1')

	msg_list = list(df['tweet'])

	n = 3

	#sentiment_list = [[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]

	fp = open("files/group.csv","a")

	fp.write("index,name,date_time,message,sentiment_code,sentiment,polarity")

	fp.close()

	# fp = open("files/Aman Kathait.csv","a")

	# fp.write("index,name,date_time,message,sentiment_code,sentiment,polarity")

	# fp.close()

	# fp = open("files/Akshat Negi.csv","a")

	# fp.write("index,name,date_time,message,sentiment_code,sentiment,polarity")

	# fp.close()

	fp = open("files/Shubham Semwal.csv","a")

	fp.write("index,name,date_time,message,sentiment_code,sentiment,polarity")

	fp.close()

	index = 0

	turn = 0

	for msg in msg_list:

		#turn = randint(1,90)

		if(turn%n==0):

			write_data(msg,index,'Aman Kathait')

		elif(turn%n==1):

			write_data(msg,index,'Akshat Negi')

		else:

			write_data(msg,index,'Shubham Semwal')

		#sleep(randint(1,2)*random())

		print(index)

		index+=1

	# for i in range(n):

	# 	fp = open('files/sentiment'+str(i)+'.csv','a')

	# 	total = sentiment_list[0][i] + sentiment_list[1][i] + sentiment_list[2][i] + sentiment_list[3][i] + sentiment_list[4][i]

	# 	fp.write(str(total)+","+str(sentiment_list[0][i])+","+str(sentiment_list[1][i])+","+str(sentiment_list[2][i])+","+str(sentiment_list[3][i])+","+str(sentiment_list[4][i])+"\n")

	# 	fp.close()

	