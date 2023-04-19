import datetime
import time
import os
while True:
	if datetime.datetime.now().minute % 2 == 0:
		os.system("netsh wlan show interfaces")
		time.sleep(20)