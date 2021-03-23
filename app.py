
############################## modules reuired ######################################

from tkinter import *					###	used to craete GUI 
from tkinter import ttk 				###	used to craete GUI
from tkinter.filedialog import askdirectory		###	used to slecet path 

from pytube import YouTube , Playlist 			###	used to download vedio/playlist
from threading import Thread 				###	used to divide process into different threads

from time import strftime,localtime,gmtime 		###	used to find local date and time 
from urllib import request 				###	used to download thumbnail
from pathlib import Path 				###	used to default download path in compter 

import subprocess,sys,os 				###	used to craete subprocess and open other application 
							###	like vedio/audio player browser et

from matplotlib import pyplot as plt                #### used to display data in pie-chart , bar graph and scatter plot ####

from random import randint
import pandas as pd

############################# End of imported modules ###########################################

class Application(): 

    """    
    ################# docstring for TwitterClient Class #################

    varibale 	type 			use to

    query 	string 		store #tag that user enter in tag_field

    count 	integer		store number of tweets to fetch from twitter

    ploarity 	list 			store sentiment score of all tweets range from -1 to +1

    positive 	list 			store postive sentiment score of different ml model used

    negative 	list 			store negative sentiment score of different ml model used

    neutral 	list 			store neutral sentiment score of different ml model used

    model 	string 		store model which is currently selected in combobox

    nbc 	undefined   		used to store naviebayes classifier object

    rf  	undefined   		used to store random forest classifier object

    dt  	undefined   		used to store decission tree classifier object

    ################# class function #################

    function 			work / task						run/call

    __init__			this function is a constructor of TwitterClient		run when TwitterClient class object is created	
    				class and it work is to allocate memory to 
    				TwiiterClient object and initailze class variables

    authentication  		this function make connection with twitter by tweepy	run after TwitterClient object is created
    				OAuthHamdler method with the help of credentials of
    				twitter developer account

    load_dict_smileys		this function make dictionary of emoticon with 		call inside clean_tweet function
    				emoticon as key and meaning as value so can be 
    				used in preprocessing phase

    load_dict_contractions  	this function make dictionary of contractions with 	call inside clean_tweet function
    				contraction like doesn't as key and meaning (does not) 
    				as value so can be used in preprocessing phase

    clean_tweet			this function is used to preprocess data . this 	call before finding ploarity of each tweet
    				function filter tweet by removinf handle , url 
    				, retweet tag and hash tag which not useful in 
    				sentiment analysis and convert emoticon , emoji
    				and contraction to thier meaning in text

    get_tweet_sentiment 	used to find sentimet of tweet i.e positive , 		call inside get_tweets function
    				negative or neutral and append sentiment score in 
    				ploarity

    get_tweets 			this function fetched tweets by using search()	call inside back_end function
    				and then call clean_tweet() to claen tweets and
    				find sentiment score using get_tweet_sentiment()
    				and save this to fetched_tweet.csv file

    back_end			this function start the back_end process work by 	call by main_thread function
    				calling get_tweets function and changing labels 
    				value so that user can Know some magic is 
    				hapening inside

    main_thread			this function divide the process into different 	run when search button is clicked in GUI
    				threads basically it reduce the load of GUI by 
    				calling back_end in different thread 

    plot_PieChart		this function display our data in pie chart form 	run when pie chart icon clicked in GUI
    				ie show value of +ve , -ve and 0 score in our data

    plot_histogram 		this function display ploarity in histogram form 	run when histogram icon clicked in GUI
    				so that user can visualize which sentiment score
    				range tweet is more .

    scatter_plot 		this function display polarity in scatter plot 		run when scatter plot icon clicked in GUI
    				graph make easy to visualize flow of sentiments
    				of twitter users on that query

    select_model 		this function return the current value of model_list	run each time when mode_list current value changes

    select_no_of_tweets		this function return the current value of choice 	run each time when choice current value changes
				combobox 

    select_trending_tag 	this function return the vlaue of selected trending 	run each time when trending_tag combobox current
				tag out of top 10 					value changes

    clear_tag	 		this function clear the value of tag_field 		run when clear button clicked in GUI

    check_tag 			this function check tag enter is valid or not 		run when tag_field value changes

    trending_tag 		this function fetch list of top 10 trending #tag 	run when program execute
				from web and display it in trending_tag combobox

    open_twitter 		this function open twitter website in default browser 	run when twitter icon is clicked in GUI

    open_fetched_tweets 	this function open fetched_tweet csv file in your 	run when open fetched tweets button is clicked in GUI
				default text editor 

    open_log_file 		this function open log_file.csv 			run when open log file button is clicked in GUI

    open_testing_dataset 	this function open test.csv 				run when open test dataset button is clicked in GUI

    open_training_dataset 	this function open train.csv 				run when open train dataset button is clicked in GUI

    check_internet 		this function check you are connected to internet 	run before creating GUI 
				or not if not then show error message
				as this program needs internet to fetched tweets

    ################# non-class function #################

    set_bg_to_<color> 		this function change the backgroud color of GUI 	run when color icon is clicked in GUI

    if__name__=="__main__"      In this function most of GUI coding is done. 		execution of program begin from this function



    """

    def __init__(self):  

    	# attempt authentication 
    	try:

    		self.polarity = [[],[],[],[]]
    		
    		self.positive = [0,0,0,0]
    		
    		self.negative = [0,0,0,0]
    		
    		self.neutral = [0,0,0,0]


    	except Exception as e:

            print("authentication failed please check your network and try again \nerror detail : "+str(e))

            msg = str(strftime("%Y-%m-%d %H:%M:%S", localtime()))+","+str(e)+"\n" 
            
            f = open("csv_files/logbook.csv","a")

            f.write(msg)

            f.close()

    def plot_PieChart(self):

        if(select_user() == "Compare All"):

            fig, axs = plt.subplots(2, 2)

            fp0 = open('files/sentiment'+str(0)+'.csv','r')

            total,very_positive,positive,neutral,negative,very_negative = fp0.read().split(',')

            total,very_positive,positive,neutral,negative,very_negative = int(total),int(very_positive),int(positive),int(neutral),int(negative),int(very_negative)

            fp0.close()


            labels0 = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
            
            sizes0 = [very_positive,positive,neutral,negative,very_negative]
            
            colors = ['green','lightgreen','yellow', 'orange', 'red']

            fp1 = open('files/sentiment'+str(1)+'.csv','r')

            total,very_positive,positive,neutral,negative,very_negative = fp1.read().split(',')

            total,very_positive,positive,neutral,negative,very_negative = int(total),int(very_positive),int(positive),int(neutral),int(negative),int(very_negative)

            fp1.close()

            labels1 = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
            
            sizes1 = [very_positive,positive,neutral,negative,very_negative]
            
            #colors = ['green', 'orange', 'red']

            fp2 = open('files/sentiment'+str(2)+'.csv','r')

            total,very_positive,positive,neutral,negative,very_negative = fp2.read().split(',')

            total,very_positive,positive,neutral,negative,very_negative = int(total),int(very_positive),int(positive),int(neutral),int(negative),int(very_negative)

            fp2.close()

            labels2 = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
            
            sizes2 = [very_positive,positive,neutral,negative,very_negative]
            
            #colors = ['green', 'orange', 'red']

            fp3 = open('files/sentiment'+str(3)+'.csv','r')

            total,very_positive,positive,neutral,negative,very_negative = fp3.read().split(',')

            total,very_positive,positive,neutral,negative,very_negative = int(total),int(very_positive),int(positive),int(neutral),int(negative),int(very_negative)

            fp3.close()

            labels3 = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
            
            sizes3 = [very_positive,positive,neutral,negative,very_negative]
            
            #colors = ['green', 'orange', 'red']

            patches,texts = axs[0, 0].pie(sizes0, colors=colors, startangle=90)

            axs[0, 0].legend(patches, labels0, loc="upper left")
            
            axs[0, 0].set_title('All select_user')
            
            patches,texts = axs[0, 1].pie(sizes1, colors=colors, startangle=135)

            axs[0, 1].legend(patches, labels1, loc="upper right")
            
            axs[0, 1].set_title('Aman Kathait')
            
            patches,texts = axs[1, 0].pie(sizes2, colors=colors, startangle=45)

            axs[1, 0].legend(patches, labels2, loc="lower left")
            
            axs[1, 0].set_title('Akshat Negi')
            
            patches,texts = axs[1, 1].pie(sizes3, colors=colors, startangle=180)

            axs[1, 1].legend(patches, labels3, loc="lower right")
            
            axs[1, 1].set_title('Shubham Semwal')

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:
                ax.label_outer()

            plt.show()

        else:

        	    #number = randint(0,4)
        	    number = select_user()

        	    df = pd.read_csv('files/'+str(user.get())+'.csv')

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

        	    #total,very_positive,positive,neutral,negative,very_negative = int(total),int(very_positive),int(positive),int(neutral),int(negative),int(very_negative)

        	    labels = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
        	    
        	    sizes = [very_positive,positive,neutral,negative,very_negative]
        	    
        	    colors = ['green','lightgreen','yellow', 'orange', 'red']
        	    
        	    plt.figure(1)
        	    
        	    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        	    
        	    plt.legend(patches, labels, loc="best")
        	    
        	    plt.title('pie - chart')
        	    
        	    plt.axis('equal')
        	    
        	    plt.show()



    def scatter_plot(self):

        if(select_user() == 'Compare All'):

            fig, axs = plt.subplots(2, 2)

            x = array(range(0,len(self.polarity[0])))
            
            y = array(self.polarity[0])

            x1 = array(range(0,len(self.polarity[1])))
            
            y1 = array(self.polarity[1])

            x2 = array(range(0,len(self.polarity[2])))
            
            y2 = array(self.polarity[2])

            x3 = array(range(0,len(self.polarity[3])))
            
            y3 = array(self.polarity[3])

            axs[0, 0].plot(x, y)
            
            axs[0, 0].set_title('group')
            
            axs[0, 1].plot(x1, y1, 'tab:orange')
            
            axs[0, 1].set_title('Aman Kathait')
            
            axs[1, 0].plot(x2, y2, 'tab:green')
            
            axs[1, 0].set_title('Akshat Negi')
            
            axs[1, 1].plot(x3, y3, 'tab:red')
            
            axs[1, 1].set_title('Shubham Semwal')

            for ax in axs.flat:
                ax.set(xlabel='tweet number', ylabel='polarity')

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:
                ax.label_outer()

            plt.show()

        else:

            #fig = plt.figure(2)

            fig = plt.figure(2)
            
            axis = fig.add_subplot(1,1,1)

            number = select_user()

            name = user.get()

            df = pd.read_csv('files/'+name+'.csv')

            X = list(df['index'])

            Y = list(df['polarity'])

            axis.scatter(X,Y)
            
            plt.xlabel('tweet number')
            
            plt.ylabel('polarity')
            
            plt.show()

    def plot_histogram(self):

        if(select_user() == 'Compare All'):

            #fig, axs = plt.subplots(2, 2)

            fig, axs = plt.subplots(2, 2)

            df = pd.read_csv('files/'+str('group')+'.csv')

            pol0 = list(df['polarity'])

            df = pd.read_csv('files/'+str('Aman Kathait')+'.csv')

            pol1 = list(df['polarity'])

            df = pd.read_csv('files/'+str('Akshat Negi')+'.csv')

            pol2 = list(df['polarity'])

            df = pd.read_csv('files/'+str('Shubham Semwal')+'.csv')

            pol3 = list(df['polarity'])

            axs[0, 0].hist(pol0,bins=7,color='green',histtype = 'barstacked')
            
            axs[0, 0].set_title('group')
            
            axs[0, 1].hist(pol1,bins=7,color='brown',histtype = 'barstacked')
            
            axs[0, 1].set_title('Aman Kathait')
            
            axs[1, 0].hist(pol2,bins=7,color='red',histtype = 'barstacked')
            
            axs[1, 0].set_title('Akshat Negi')
            
            axs[1, 1].hist(pol3,bins=7,color='blue',histtype = 'barstacked')
            
            axs[1, 1].set_title('Shubham Semwal')

            for ax in axs.flat:
                ax.set(xlabel='polarity of tweets', ylabel='number of tweets')

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:
                ax.label_outer()

            plt.show()
        
        else:

            #plt.hist(self.polarity[0],bins=7,color='green',histtype = 'barstacked')

            number = select_user()

            df = pd.read_csv('files/'+str(user.get())+'.csv')

            pol = list(df['polarity'])

            plt.hist(pol,bins=4,color='green',histtype = 'barstacked')
            
            plt.ylabel('number of tweets')
            
            plt.xlabel('polarity of tweets')
            
            plt.show()


