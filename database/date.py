import re
import sys

def Month (month):
    #print ('.....[Month Transform]....')
    month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    m = month[:3]
    index = month_list.index(m) + 1
    if index > 9:
        mon_replace = str(index)
        #print ('mon_replace:', mon_replace)
        return mon_replace
    else:
        mon_replace = '0' + str(index)
        #print ('mon_replace:', mon_replace)
        return mon_replace



def get_date(data):
    
    pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-3]{0,1}\d,{0,1} [1|2]\d{3})|([0_3]{0,1}\d{0,1} {0,1}(January|February|March|April|May|June|July|August|September|October|November|December){0,1} [1|2]\d{3})|(\d{1,2}/\d{1,2}/[1|2]\d{3})|([1|2]\d{3}-\d{1,2}-\d{1,2})|([1|2]\d{3}-[1|2]\d{3})'
    years = {'ID','date'}
    with open(data) as f:
        lines = f.readlines()
        ID = len(lines)
        for i,l in zip(range(ID), lines):
            match = re.search(pattern, l)
            if match:
                date = match.group(0)
                dash = '-'
                complement = 'XX'
                p1 = '[0-3]{0,1}\d ((January|Jan)|(February|Feb)|(March|Mar)|(April|Apr)|May|(June|Jun)|(July|Jul)|(August|Aug)|(September|Sep|Sept)|(October|Oct)|(November|Nov)|(December|Dec)) [1|2]\d{3}' # 30 June 2019
                p2 = '((January|Jan)|(February|Feb)|(March|Mar)|(April|Apr)|May|(June|Jun)|(July|Jul)|(August|Aug)|(September|Sep|Sept)|(October|Oct)|(November|Nov)|(December|Dec)) ([0-3]{0,1}\d){0,1},{0,1} {0,1}([1|2]\d{3})' # Sep 23, 2019   or January 2017
                p3 = '\d{1,2}/\d{1,2}/[1|2]\d{3}' # 28/03/2018
                p4 = '[1|2]\d{3}-[1|2]\d{3}' # 2018-2020
                p5 = '[1|2]\d{3}' # 2017
                if re.search(p1, date):
                    #print ('P1')
                    list = re.split(' ', date)
                    D = list[0]
                    if len(D) == 1:
                        D = '0' + D
                        #print ('D:', D)
                    M = Month(list[1])
                    #print ('M:', M)
                    Y = list[2]
                    #print ('Y:', Y)
                    date = Y + dash + M + dash + D
                    print (i + 1, date)
                elif re.search(p2, date):
                    #print ('P2')
                    list = re.split(' ', date)
                    if list[0] != '':
                        M = Month(list[0])
                        #print ('M:', M)
                        D = list[1].strip(',')
                        if len(D) == 1:
                            D = '0' + D
                            #print ('D:', D)
                        Y = list[2]
                        #print ('Y:', Y)
                        date = Y + dash + M + dash + D
                        print (i + 1, date)
                    else:
                        M = Month(list[1])
                        #print ('M:', M)
                        Y = list[2]
                        #print ('Y:', Y)
                        date = Y + dash + M + dash + complement
                        print (i + 1, date)
                elif re.search(p3, date):
                    #print ('P3')
                    list = re.split('/', date)
                    D = list[0]
                    if len(D) == 1 :
                        D = '0' + D
                       # print ('D:', D)
                    M = list[1]
                    if len(M) >1:
                        if int(M) >= 12 :
                            m = D
                            D = M
                            M = m
                           # print ('M:', M)
                    else:
                        M = '0' + M
                        #print ('M:', M)
                    Y = list[2]
                    #print ('Y:', Y)
                    date = Y + dash + M + dash + D
                    print (i + 1, date)
                elif re.search(p4, date):
                    #print ('P4')
                    list = re.split('-', date)
                    Y1 = list[0]
                    Y2 = list[1]
                    date = Y1 + dash + complement + dash + complement + dash + Y2 + dash + complement + dash + complement
                    print (i + 1, date)
                elif re.search(p5, date):
                    date = (date + dash + complement + dash + complement)
                    date = re.sub('.* ', '', date)
                    print (i + 1, date)

if __name__ == "__main__": get_date("data.txt")
