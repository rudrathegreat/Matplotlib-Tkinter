import datetime
from random import randint
from time import sleep

while True:

    temp = randint(150, 350)/10
    cond = randint(1100, 1450)
    pH = randint(300, 900)/100
    path = 'files\sampleText.txt'
    file_handle = open(path, 'a')
    present = datetime.datetime.now()
    file_handle.write(str(present) + ',' + str(temp) + ',' + str(cond) + ',' + str(pH) + "\n")
    file_handle.close()
    sleep(20)
