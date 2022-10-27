from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
import random
from picamera import PiCamera
from time import sleep
import os
import threading
import datetime
from _thread import start_new_thread
import time
threadId = 1
#from pygtail import Pygtail
REQUEST_KWARGS={
    'proxy_url': 'URL_TO_PROXY',
    'urllib3_proxy_kwargs': {
        'username': 'YOURPROXY',
        'password': 'PASSWORDPROXY',
    }
}




variations = ("{} fuk you")
names = ("andrew", "mask")
statistics = {}

for name in names:
	statistics[name] = 0

updater = Updater(token='YOUR_TOKEN', use_context=True, request_kwargs=REQUEST_KWARGS)


#my_file = open('/home/pi/sample.log')
#my_string = my_file.read()
#my_file.close()



def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="whaaat")
	context.bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/pi/telebot/python-telegram-bot/image.jpg','rb'));

			
	


def pushing(update, context):

	while True:

		my_file = open('/home/pi/telebot/python-telegram-bot/sample.txt','r')

		my_string = my_file.read()
		line = my_file.readline()
		my_file.close()
		print(my_string)

		if (my_string == "*alert*"):
			camera.start_preview()

			camera.capture('/home/pi/telebot/python-telegram-bot/image.jpg')
			
			
			camera.stop_preview()	


			camera.start_preview()
			camera.start_recording('/home/pi/telebot/python-telegram-bot/video.h264')
			sleep(5)
			camera.stop_recording()
			camera.stop_preview()			
			print("before")
			os.system("sudo MP4Box -add /home/pi/telebot/python-telegram-bot/video.h264  /home/pi/telebot/python-telegram-bot/trying.mp4")
			sleep(1)
			context.bot.send_photo(chat_id=update.message.chat_id, photo=open('/home/pi/telebot/python-telegram-bot/image.jpg','rb'));
			context.bot.send_document(chat_id=update.message.chat_id, document=open('/home/pi/telebot/python-telegram-bot/trying.mp4', 'rb'))
			print("after")
			#context.bot.send_message(chat_id=update.message.chat_id, text=open('/home/pi/telebot/python-telegram-bot/sample.txt').read())
			context.bot.send_message(chat_id=update.message.chat_id, text="Alert! Intruder!")
			my_file = open('/home/pi/telebot/python-telegram-bot/sample.txt','w')
			my_string = my_file.write("")
			my_file.close()
			os.system("sudo rm -rf /home/pi/telebot/python-telegram-bot/video.h264  /home/pi/telebot/python-telegram-bot/trying.mp4")


			
		elif (my_string != ""):
			context.bot.send_message(chat_id=update.message.chat_id, text=open('/home/pi/telebot/python-telegram-bot/sample.txt').read())
			my_file = open('/home/pi/telebot/python-telegram-bot/sample.txt','w')
			my_string = my_file.write("")
			my_file.close()

					
		
			


	
def message(update, context):


	if update.message.text.lower().find("pidor") != -1:
		context.bot.send_message(chat_id=update.message.chat_id, text="no you")
		return
	if update.message.text.lower().find("all information") != -1:
		my_file = open('sample.txt')
		my_string = my_file.readline()
		my_file.close()
		context.bot.send_message(chat_id=update.message.chat_id, text= open('sample.txt').read(100))
		return





def stats(update, context):
	res = ""
	for key, value in statistics.items():
		res += key + ": " + str(value) + "\n"
	print(statistics)
	context.bot.send_message(chat_id=update.message.chat_id, text=res)
camera = PiCamera()
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stats', stats))
updater.dispatcher.add_handler(CommandHandler('privet', message))
updater.dispatcher.add_handler(CommandHandler('pushing', pushing))
#updater.dispatcher.add_handler(CommandHandler('stop_pushing', stop_pushing))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message))


updater.start_polling()
updater.idle()
