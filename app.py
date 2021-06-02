
############################### modules reuired ######################################

from tkinter import *                   ### used to craete GUI 

from tkinter import ttk                 ### used to craete GUI

from tkinter import messagebox              ### to genrate message when gui is distroyed

from threading import Thread                ### used to divide process into different threads

from matplotlib import pyplot as plt                ###     used to display data in pie-chart , bar graph and scatter plot 

import matplotlib.animation as animation        ### used plot live plot of group messages

from time import sleep                  ###     used for delay

import pandas as pd                 ###     used to read csv files

from random import randint              ###     used to change plot colors 

from math import sqrt , ceil                ### used to find perfect grid 

import os                       ### used to open subprocess or different application

############################# End of imported modules ###########################################

class Application():

    """    
    ################# docstring for Application Class #################
    
    ######### class attributes ##########

    varibale        type                    use to

    index           integer                 unique number for each message fetch

    root        tkinter.TK          reprsent main GUI window

    text        tkinter.Text            display live sentiment on GUI text field

    user        StringVar           store current username selected in UserList combobox

    Theme       StringVar           store current theme selected in theme combobox

    UserList        tkinter.ttk.Combobox        store list of all users in a group

    topframe        tkinter.Frame           top frame og GUI in which darkcolor and lightcolor frame is shown

    middleframe     tkinter.Frame           middle frame in which text feild and combobox shown

    bottomframe     tkinter.Frame           frame in which button of different plot is shown

    ######### class methods #############

    function            work / task                                     run/call

    __init__            this function is a constructor of Application           run when Application class object is created  
                        class and it work is to allocate memory

    plot_PieChart       this function display our data in pie chart form    run when pie chart icon clicked in GUI
                        ie show value of very +ve , +ve , 0 , -ve and
                        very -ve score in our data

    plot_histogram      this function display ploarity in histogram form    run when histogram icon clicked in GUI
                        so that user can visualize which sentiment score
                        range tweet is more .

    scatter_plot        this function display polarity in scatter plot      run when scatter plot icon clicked in GUI
                        graph make easy to visualize flow of sentiments
                        of twitter users on that query
                         
    live_plot       this function show live sentiment in graph using    run when live button is clicked in GUI 
                animation and simulation of previous chats

    back_end        this function start the seprate thred to read       call in main function
                    csv files and update text feild in GUI if 
                    any chnage occur
    
    chnage_vlaues       this function update the list of username in        run each time when combobox clicked
                    UserList combobox when new user added to group
    
    on_closing          this function confirm user to exit GUI          run before gui is closed
    
    select_user     this function return the curret value of        call inside many function
                    UserList combobox
    
    select_theme    this function chage theme of plot graphs        call each time when Themen combobox vkaue chnaged

    chnage_bg       this function change the backgroud color of GUI     run when color icon is clicked in GUI

    open_telegram       this function open Telegram                 run when telegram icon is clicked in GUI

    open_xls        this function open csv file             run when open xls button is clicked in GUI

    GUI             In this function most of GUI coding is done.        call in main function

    __main__            In this object of Application class created         execution of program begin from this function

    """

    def __init__(self):  

        self.index = None
        
        self.root = None
        
        self.text = None
        
        self.user = None
        
        self.theme = None
        
        self.topframe = None
        
        self.middleframe = None
        
        self.bottomframe = None
        
        self.comboframe = None
        
        self.UserList = None

    def live_plot(self):

        if(self.select_user() == "Compare All"):

            if(self.select_type() == 'polarity'):

                n,col,Interval = randint(0,2) , self.select_theme() , (100,500,1000)

                self.index = -1

                fig = plt.figure()

                axis = fig.add_subplot(1,1,1)

                colors = ['yellow','green','lightgreen', 'orange', 'red']

                X,Y = [],[] #[1,2,3,4,5],[0.501,0.3,0.0,-0.2,-0.51]

                def animate(i):

                    self.index+=1

                    fp = open('files/Group.csv','r')

                    last_line = list(fp.readlines()[-1].split(','))

                    fp.close()

                    #print(last_line)

                    x,y = int(last_line[0]),float(last_line[6])

                    sc = int(last_line[4])

                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[0],markersize=7)

                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[1],markersize=7)
                    
                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[2],markersize=7)
                    
                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[3],markersize=7)
                    
                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[4],markersize=7)

                    X.append(x)

                    Y.append(y)

                    labels = ('Very Positive','Positive','Neutral','Negative','Very Negative')

                    #plt.cla()

                    plt.title("Live Sentiment of Telegram Group")

                    plt.xlabel('message id')

                    plt.ylabel('Polarity')

                    plt.legend(labels,loc='upper left')

                    plt.ylim([-1,1])

                    plt.plot(X,Y,'-ok',color=col,markerfacecolor=colors[sc],markersize=7)

                ani = animation.FuncAnimation(plt.gcf(),animate, interval= Interval[randint(0,2)])

                plt.show()

            else:

                n,col,Interval = randint(0,2) , self.select_theme() , (100,500,1000)

                self.index = -1

                fig = plt.figure()

                axis = fig.add_subplot(1,1,1)

                colors = ['yellow','red', 'orange','blue','black']

                X,Y = [],[] #[1,2,3,4,5],[0.501,0.3,0.0,-0.2,-0.51]

                def animate(i):

                    self.index+=1

                    fp = open('files/Group.csv','r')

                    last_line = list(fp.readlines()[-1].split(','))

                    fp.close()

                    #print(last_line)

                    x,y = int(last_line[0]),float(last_line[13])

                    ec = int(last_line[12])

                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[0],markersize=7)

                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[1],markersize=7)
                    
                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[2],markersize=7)
                    
                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[3],markersize=7)
                    
                    plt.plot(x,y,'-ok',color=col,markerfacecolor=colors[4],markersize=7)

                    X.append(x)

                    Y.append(y)

                    labels = ('Happy','Angry','Surprise','Sad','Fear')

                    #plt.cla()

                    plt.title("Live Sentiment of Telegram Group")

                    plt.xlabel('message id')

                    plt.ylabel('Polarity')

                    plt.legend(labels,loc='upper left')

                    plt.ylim([0,1.5])

                    plt.plot(X,Y,'-ok',color=col,markerfacecolor=colors[ec],markersize=7)

                ani = animation.FuncAnimation(plt.gcf(),animate, interval= Interval[randint(0,2)])

                plt.show()

        else:

            if(self.select_type() == 'polarity'):

                n,col , Interval , name = randint(0,3) , self.select_theme() , (250,500,750,1000) , self.user.get()

                fig = plt.figure()

                axis = fig.add_subplot(1,1,1)

                self.index = -1

                X,Y = [],[]

                df = pd.read_csv('files/'+name+'.csv')

                pol = list(df['polarity']) #[0.501,0.3,0.0,-0.2,-0.51]+list(df['polarity'])

                sc = list(df['sentiment_code'])

                colors = ['yellow','green','lightgreen', 'orange', 'red']

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

                    X.append(x)

                    Y.append(y)

                    labels = ('Very Positive','Positive','Neutral','Negative','Very Negative')

                    #plt.cla()

                    plt.title("Live Sentiment Simulatiom of "+ name +" messages")

                    plt.xlabel('message id')

                    plt.ylabel('Polarity')

                    plt.legend(labels,loc='upper left')

                    plt.ylim([-1,1])

                    plt.plot(X,Y,'-ok',color=col,markerfacecolor=colors[sc[self.index]],markersize=7)

                ani = animation.FuncAnimation(plt.gcf(),animate, interval= Interval[randint(0,3)])

                plt.show()

            else:

                n,col , Interval , name = randint(0,3) , self.select_theme() , (750,1000,1250,1500) , self.user.get()

                fig = plt.figure()

                axis = fig.add_subplot(1,1,1)

                self.index = -1

                X,Y = [],[]

                df = pd.read_csv('files/'+name+'.csv')

                Eval = list(df['Value'])

                ec = list(df['Emotion_code'])

                colors = ['green','red','orange','blue','black']

                plt.plot(0,float(Eval[0]),'-ok',color=col,markerfacecolor=colors[0],markersize=7)

                plt.plot(0,float(Eval[0]),'-ok',color=col,markerfacecolor=colors[1],markersize=7)
                
                plt.plot(0,float(Eval[0]),'-ok',color=col,markerfacecolor=colors[2],markersize=7)
                
                plt.plot(0,float(Eval[0]),'-ok',color=col,markerfacecolor=colors[3],markersize=7)
                
                plt.plot(0,float(Eval[0]),'-ok',color=col,markerfacecolor=colors[4],markersize=7)

                def animate(i):

                    self.index+=1

                    x,y = 0,0

                    if(self.index < len(Eval)):

                        x,y = self.index,float(Eval[self.index])

                    else:

                        x,y = self.index-1,float(Eval[self.index-1])

                        self.index-=1

                    X.append(x)

                    Y.append(y)

                    labels = ('Happy','Angry','Surprise','Sad','Fear')

                    #plt.cla()

                    plt.title("Live Sentiment Simulatiom of "+ name +" messages")

                    plt.xlabel('message id')

                    plt.ylabel('Polarity')

                    plt.legend(labels,loc='upper left')

                    plt.ylim([-0.5,1.5])

                    plt.plot(X,Y,'-ok',color=col,markerfacecolor=colors[ec[self.index]],markersize=7)

                ani = animation.FuncAnimation(plt.gcf(),animate, interval= Interval[randint(0,3)])

                plt.show()      

    def plot_PieChart(self):
    
        if(self.select_user() == "Compare All"):

            if(self.select_type() == 'polarity'):

                fp = open('files/Compare All.csv','w')

                fp.write("Username,very_positive,positive,neutral,negative,very_negative,total\n")

                fp.close()

                fp = open('files/group_details.csv')

                username = fp.readlines()[-1].split(',')

                n = int(username[0])

                grid = ceil(sqrt(n))

                fig, axs = plt.subplots(grid, grid)

                x,y = 0,0

                angel = (90,180,270,360)

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

                    patches,texts = axs[x,y].pie(sizes, colors=colors, startangle = angel[randint(0,3)])

                    axs[x,y].legend(patches, labels, loc = 'lower left') #location[randint(0,4)])
                    
                    axs[x,y].set_title(username[i])

                    y = y+1

                # Hide x labels and tick labels for top plots and y ticks for right plots.
                for ax in axs.flat:

                    ax.label_outer()

                plt.savefig('images/user/Compare_All_'+self.theme.get()+'_polarity_pie.png', bbox_inches='tight')

                plt.show()

            else:

                fp = open('files/Compare All.csv','w')

                fp.write("Username,very_positive,positive,neutral,negative,very_negative,total\n")

                fp.close()

                fp = open('files/group_details.csv')

                username = fp.readlines()[-1].split(',')

                n = int(username[0])

                grid = ceil(sqrt(n))

                fig, axs = plt.subplots(grid, grid)

                x,y = 0,0

                angel = (90,180,270,360)

                for i in range(1,n+1):

                    df = pd.read_csv('files/'+username[i]+'.csv')

                    Happy = sum(df['Happy'])
                    
                    Angry = sum(df['Angry'])
                    
                    Surprise = sum(df['Surprise'])
                    
                    Sad = sum(df['Sad'])
                    
                    Fear = sum(df['Fear'])
                    
                    total = Happy + Angry + Surprise + Sad + Fear
                    
                    labels = ['Happy {:.2f} %'.format(Happy/total*100) , 'Angry {:.2f} %'.format(Angry/total*100) ,'Surprise {:.2f} %'.format(Surprise/total*100) , 'Sad {:.2f} %'.format(Sad/total*100) ,'Fear {:.2f} %'.format(Fear/total*100)]
                    
                    sizes = [Happy,Angry,Surprise,Sad,Fear]
                    
                    colors = ['yellow','red','orange', 'grey', 'black']

                    if(self.theme.get() == 'dark_background'):

                        colors[3],colors[4] = 'green','blue'

                    if(y == grid):

                        x,y = x+1,0

                    #print(x,y)

                    patches,texts = axs[x,y].pie(sizes, colors=colors, startangle = angel[randint(0,3)])

                    axs[x,y].legend(patches, labels, loc = 'lower left') #location[randint(0,4)])
                    
                    axs[x,y].set_title(username[i])

                    y = y+1

                # Hide x labels and tick labels for top plots and y ticks for right plots.
                for ax in axs.flat:

                    ax.label_outer()

                plt.savefig('images/user/Compare_All_'+self.theme.get()+'_emotion_pie.png', bbox_inches='tight')

                plt.show()

        else:

                if(self.select_type() == "emotion"):
                
                    df = pd.read_csv('files/'+str(self.user.get())+'.csv')
                    
                    Happy = sum(df['Happy'])
                    
                    Angry = sum(df['Angry'])
                    
                    Surprise = sum(df['Surprise'])
                    
                    Sad = sum(df['Sad'])
                    
                    Fear = sum(df['Fear'])
                    
                    total = Happy + Angry + Surprise + Sad + Fear
                    
                    labels = ['Happy {:.2f} %'.format(Happy/total*100) , 'Angry {:.2f} %'.format(Angry/total*100) ,'Surprise {:.2f} %'.format(Surprise/total*100) , 'Sad {:.2f} %'.format(Sad/total*100) ,'Fear {:.2f} %'.format(Fear/total*100)]
                    
                    sizes = [Happy,Angry,Surprise,Sad,Fear]
                    
                    colors = ['yellow','red','orange', 'grey', 'black']
                    
                    plt.figure(1)
                    
                    angel = (90,180,270,360)
                    
                    if(self.theme.get() == 'dark_background'):
                    
                        colors[3],colors[4] = 'green','blue'
                        
                    patches, texts = plt.pie(sizes, colors=colors, startangle= angel[randint(0,3)])
                    
                    plt.legend(patches, labels, loc="best")
                    
                    plt.title('Emotion-chart')
                    
                    plt.axis('equal')
                    
                    plt.savefig('images/user/'+self.user.get()+'_'+self.theme.get()+'_emotion_pie.png',bbox_inches='tight')
                    
                    plt.show()
                    
                    
                    
                else:
                
                    df = pd.read_csv('files/'+str(self.user.get())+'.csv')
                    
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
                            
                    labels = ['Very Positive {:.2f} %'.format(very_positive/total*100) , 'Positive {:.2f} %'.format(positive/total*100) ,'Neutral {:.2f} %'.format(neutral/total*100) , 'Negative {:.2f} %'.format(negative/total*100) ,'Very Negative {:.2f} %'.format(very_negative/total*100)]
                    
                    sizes = [very_positive,positive,neutral,negative,very_negative]
                    
                    colors = ['green','lightgreen','yellow', 'orange', 'red']
                    
                    plt.figure(1)
                    
                    angel = (90,180,270,360)
                    
                    patches, texts = plt.pie(sizes, colors=colors, startangle= angel[randint(0,3)])
                    
                    plt.legend(patches, labels, loc="best")
                    
                    plt.title('polarity-chart')
                    
                    plt.axis('equal')
                    
                    plt.savefig('images/user/'+str(self.user.get())+'_'+self.theme.get()+'_polarity_pie.png',bbox_inches='tight')
                    
                    plt.show()
                    



    def scatter_plot(self):

        if(self.select_user() == 'Compare All'):

            if(self.select_type() == 'polarity'):

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

                    X = list(range(0,len(df['polarity'])))

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

                plt.savefig('images/user/Compare_All_'+self.theme.get()+'_polarity_scatter.png', bbox_inches='tight')

                plt.show()

            else:

                fp = open('files/group_details.csv')

                username = fp.readlines()[-1].split(',')

                n = int(username[0])

                grid = ceil(sqrt(n))

                fig, axs = plt.subplots(grid, grid)

                x,y = 0,0

                for i in range(1,n+1):

                    df = pd.read_csv('files/'+username[i]+'.csv')

                    X = list(df['index'][0:100])

                    Happy = list(df['Happy'][0:100])
                    
                    Angry = list(df['Angry'][0:100])
                    
                    Surprise = list(df['Surprise'][0:100])
                    
                    Sad = list(df['Sad'][0:100])
                    
                    Fear = list(df['Fear'][0:100])

                    if(y == grid):

                        x,y = x+1,0

                    colors = ['green','red','orange','blue','black']

                    if(self.theme.get() == 'dark_background'):

                        colors[4] = 'pink'

                    axs[x,y].scatter(X,Happy,label='Happy',color=colors[0])

                    axs[x,y].scatter(X,Angry,label='Angry',color=colors[1])

                    axs[x,y].scatter(X,Surprise,label='Surprise',color=colors[2])

                    axs[x,y].scatter(X,Sad,label='Sad',color=colors[3])

                    axs[x,y].scatter(X,Fear,label='Fear',color=colors[4])

                    # axs[x,y].ylim([0.1,1.2])
                    
                    axs[x,y].set_title(username[i])

                    y = y + 1

                # Hide x labels and tick labels for top plots and y ticks for right plots.
                for ax in axs.flat:

                    ax.label_outer()

                plt.savefig('images/user/Compare_All_'+self.theme.get()+'_emotion_scatter.png', bbox_inches='tight')

                plt.show()

        else:

            if(self.select_type() == 'polarity'):

                fig = plt.figure(2)

                colors = ('green','orange','lightblue','red','brown','yellow')
                
                axis = fig.add_subplot(1,1,1)

                name = self.user.get()

                df = pd.read_csv('files/'+name+'.csv')

                X = list(df['index'])

                Y = list(df['polarity'])

                axis.scatter(X,Y)

                #axis.plot(X,Y,'tab:'+str(colors[randint(0,5)]))
                
                plt.xlabel('tweet number')
                
                plt.ylabel('polarity')

                plt.savefig('images/user/'+str(self.user.get())+'_'+self.theme.get()+'_polarity_scatter.png', bbox_inches='tight')
                
                plt.show()

            else:

                fig = plt.figure(2)

                name = self.user.get()

                df = pd.read_csv('files/'+name+'.csv')

                X = list(df['index'][0:100])

                Happy = list(df['Happy'][0:100])
                
                Angry = list(df['Angry'][0:100])
                
                Surprise = list(df['Surprise'][0:100])
                
                Sad = list(df['Sad'][0:100])
                
                Fear = list(df['Fear'][0:100])

                colors = ['green','red','orange','blue','black']

                if(self.theme.get() == 'dark_background'):

                    colors[4] = 'pink'

                plt.scatter(X,Happy,label='Happy',color=colors[0])

                plt.scatter(X,Angry,label='Angry',color=colors[1])

                plt.scatter(X,Surprise,label='Surprise',color=colors[2])

                plt.scatter(X,Sad,label='Sad',color=colors[3])

                plt.scatter(X,Fear,label='Fear',color=colors[4])

                plt.ylim([0.1,1.2])
                
                plt.xlabel('message id')
                
                plt.ylabel('emotion')

                plt.legend(loc = 'upper right')

                plt.savefig('images/user/'+str(self.user.get())+'_'+self.theme.get()+'_emotion_scatter.png', bbox_inches='tight')
                
                plt.show()

    def plot_histogram(self):

        if(self.select_user() == 'Compare All'):

            if(self.select_type() == 'polarity'):

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

                    y = y + 1

                for ax in axs.flat:

                    ax.set(xlabel='polarity of tweets', ylabel='number of tweets')

                # Hide x labels and tick labels for top plots and y ticks for right plots.
                for ax in axs.flat:

                    ax.label_outer()

                plt.savefig('images/user/Compare_All_'+self.theme.get()+'_polarity_histogram.png', bbox_inches='tight')

                plt.show()

            else:

                fp = open('files/group_details.csv')

                username = fp.readlines()[-1].split(',')

                n = int(username[0])

                grid = ceil(sqrt(n))

                fig, axs = plt.subplots(grid, grid)

                x,y = 0,0

                colors = ['yellow','red','orange', 'grey', 'black']

                Emotion = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']

                for i in range(1,n+1):

                    df = pd.read_csv('files/'+username[i]+'.csv')

                    Happy = sum(df['Happy'])
                    
                    Angry = sum(df['Angry'])
                    
                    Surprise = sum(df['Surprise'])
                    
                    Sad = sum(df['Sad'])
                    
                    Fear = sum(df['Fear'])
                    
                    sizes = [Happy,Angry,Surprise,Sad,Fear]

                    if(y == grid):

                        x,y = x+1,0

                    if(self.theme.get() == 'dark_background'):

                        colors[3],colors[4] = 'green','blue'

                    #N,bins,patches = 
                    axs[x,y].bar(Emotion,sizes,color= colors)

                    axs[x,y].set_title(username[i])

                    y = y + 1

                for ax in axs.flat:

                    ax.set(xlabel='Emotions', ylabel='Count')

                # Hide x labels and tick labels for top plots and y ticks for right plots.
                for ax in axs.flat:

                    ax.label_outer()

                plt.savefig('images/user/Compare_All_'+self.theme.get()+'_emotion_bar.png', bbox_inches='tight')

                plt.show()
        
        else:

            if(self.select_type() == 'polarity'):

                colors = ('green','orange','lightblue','red','brown','yellow')

                df = pd.read_csv('files/'+str(self.user.get())+'.csv')

                pol = list(df['polarity'])

                plt.hist(pol,bins=randint(4,8),color=colors[randint(0,5)],histtype = 'barstacked')
                
                plt.ylabel('number of tweets')
                
                plt.xlabel('polarity of tweets')

                plt.savefig('images/user/'+str(self.user.get())+'_'+self.theme.get()+'_polarity_histogram.png', bbox_inches='tight')
                
                plt.show()

            else:

                colors = ['yellow','red','orange', 'grey', 'black']

                df = pd.read_csv('files/'+str(self.user.get())+'.csv')

                Happy = sum(df['Happy'])
                
                Angry = sum(df['Angry'])
                
                Surprise = sum(df['Surprise'])
                
                Sad = sum(df['Sad'])
                
                Fear = sum(df['Fear'])
                
                sizes = [Happy,Angry,Surprise,Sad,Fear]
                
                Emotion = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']

                if(self.theme.get() == 'dark_background'):

                    colors[3],colors[4] = 'green','blue'
                
                plt.bar(Emotion,sizes,color = colors)

                plt.ylabel('Number')
                
                plt.xlabel('Emotions')

                plt.savefig('images/user/'+str(self.user.get())+'_'+self.theme.get()+'_emotion_bar.png', bbox_inches='tight')
                
                plt.show()

    def change_bg(self,color):

        self.root.configure(background=color)

        self.topframe.configure(background=color)

        self.middleframe.configure(background=color)

        self.bottomframe.configure(background=color)

        self.comboframe.configure(background=color)

    def back_end(self):

        while(True):
        
            fp = open('files/Group.csv','r')
            
            msg = fp.readlines()[-1]
            
            fp.close()
            
            #print(msg)
            
            msg = list(msg.split(','))
            
            output = ' message id \t\t:  '+msg[0] + \
                     '\n username \t\t:  '+msg[1] +\
                     '\n time \t\t:  '+msg[2] +\
                     '\n message \t\t:  '+msg[3]+\
                     '\n sentiment \t\t:  '+msg[5]+\
                     '\n polarity \t\t:  '+msg[6]+\
                     '\n\n Emotions -> '+\
                     '{ Happy : '+msg[7]+\
                     ',Angry : '+msg[8]+\
                     ',Surprise : '+msg[9]+\
                     ',Sad : '+msg[10]+\
                     ',Fear : '+msg[11]+' }'
            
            self.text.delete('1.0','end')
            
            self.text.insert(INSERT,output)

            sleep(2)

    def open_telegram(self,event=None):

        url = 'https://t.me/joinchat/NAf-3Uj4f3xvGHiRlmlEfw'

        import subprocess, sys

        if sys.platform.startswith('linux'):
            
            subprocess.Popen(['xdg-open', url],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        elif sys.platform.startswith('win32'):
            
            os.startfile(url)
        
        elif sys.platform.startswith('cygwin'):
            
            os.startfile(url)
        
        elif sys.platform.startswith('darwin'):
            
            subprocess.Popen(['open', url],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            
            subprocess.Popen(['xdg-open', url],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def open_xls(self):

        file_path = str(self.user.get())

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


    def chnageValues(self,event = None):

        fp = open('files/group_details.csv','r')
        
        tmp = list(fp.readlines()[-1].split(','))
        
        fp.close()
        
        if(int(tmp[0]) >= len(self.UserList['values'])):
        
            self.UserList['values'] = ['Compare All']+tmp[1:]

    def select_user(self,event = None):

        return self.user.get()

    def select_type(self,event = None):

        return self.type.get()

    def select_theme(self,event = None):

        if(self.theme.get() == 'seaborn-whitegrid'):

            plt.style.use('seaborn-whitegrid')

            return "blue"

        elif(self.theme.get() == 'dark_background'):

            plt.style.use('dark_background') 

            return "white"

        elif(self.theme.get() == 'ggplot'):

            plt.style.use('ggplot')

            return "black"

        else:

            plt.style.use('classic')

            return "black"
        
    def on_closing(self):

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
                
                self.root.destroy()

    def GUI(self):

        self.root = Tk()

        self.root.title("Telegram Group Sentiment Analysis Desktop Application ")

        self.root.geometry("900x650")

        #self.root.resizable(width = False , height = False)
        
        self.root.configure(background = "brown")

        label1 = Label(self.root,text="Telegram Group Sentiment Analysis",fg="blue",bg="skyblue",font=("",15,"bold"))
        
        label1.pack(side=TOP,pady=20)

        self.topframe = Frame(self.root,background="brown")

        self.topframe.pack()

        darkcolor = Frame(self.topframe)

        darkcolor.pack(side = LEFT)

        icon_img = PhotoImage(file="images/app/telegram.png")

        icon_img = icon_img.subsample(2,2)

        icon_button = Button(self.topframe,image = icon_img , command = self.open_telegram)

        icon_button.pack(side = LEFT,padx = 75)

        lightcolor = Frame(self.topframe)

        lightcolor.pack(side = LEFT)

        red_image = PhotoImage(file = "images/app/red.png")
        
        brown_image = PhotoImage(file = "images/app/brown.png")
        
        pink_image = PhotoImage(file = "images/app/pink.png")

        grey_image = PhotoImage(file = "images/app/grey.png")

        green_image = PhotoImage(file = "images/app/green.png")

        blue_image = PhotoImage(file = "images/app/blue.png")

        violet_image = PhotoImage(file = "images/app/violet.png")

        orange_image = PhotoImage(file = "images/app/orange.png")

        yellow_image = PhotoImage(file = "images/app/yellow.png")

        lightgreen_image = PhotoImage(file = "images/app/lightgreen.png")

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

        red_button = Button(darkcolor,image = red_image,command = lambda: self.change_bg("red"))
        
        red_button.pack(side = LEFT)

        brown_button = Button(darkcolor, image = brown_image,command = lambda: self.change_bg("brown"))
        
        brown_button.pack(side = LEFT)

        green_button = Button(darkcolor,image = green_image,command = lambda: self.change_bg("green"))
        
        green_button.pack(side = LEFT)

        orange_button = Button(darkcolor,image = orange_image,command = lambda: self.change_bg("orange"))
           
        orange_button.pack(side = LEFT)

        violet_button = Button(darkcolor,image = violet_image,command = lambda: self.change_bg("violet"))
           
        violet_button.pack(side = LEFT)

        pink_button = Button(lightcolor,image = pink_image,command = lambda: self.change_bg("pink"))
        
        pink_button.pack(side = LEFT)

        grey_button = Button(lightcolor, image = grey_image,command = lambda: self.change_bg("grey"))
        
        grey_button.pack(side = LEFT)

        blue_button = Button(lightcolor,image = blue_image,command = lambda: self.change_bg("lightblue"))
        
        blue_button.pack(side = LEFT)

        yellow_button = Button(lightcolor,image = yellow_image,command = lambda: self.change_bg("yellow"))
           
        yellow_button.pack(side = LEFT)

        lightgreen_button = Button(lightcolor,image = lightgreen_image,command = lambda: self.change_bg("lightgreen"))
           
        lightgreen_button.pack(side = LEFT)

        self.middleframe = Frame(self.root,background="brown")

        self.middleframe.pack(pady = 10)

        label3 = Label(self.middleframe,text="Live dislpay of Group chat",fg="red",bg="yellow",font=("",12,"bold"))
        
        label3.pack(side=TOP,pady=10)
        
        self.text = Text(self.middleframe,height=8,width=80,font=("",12,"bold"),bg="black",fg="white")
        
        fp = open('files/Group.csv','r')
        
        msg = fp.readlines()[-1]
        
        msg = list(msg.split(','))
        
        output = 'message id \t\t: '+msg[0] +'\nusername \t\t: '+msg[1] +'\ntime \t\t: '+msg[2] +'\nmessage \t\t: '+msg[3]+'\nsentiment \t\t: '+msg[4]+'\npolarity \t\t:'+msg[5]
        
        self.text.insert(INSERT,output)
        
        self.text.pack(side = TOP)
        
        thread1 = Thread(target = self.back_end)
        
        thread1.setDaemon(True)
        
        thread1.start()

        label4 = Label(self.middleframe,text="Select Username that details you want to see",fg="red",bg="yellow",font=("",12,"bold"))
        
        label4.pack(side=TOP,pady=10)

        Values = ['Compare All'] #,'Aman Kathait','Akshat Negi','Shubham Semwal','Group']

        fp = open('files/group_details.csv')

        tmp = fp.readlines()[-1].split(',')

        Values += tmp[1:]

        self.user = StringVar()
        
        self.comboframe = Frame(self.middleframe,background="brown")
        
        self.comboframe.pack(padx = 150)

        self.UserList = ttk.Combobox(self.comboframe,textvariable = self.user,height=30 , state = 'readonly',postcommand = self.chnageValues)

        self.UserList['values'] = Values
        
        self.UserList.pack(side = LEFT,padx=10)

        self.UserList.current(1)

        self.UserList.bind("<<ComboboxSelected>>",self.select_user)

        self.type = StringVar()
        
        Type = ttk.Combobox(self.comboframe,textvariable = self.type,height=30 , state = 'readonly')
        
        Type['values'] = ('emotion','polarity')
        
        Type.pack(side = LEFT,padx=10)
        
        Type.current(0)
        
        Type.bind("<<ComboboxSelected>>",self.select_type)
        
        self.theme = StringVar()
        
        Theme = ttk.Combobox(self.comboframe,textvariable = self.theme,height=30 , state = 'readonly')
        
        Theme['values'] = ('classic','seaborn-whitegrid','dark_background','ggplot')
        
        Theme.pack(side = LEFT,padx=10)
        
        Theme.current(0)
        
        Theme.bind("<<ComboboxSelected>>",self.select_theme)

        #################

        label5 = Label(self.root,text="Select appropriate diagram to dislpay User Details",fg="red",bg="yellow",font=("",12,"bold"))
        
        label5.pack(side=TOP,pady=10)

        self.bottomframe = Frame(self.root,background="brown",width=700,height=150)
        
        self.bottomframe.pack(side = TOP,pady = 20)

        piechart_image = PhotoImage(file = "images/app/piechart.png")
        
        scatterplot_image = PhotoImage(file = "images/app/scatter.png")
        
        histogram_image = PhotoImage(file = "images/app/histogram.png")

        xls_image = PhotoImage(file = "images/app/xls_icon.png")

        live_image = PhotoImage(file = "images/app/live.png")

        piechart_image = piechart_image.subsample(2,2)
        
        scatterplot_image = scatterplot_image.subsample(2,2)
        
        histogram_image = histogram_image.subsample(2,2)

        xls_image = xls_image.subsample(2,2)

        live_image = live_image.subsample(2,2)

        piechart_button = Button(self.bottomframe,image = piechart_image,command = self.plot_PieChart)
        
        piechart_button.pack(side = LEFT,padx=10)

        scatterplot_button = Button(self.bottomframe, image = scatterplot_image,command = self.scatter_plot)
        
        scatterplot_button.pack(side = LEFT,padx=10)

        histogram_button = Button(self.bottomframe,image = histogram_image,command = self.plot_histogram)
        
        histogram_button.pack(side = LEFT,padx=10)

        xls_button = Button(self.bottomframe,image = xls_image,command = self.open_xls)
        
        xls_button.pack(side = LEFT,padx=10)

        live_button = Button(self.bottomframe,image = live_image,command = self.live_plot)
        
        live_button.pack(side = LEFT,padx=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.root.mainloop()
        



if __name__ == '__main__':

    app = Application()

    print(app.__doc__)

    app.GUI()