def set_bg_to_grey():

    root.configure(background="grey")

    topframe.configure(background="grey")

    middleframe.configure(background="grey")

    bottomFrame.configure(background="grey")

def set_bg_to_red():

    root.configure(background="red")

    topframe.configure(background="red")

    middleframe.configure(background="red")

    bottomFrame.configure(background="red")

def set_bg_to_pink():

    root.configure(background="pink")

    topframe.configure(background="pink")

    middleframe.configure(background="pink")

    bottomFrame.configure(background="pink")

def set_bg_to_brown():

    root.configure(background="brown")

    topframe.configure(background="brown")

    middleframe.configure(background="brown")

    bottomFrame.configure(background="brown")


def set_bg_to_green():

    root.configure(background="green")

    topframe.configure(background="green")

    middleframe.configure(background="green")

    bottomFrame.configure(background="green")

def set_bg_to_blue():

    root.configure(background="lightblue")

    topframe.configure(background="lightblue")

    middleframe.configure(background="lightblue")

    bottomFrame.configure(background="lightblue")

def set_bg_to_orange():

	root.configure(background="orange")

	topframe.configure(background="orange")

	middleframe.configure(background="orange")

	bottomFrame.configure(background="orange")

def set_bg_to_violet():

	root.configure(background="violet")

	topframe.configure(background="violet")

	middleframe.configure(background="violet")

	bottomFrame.configure(background="violet")

