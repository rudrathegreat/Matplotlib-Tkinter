import datetime
from random import randint
from time import sleep

while True:
    temp = randint(15, 35)
    path = 'D:\Rudra\Python\Code\Displayer\sampleText.txt'
    file_handle = open(path, 'a')
    present = datetime.datetime.now()
    file_handle.write(str(present) + ',' + str(temp) + "\n")
    file_handle.close()
    sleep(20)
