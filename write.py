
from time import sleep

from random import random,randint

x = 0

while(True):

	sleep(0.1)

	x+=1

	if(randint(0,9)%2==0):

		y = random() * -1

	else:

		y = random()

	print(x,y,sep=",")

	with open('file.txt','a') as fp:

		fp.write(str(x)+","+str(y)+"\n")