def set_bg_to_yellow():

	root.configure(background="yellow")

	topframe.configure(background="yellow")

	middleframe.configure(background="yellow")

	bottomFrame.configure(background="yellow")

def set_bg_to_lightgreen():

	root.configure(background="lightgreen")

	topframe.configure(background="lightgreen")

	middleframe.configure(background="lightgreen")

	bottomFrame.configure(background="lightgreen")

def open_telegram(event=None):

	pass

def main_thread(event=None):

	pass

def select_user(event = None):

	#global group_user_name

	return user.get()



if __name__ == '__main__':

	# yd = YouTube_Downloader()

	# print(yd.__doc__)

	# yd.history()

	app = Application()

	root = Tk()

	root.title("Telegram Group Sentiment Analysis Desktop Application ")

	root.geometry("800x600")

	root.resizable(width = False , height = False)
	
	root.configure(background = "lightblue")

	label1 = Label(root,text="Telegram Group Sentiment Analysis",fg="blue",bg="skyblue",font=("",15,"bold"))
    
	label1.pack(side=TOP,pady=20)

	topframe = Frame(root,background="lightblue")

	topframe.pack()

	darkcolor = Frame(topframe)

	darkcolor.pack(side = LEFT)

	icon_img = PhotoImage(file="image_resource/telegram.png")

	icon_img = icon_img.subsample(2,2)

	icon_button = Button(topframe,image = icon_img , command = open_telegram)

	icon_button.pack(side = LEFT,padx = 75)

	lightcolor = Frame(topframe)

	lightcolor.pack(side = LEFT)

	red_image = PhotoImage(file = "image_resource/red.png")
    
	brown_image = PhotoImage(file = "image_resource/brown.png")
    
	pink_image = PhotoImage(file = "image_resource/pink.png")

	grey_image = PhotoImage(file = "image_resource/grey.png")

	green_image = PhotoImage(file = "image_resource/green.png")

	blue_image = PhotoImage(file = "image_resource/blue.png")

	violet_image = PhotoImage(file = "image_resource/violet.png")

	orange_image = PhotoImage(file = "image_resource/orange.png")

	yellow_image = PhotoImage(file = "image_resource/yellow.png")

	lightgreen_image = PhotoImage(file = "image_resource/lightgreen.png")

	red_image = red_image.subsample(4,4)
    
	brown_image = brown_image.subsample(4,4)
    
	pink_image = pink_image.subsample(4,4)

	grey_image = grey_image.subsample(4,4)

	green_image = green_image.subsample(4,4)

	blue_image = blue_image.subsample(4,4)

	violet_image = violet_image.subsample(4,4)

	orange_image = orange_image.subsample(4,4)

	yellow_image = yellow_image.subsample(4,4)

	lightgreen_image = lightgreen_image.subsample(4,4)

	red_button = Button(darkcolor,image = red_image,command = set_bg_to_red)
    
	red_button.pack(side = LEFT)

	brown_button = Button(darkcolor, image = brown_image,command = set_bg_to_brown)
    
	brown_button.pack(side = LEFT)

	green_button = Button(darkcolor,image = green_image,command = set_bg_to_green)
    
	green_button.pack(side = LEFT)

	orange_button = Button(darkcolor,image = orange_image,command = set_bg_to_orange)
	   
	orange_button.pack(side = LEFT)

	violet_button = Button(darkcolor,image = violet_image,command = set_bg_to_violet)
	   
	violet_button.pack(side = LEFT)

	pink_button = Button(lightcolor,image = pink_image,command = set_bg_to_pink)
    
	pink_button.pack(side = LEFT)

	grey_button = Button(lightcolor, image = grey_image,command = set_bg_to_grey)
    
	grey_button.pack(side = LEFT)

	blue_button = Button(lightcolor,image = blue_image,command = set_bg_to_blue)
    
	blue_button.pack(side = LEFT)

	yellow_button = Button(lightcolor,image = yellow_image,command = set_bg_to_yellow)
	   
	yellow_button.pack(side = LEFT)

	lightgreen_button = Button(lightcolor,image = lightgreen_image,command = set_bg_to_lightgreen)
	   
	lightgreen_button.pack(side = LEFT)

	middleframe = Frame(root)

	middleframe.pack(pady = 10)

	label3 = Label(root,text="Live dislpay of Group chat",fg="red",bg="yellow",font=("",12,"bold"))
	
	label3.pack(side=TOP,pady=10)

	tag = Entry(root,justify=CENTER,font = ("verdana","15","bold"))
	
	tag.pack(side = TOP)

	label4 = Label(root,text="Select Username that details you want to see",fg="red",bg="yellow",font=("",12,"bold"))
	
	label4.pack(side=TOP,pady=10)

	Values = ['Compare All','Aman Kathait','Akshat Negi','Shubham Semwal','group']

	user = StringVar()

	choices = ttk.Combobox(root,textvariable = user,height=10)

	choices['values'] = Values
	
	choices.pack()

	choices.current(0)

	choices.bind("<<ComboboxSelected>>",select_user)

	#################

	label5 = Label(root,text="Select appropriate diagram to dislpay User Details",fg="red",bg="yellow",font=("",12,"bold"))
	
	label5.pack(side=TOP,pady=10)

	bottomFrame = Frame(root,background="lightblue",width=700,height=150)
	
	bottomFrame.pack(side = TOP,pady = 20)

	piechart_image = PhotoImage(file = "image_resource/piechart.png")
	
	scatterplot_image = PhotoImage(file = "image_resource/scatter.png")
	
	histogram_image = PhotoImage(file = "image_resource/histogram.png")

	piechart_image = piechart_image.subsample(2,2)
	
	scatterplot_image = scatterplot_image.subsample(2,2)
	
	histogram_image = histogram_image.subsample(2,2)

	piechart_button = Button(bottomFrame,image = piechart_image,command = app.plot_PieChart)
	
	piechart_button.pack(side = LEFT,padx=20)

	scatterplot_button = Button(bottomFrame, image = scatterplot_image,command = app.scatter_plot)
	
	scatterplot_button.pack(side = LEFT,padx=20)

	histogram_button = Button(bottomFrame,image = histogram_image,command = app.plot_histogram)
	
	histogram_button.pack(side = LEFT,padx=20)
	
	root.mainloop()