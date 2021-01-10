# This notification app made by Abhishek Kumar

# This is english to hindi vocabulary notification app. It give 
# nofication every 10 min.

# It is open source app anyone change it and use it. 


import time 
import schedule
import random
from plyer import notification 

def Notification(): 
	file = open("notify/words.txt").readlines()
	word = random.choice(file)
	notification.notify( 
			title = "English Vocabulary", 
			message = word,
			app_icon = "/home/abhishek/Desktop/notif.jpeg",
			timeout = 15
					) 
schedule.every(10).minutes.do(Notification)		#for minute setting 
#schedule.every().hour.do(notification)			#for hour setting

while True:
	schedule.run_pending()
	time.sleep(1)
