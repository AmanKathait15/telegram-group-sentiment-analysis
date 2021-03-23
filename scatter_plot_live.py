from matplotlib import pyplot as plt
import matplotlib.animation as animation
import random as r
from time import sleep

#plt.style.use('seaborn-whitegrid')
#plt.style.use('dark_background') 
#plt.style.use('ggplot')

fig = plt.figure()

axis = fig.add_subplot(1,1,1)

index = -1

X,Y = [],[]

def animate(i):

	global index

	with open('file.txt','r') as fp:

		global index

		index+=1

		lines = fp.read().splitlines()

		last_line = lines[index] # -1 for last line

		x,y = last_line.split(',')

		x,y = int(x),float(y)

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

		plt.xlabel('chat number')

		plt.ylabel('Polarity')

		plt.legend(labels,loc='upper right')

		plt.ylim([-1,1])

		#plt.autoscale(enable=True, axis='x')

		plt.scatter(X,Y,color="black",markerfacecolor=color,markersize=7)

		# leg = axis.get_legend()

		# leg.legendHandles[0].set_color('red')
		
		# leg.legendHandles[1].set_color('yellow')


ani = animation.FuncAnimation(plt.gcf(),animate, interval=1000)

plt.show()