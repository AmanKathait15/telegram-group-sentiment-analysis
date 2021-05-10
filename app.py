
############################## modules reuired ######################################

from tkinter import *					###	used to craete GUI 

from tkinter import ttk 				###	used to craete GUI

from tkinter import messagebox

from threading import Thread 				###	used to divide process into different threads

from time import strftime,localtime,gmtime 		###	used to find local date and time

from matplotlib import pyplot as plt                #### used to display data in pie-chart , bar graph and scatter plot ####

import matplotlib.animation as animation

from time import sleep

import pandas as pd

from random import randint

from math import sqrt , ceil

from numpy import array

import os

############################# End of imported modules ###########################################

class Application():

    def __init__(self):  

    	# attempt authentication 
    	try:

            self.index = None

    	except Exception as e:

            print("authentication failed please check your network and try again \nerror detail : "+str(e))

            msg = str(strftime("%Y-%m-%d %H:%M:%S", localtime()))+","+str(e)+"\n" 
            
            f = open("csv_files/logbook.csv","a")

            f.write(msg)

            f.close()

    def live_plot(self):

        if(select_user() == "Compare All"):

            n,col,Interval = randint(0,2) , select_theme() , (100,500,1000)

            self.index = -1

            fig = plt.figure()

            axis = fig.add_subplot(1,1,1)

            colors = ['green','lightgreen','yellow', 'orange', 'red']

            X,Y = [],[] #[1,2,3,4,5],[0.501,0.3,0.0,-0.2,-0.51]

            def animate(i):

                self.index+=1

                fp = open('files/Group.csv','r')

                last_line = list(fp.readlines()[-1].split(','))

                fp.close()

                #print(last_line)

                x,y = int(last_line[0]),float(last_line[6])

                plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[0],markersize=7)

                plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[1],markersize=7)
                
                plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[2],markersize=7)
                
                plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[3],markersize=7)
                
                plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[4],markersize=7)

                color = "green"

                if(y>0.5):
                    color = "green"
                elif(y>0):
                    color = "lightgreen"
                elif(y==0):
                    color = "yellow"
                elif(y>-0.5):
                    color = "orange"
                else:
                    color = "red"

                #print(x,y,sep=" ")

                X.append(x)

                Y.append(y)

                labels = ('Very Positive','Positive','Neutral','Negative','Very Negative')

                #plt.cla()

                plt.title("Live Sentiment of Telegram Group")

                plt.xlabel('message id')

                plt.ylabel('Polarity')

                plt.legend(labels,loc='upper left')

                plt.ylim([-1,1])

                plt.plot(X,Y,'-ok',color=col,markerfacecolor=color,markersize=7)

            ani = animation.FuncAnimation(plt.gcf(),animate, interval= Interval[randint(0,2)])

            plt.show()

        else:

            n,col , Interval , name = randint(0,3) , select_theme() , (250,500,750,1000) , user.get()

            fig = plt.figure()

            axis = fig.add_subplot(1,1,1)

            self.index = -1

            X,Y = [],[]

            df = pd.read_csv('files/'+name+'.csv')

            pol = list(df['polarity']) #[0.501,0.3,0.0,-0.2,-0.51]+list(df['polarity'])

            colors = ['green','lightgreen','yellow', 'orange', 'red']

            plt.plot(0,float(pol[0]),'-ok',color=col,markerfacecolor=colors[0],markersize=7)

            plt.plot(0,float(pol[0]),'-ok',color=col,markerfacecolor=colors[1],markersize=7)
            
            plt.plot(0,float(pol[0]),'-ok',color=col,markerfacecolor=colors[2],markersize=7)
            
            plt.plot(0,float(pol[0]),'-ok',color=col,markerfacecolor=colors[3],markersize=7)
            
            plt.plot(0,float(pol[0]),'-ok',color=col,markerfacecolor=colors[4],markersize=7)

            def animate(i):

                self.index+=1

                x,y = 0,0

                if(self.index < len(pol)):

                    x,y = self.index,float(pol[self.index])

                else:

                    x,y = self.index-1,float(pol[self.index-1])

                    self.index-=1

                color = "green"

                if(y>0.5):
                    color = "green"
                elif(y>0):
                    color = "lightgreen"
                elif(y==0):
                    color = "yellow"
                elif(y>-0.5):
                    color = "orange"
                else:
                    color = "red"

                #print(x,y,sep=" ")

                X.append(x)

                Y.append(y)

                labels = ('Very Positive','Positive','Neutral','Negative','Very Negative')

                #plt.cla()

                plt.title("Live Sentiment Simulatiom of "+ name +" messages")

                plt.xlabel('message id')

                plt.ylabel('Polarity')

                plt.legend(labels,loc='upper left')

                plt.ylim([-1,1])

                plt.plot(X,Y,'-ok',color=col,markerfacecolor=color,markersize=7)

            ani = animation.FuncAnimation(plt.gcf(),animate, interval= Interval[randint(0,3)])

            plt.show()    	

    def plot_PieChart(self):
    
        if(select_user() == "Compare All"):

            fp = open('files/Compare All.csv','w')

            fp.write("Username,very_positive,positive,neutral,negative,very_negative,total\n")

            fp.close()

            fp = open('files/group_details.csv')

            username = fp.readlines()[-1].split(',')

            n = int(username[0])

            grid = ceil(sqrt(n))

            fig, axs = plt.subplots(grid, grid)

            x,y = 0,0

            angel,location = (45,90,120,180,270,300,0) , ('best','upper left','upper right','lower left','lower right')

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

            	labels = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
            	
            	sizes = [very_positive,positive,neutral,negative,very_negative]
            	
            	fp = open('files/Compare All.csv','a')
            	
            	fp.write(username[i]+","+str(very_positive) + " [ {:.2f} % ],".format(very_positive/total*100) + str(positive)+ " [ {:.2f} % ],".format(positive/total*100) +str(neutral)+ " [ {:.2f} % ],".format(neutral/total*100) +str(negative)+ " [ {:.2f} % ],".format(negative/total*100) +str(very_negative)+ " [ {:.2f} % ],".format(very_negative/total*100) +str(total)+"\n")
            	
            	fp.close()
            	
            	colors = ['green','lightgreen','yellow', 'orange', 'red']

            	if(y == grid):

            		x,y = x+1,0

            	#print(x,y)

            	patches,texts = axs[x,y].pie(sizes, colors=colors, startangle = 90 ) #angel[randint(0,6)])

            	axs[x,y].legend(patches, labels, loc = 'lower right') #location[randint(0,4)])
            	
            	axs[x,y].set_title(username[i])

            	y = y+1

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:

            	ax.label_outer()

            plt.savefig('image_resource/Compare_All_pie.png', bbox_inches='tight')

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
        	    
        	    #plt.savefig('image_resource/'+str(user.get())+'_pie.png',bbox_inches='tight')
        	    
        	    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        	    
        	    plt.legend(patches, labels, loc="best")
        	    
        	    plt.title('pie - chart')
        	    
        	    plt.axis('equal')
        	    
        	    plt.savefig('image_resource/'+str(user.get())+'_pie.png',bbox_inches='tight')
        	    
        	    plt.show()



    def scatter_plot(self):

        if(select_user() == 'Compare All'):

            fp = open('files/group_details.csv')

            username = fp.readlines()[-1].split(',')

            n = int(username[0])

            grid = ceil(sqrt(n))

            fig, axs = plt.subplots(grid, grid)

            x,y = 0,0

            colors = ('orange','red','green','blue','brown','pink','yellow','lightgreen','grey','lightblue')

            for i in range(1,n+1):

            	df = pd.read_csv('files/'+username[i]+'.csv')

            	#X = list(df['index'])

            	X = array(range(0,len(df['polarity'])))

            	Y = list(df['polarity'])

            	if(y == grid):

            		x,y = x+1,0

            	#print(x,y)

            	axs[x,y].plot(X, Y, 'tab:'+str(colors[i-1]))
            	
            	axs[x,y].set_title(username[i])

            	y = y + 1

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:

            	ax.label_outer()

            plt.savefig('image_resource/Compare_All_scatter.png', bbox_inches='tight')

            plt.show()

        else:

            #fig = plt.figure(2)

            fig = plt.figure(2)

            colors = ('green','orange','lightblue','red','brown','yellow')
            
            axis = fig.add_subplot(1,1,1)

            number = select_user()

            name = user.get()

            df = pd.read_csv('files/'+name+'.csv')

            X = list(df['index'])

            Y = list(df['polarity'])

            axis.scatter(X,Y)

            #axis.plot(X,Y,'tab:'+str(colors[randint(0,5)]))
            
            plt.xlabel('tweet number')
            
            plt.ylabel('polarity')

            plt.savefig('image_resource/'+str(user.get())+'_scatter.png', bbox_inches='tight')
            
            plt.show()

    def plot_histogram(self):

        if(select_user() == 'Compare All'):

            fp = open('files/group_details.csv')

            username = fp.readlines()[-1].split(',')

            n = int(username[0])

            grid = ceil(sqrt(n))

            fig, axs = plt.subplots(grid, grid)

            x,y = 0,0

            colors = ('orange','red','green','blue','brown','pink','yellow','lightgreen','grey')

            for i in range(1,n+1):

            	df = pd.read_csv('files/'+username[i]+'.csv')

            	p = list(df['polarity'])

            	pol = []

            	for j in p:

            		pol.append(int(j * 10))

            	if(y == grid):

            		x,y = x+1,0

            	#N,bins,patches = 
            	axs[x,y].hist(pol,bins=5, edgecolor='white', linewidth=1,color=colors[i-1],histtype = 'barstacked')

            	axs[x,y].set_title(username[i])

            	# for j in range(-10,-5):

            	#     patches[j].set_facecolor('r')

            	# for j in range(-5,0):

            	#     patches[j].set_facecolor('0')

            	# for j in range(-1,0):

            	#     patches[j].set_facecolor('y')

            	# for j in range(0,len(patches)):

            	#     patches[j].set_facecolor('g')
            	
            	# axs[x,y].ylabel('number of tweets')
            	
            	# axs[x,y].xlabel('polarity of tweets')

            	y = y + 1

            for ax in axs.flat:

            	ax.set(xlabel='polarity of tweets', ylabel='number of tweets')

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:

            	ax.label_outer()

            plt.savefig('image_resource/Compare_All_histogram.png', bbox_inches='tight')

            plt.show()
        
        else:

            #plt.hist(self.polarity[0],bins=7,color='green',histtype = 'barstacked')

            number = select_user()

            colors = ('green','orange','lightblue','red','brown','yellow')

            df = pd.read_csv('files/'+str(user.get())+'.csv')

            pol = list(df['polarity'])

            plt.hist(pol,bins=randint(4,8),color=colors[randint(0,5)],histtype = 'barstacked')
            
            plt.ylabel('number of tweets')
            
            plt.xlabel('polarity of tweets')

            plt.savefig('image_resource/'+str(user.get())+'_histogram.png', bbox_inches='tight')
            
            plt.show()


