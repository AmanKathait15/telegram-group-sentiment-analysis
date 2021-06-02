# telegram-group-sentiment-analysis
 
"A GUI based desktop application that can monitor the activities of a telegram group by reading a text message in a group chat using Telegram bot. It then uses a supervised machine learning model to classify chats in “very positive” , “positive”, “neutral” , “negative” and “very negative” classes and further shows the result to admin in different graphs like pie chart , histogram , bar graph , scatter plot and line plot in a desktop application."

# Heroku Web App 

[tgsab-major-project.herokuapp.com](https://tgsab-major-project.herokuapp.com/)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/webapp.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/wp2.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/wp3.png)



# Desktop Application Screenshot

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/gui.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/Figure_7.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/Figure_8.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/Figure_3.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/Figure_1.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/Figure_2.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/Figure_6.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/live2.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/live1.png)

## Telegram Bot


![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/chat2.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/help.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/mr.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/gr.png)


## User Records

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/csv1.png)

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/csv2.png)

## Model Accuracy

# Using Bag of Words

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/bgw.png)

#  Using ( Tf-Idf ) term frequency–inverse document frequency

![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/tfidf.png)
 
 
 ## python module used
 
 
 1 telebot\
 2 sklearn\
 3 pandas\
 4 time\
 5 tkinter\
 6 threading\
 7 matplotlib\
 8 textblob\
 9 numpy\
 10 telepot\
 11 text2emotion\
 12 Flask
 
 ## Step 1 - installation
 
type command in terminal : **pip install -r requirement.txt**

or download libraries individually

type command in terminal : **pip install textblob**  check latest version [here](https://pypi.org/project/textblob/)<br>
type command in terminal : **pip install pyTelegramBotAPI**  check latest version [here](https://pypi.org/project/pyTelegramBotAPI/)<br>
type command in terminal : **pip install telepot**  check latest version [here](https://pypi.org/project/telepot/)<br>
type command in terminal : **pip install text2emotion**  check latest version [here](https://pypi.org/project/text2emotion/)<br>

 ## Step 2 - Enter your bot token , telegram group id and Heroku Web App url in confi.py file
 
 ![final output screen shot](https://github.com/AmanKathait15/telegram-group-sentiment-analysis/blob/main/readme_images/config.png)
 
 to know how to create telegram bot check this [article](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot)
 
 to find telegram group id check [this](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
 
 ## Step 3 - Run in your system
 
 type command in terminal : **python3 bot.py** then **python3 app.py** then enter input using telegram app
 
 ## Step 4 deploy bot in cloud
 
 first create an app in [Herkou](https://dashboard.heroku.com/login) then follow their guidelines step by step.
 
 ## References
 
 [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)\
 [https://towardsdatascience.com/twitter-sentiment-analysis-using-fasttext-9ccd04465597](https://towardsdatascience.com/twitter-sentiment-analysis-using-fasttext-9ccd04465597)\
 [https://towardsdatascience.com/twitter-sentiment-analysis-classification-using-nltk-python-fa912578614c](https://towardsdatascience.com/twitter-sentiment-analysis-classification-using-nltk-python-fa912578614c)\
 [https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/)\
 [https://www.youtube.com/watch?v=eFdPGpny_hY](https://www.youtube.com/watch?v=eFdPGpny_hY)\
 [https://pypi.org/project/googletrans/](https://pypi.org/project/googletrans/)\
 [https://textblob.readthedocs.io/en/dev/_modules/textblob/classifiers.html](https://textblob.readthedocs.io/en/dev/_modules/textblob/classifiers.html)\
 [https://textblob.readthedocs.io/en/dev/classifiers.html](https://textblob.readthedocs.io/en/dev/classifiers.html)\
 [https://www.geeksforgeeks.org/saving-a-machine-learning-model/](https://www.geeksforgeeks.org/saving-a-machine-learning-model/)
