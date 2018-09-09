from _pydecimal import Decimal
from datetime import *


class Renderer(object):

    def renderData(data):
        DataFilePath = "files\sampleText.txt"
        pullData = open(DataFilePath, "r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        for eachLine in dataList:
            if len(eachLine) > 1:
                date, temp, cond, ph = eachLine.split(',')
                timestamp1 = datetime.strptime(date, fmt)
                timestamp2 = datetime.strptime(str(datetime.now()), fmt)
                interval = (timestamp2 - timestamp1)
                if interval.days <= 1:
                    date, time = date.split(' ')
                    hour, minute, second = time.split(':')
                    # xList.append(Decimal(hour))
                    xAxisDateTime = str(timestamp1.date()) + " " + str(timestamp1.hour) + ":00"
                    xList.append(xAxisDateTime)
                    if data == 'temp':
                        yList.append(Decimal(temp))
                    if data == 'cond':
                        yList.append(Decimal(cond))
                    if data == 'ph':
                        yList.append(Decimal(ph))