def change_bg(color):

    root.configure(background=color)

    topframe.configure(background=color)

    middleframe.configure(background=color)

    bottomFrame.configure(background=color)

    ComboFrame.configure(background=color)
	
def back_end():

	while(flag):
	
		fp = open('files/Group.csv','r')
		
		msg = fp.readlines()[-1]
		
		fp.close()
		
		#print(msg)
		
		msg = list(msg.split(','))
		
		output = ' message id \t\t:  '+msg[0] +'\n username \t\t:  '+msg[1] +'\n time \t\t:  '+msg[2] +'\n message \t\t:  '+msg[3]+'\n sentiment \t\t:  '+msg[5]+'\n polarity \t\t:  '+msg[6]
		
		text.delete('1.0','end')
		
		text.insert(INSERT,output)
		
		sleep(2)
		
		if(msg[1] not in tmp):
		
			text.delete('1.0','end')
		
			text.insert(INSERT,"\tNew Member Added\n\n\t"+msg[1]+" joined the group ")
			
		if(not flag):
		
			break

def open_telegram(event=None):

	pass

def open_xls():

	file_path = str(user.get())

	import subprocess, sys

	if sys.platform.startswith('win32'):

		file_path = "files\\"+file_path+".csv"

	else:

		file_path = "files/"+file_path+".csv"

	print(file_path)

	if sys.platform.startswith('linux'):
	    
	    subprocess.Popen(['xdg-open', file_path],
	                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	elif sys.platform.startswith('win32'):
	    
	    os.startfile(file_path)
	
	elif sys.platform.startswith('cygwin'):
	    
	    os.startfile(file_path)
	
	elif sys.platform.startswith('darwin'):
	    
	    subprocess.Popen(['open', file_path],
	                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	else:
	    
	    subprocess.Popen(['xdg-open', file_path],
	                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def chnageValues(event = None):

    fp = open('files/group_details.csv','r')
    
    tmp = list(fp.readlines()[-1].split(','))
    
    fp.close()
    
    if(int(tmp[0]) >= len(choices['values'])):
    
        choices['values'] = ['Compare All']+tmp[1:]

def select_user(event = None):

    return user.get()

def select_theme(event = None):

    if(Theme.get() == 'seaborn-whitegrid'):

        plt.style.use('seaborn-whitegrid')

        return "blue"

    elif(Theme.get() == 'dark_background'):

        plt.style.use('dark_background') 

        return "white"

    elif(Theme.get() == 'ggplot'):

        plt.style.use('ggplot')

        return "black"

    else:

        plt.style.use('classic')

        return "black"
	
def on_closing():

	flag = False
	
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
	        
	        root.destroy()

if __name__ == '__main__':

	# yd = YouTube_Downloader()

	# print(yd.__doc__)

	# yd.history()

	app = Application()
	
	flag = True
	
	root = Tk()

	root.title("Telegram Group Sentiment Analysis Desktop Application ")

	root.geometry("800x650")

	#root.resizable(width = False , height = False)
	
	root.configure(background = "brown")

	label1 = Label(root,text="Telegram Group Sentiment Analysis",fg="blue",bg="skyblue",font=("",15,"bold"))
    
	label1.pack(side=TOP,pady=20)

	topframe = Frame(root,background="brown")

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

	red_button = Button(darkcolor,image = red_image,command = lambda: change_bg("red"))
    
	red_button.pack(side = LEFT)

	brown_button = Button(darkcolor, image = brown_image,command = lambda: change_bg("brown"))
    
	brown_button.pack(side = LEFT)

	green_button = Button(darkcolor,image = green_image,command = lambda: change_bg("green"))
    
	green_button.pack(side = LEFT)

	orange_button = Button(darkcolor,image = orange_image,command = lambda: change_bg("orange"))
	   
	orange_button.pack(side = LEFT)

	violet_button = Button(darkcolor,image = violet_image,command = lambda: change_bg("violet"))
	   
	violet_button.pack(side = LEFT)

	pink_button = Button(lightcolor,image = pink_image,command = lambda: change_bg("pink"))
    
	pink_button.pack(side = LEFT)

	grey_button = Button(lightcolor, image = grey_image,command = lambda: change_bg("grey"))
    
	grey_button.pack(side = LEFT)

	blue_button = Button(lightcolor,image = blue_image,command = lambda: change_bg("lightblue"))
    
	blue_button.pack(side = LEFT)

	yellow_button = Button(lightcolor,image = yellow_image,command = lambda: change_bg("yellow"))
	   
	yellow_button.pack(side = LEFT)

	lightgreen_button = Button(lightcolor,image = lightgreen_image,command = lambda: change_bg("lightgreen"))
	   
	lightgreen_button.pack(side = LEFT)

	middleframe = Frame(root,background="brown")

	middleframe.pack(pady = 10)

	label3 = Label(middleframe,text="Live dislpay of Group chat",fg="red",bg="yellow",font=("",12,"bold"))
	
	label3.pack(side=TOP,pady=10)
	
	text = Text(middleframe,height=6,width=75,font=("",12,"bold"),bg="black",fg="white")
	
	fp = open('files/Group.csv','r')
	
	msg = fp.readlines()[-1]
	
	msg = list(msg.split(','))
	
	output = 'message id \t\t: '+msg[0] +'\nusername \t\t: '+msg[1] +'\ntime \t\t: '+msg[2] +'\nmessage \t\t: '+msg[3]+'\nsentiment \t\t: '+msg[4]+'\npolarity \t\t:'+msg[5]
	
	text.insert(INSERT,output)
	
	text.pack(side = TOP)
	
	thread1 = Thread(target = back_end)
	
	thread1.setDaemon(True)
	
	thread1.start()

	label4 = Label(middleframe,text="Select Username that details you want to see",fg="red",bg="yellow",font=("",12,"bold"))
	
	label4.pack(side=TOP,pady=10)

	Values = ['Compare All'] #,'Aman Kathait','Akshat Negi','Shubham Semwal','Group']

	fp = open('files/group_details.csv')

	tmp = fp.readlines()[-1].split(',')

	Values += tmp[1:]

	user = StringVar()
	
	ComboFrame = Frame(middleframe,background="brown")
	
	ComboFrame.pack(padx = 150)

	choices = ttk.Combobox(ComboFrame,textvariable = user,height=30 , state = 'readonly',postcommand = chnageValues)

	choices['values'] = Values
	
	choices.pack(side = LEFT,padx=20)

	choices.current(0)

	choices.bind("<<ComboboxSelected>>",select_user)
	
	Theme = StringVar()
	
	theme = ttk.Combobox(ComboFrame,textvariable = Theme,height=30 , state = 'readonly')
	
	theme['values'] = ('default','seaborn-whitegrid','dark_background','ggplot')
	
	theme.pack(side = LEFT,padx=20)
	
	theme.current(0)
	
	theme.bind("<<ComboboxSelected>>",select_theme)

	#################

	label5 = Label(root,text="Select appropriate diagram to dislpay User Details",fg="red",bg="yellow",font=("",12,"bold"))
	
	label5.pack(side=TOP,pady=10)

	bottomFrame = Frame(root,background="brown",width=700,height=150)
	
	bottomFrame.pack(side = TOP,pady = 20)

	piechart_image = PhotoImage(file = "image_resource/piechart.png")
	
	scatterplot_image = PhotoImage(file = "image_resource/scatter.png")
	
	histogram_image = PhotoImage(file = "image_resource/histogram.png")

	xls_image = PhotoImage(file = "image_resource/xls_icon.png")

	live_image = PhotoImage(file = "image_resource/live.png")

	piechart_image = piechart_image.subsample(2,2)
	
	scatterplot_image = scatterplot_image.subsample(2,2)
	
	histogram_image = histogram_image.subsample(2,2)

	xls_image = xls_image.subsample(2,2)

	live_image = live_image.subsample(2,2)

	piechart_button = Button(bottomFrame,image = piechart_image,command = app.plot_PieChart)
	
	piechart_button.pack(side = LEFT,padx=10)

	scatterplot_button = Button(bottomFrame, image = scatterplot_image,command = app.scatter_plot)
	
	scatterplot_button.pack(side = LEFT,padx=10)

	histogram_button = Button(bottomFrame,image = histogram_image,command = app.plot_histogram)
	
	histogram_button.pack(side = LEFT,padx=10)

	xls_button = Button(bottomFrame,image = xls_image,command = open_xls)
	
	xls_button.pack(side = LEFT,padx=10)

	live_button = Button(bottomFrame,image = live_image,command = app.live_plot)
	
	live_button.pack(side = LEFT,padx=10)
	
	root.protocol("WM_DELETE_WINDOW", on_closing)
	
	root.mainloop()
