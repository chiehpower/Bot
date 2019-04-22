# Author : Chieh
# Please install below some packages in your termial first.
# pip install itchat
# pip install apscheduler

import itchat
import time
itchat.auto_login(hotReload=True)

from apscheduler.schedulers.blocking import BlockingScheduler
friends = itchat.get_friends(update=True)
groups = itchat.get_chatrooms(update=True)  

# See your friends and their UserName.

def Fname(s):
    x= 0
    for i in s:
        yield x,friends[x]['NickName'],friends[x]['UserName']
        x += 1
friend_list = list(Fname(friends))

friend_list

# This cell is that you can send the message to your friend.
# you should type the message and name.

def sendMessage(Name):
    X = input('Type your message: ')
    for i in range(len(friends)):
        while Name == friends[i]['NickName']:
            itchat.send(X, toUserName=friends[i]['UserName'])
            break
print('Please type the original name of your friend, not the name which was changed before.')
SendName = input('Your Friend Name:')
sendMessage(SendName)

# This cell can let you send the message to your own filehelper. (文件傳輸助手）

message = input()
itchat.send(message, toUserName='filehelper')

# This cell can reply automatically messages, if anyone sends the message to you. 
# However, it will reply the same messages.

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text
itchat.run()

# Of course, you can change some word inteh the position of return. For example, you can type
# return u'Hi, this is automatically reply system. Now I have a little bit busy, 
# and I will reply later. Sorry! I have recived your messages: %s\n' % (msg['Text'])

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return u'Hi, this is automatically reply system. Now I have a little bit busy, and I will reply later. Sorry! I have recived your messages: %s\n' % (msg['Text'])
itchat.run()

# This cell is that you can scheduler the time, 
# and then it will automatically keep sending the messages.

# Now I set that it will send the current time by interval of time.

import datetime
SName = input('Your friend name: ')
def number(Name):
    for i in range(len(friends)):
        while Name == friends[i]['NickName']:
            return i
n = number(SName)
def send():
    global n
    def SSsend(n):
        X= datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return itchat.send(X, toUserName=friends[n]['UserName'])
    return SSsend(n)
model = BlockingScheduler()
model.add_job(send,'interval', seconds=1)
model.start()

# You can change the parameters.

# weeks
# days
# hours
# minutes
# seconds
# start_date(datetime(should use string))
# end_date(datetime(should use string))
# timezone(datetime(should use string))

# and

# date
# interval
# cron

# Chinese reference article:
# https://www.jianshu.com/p/ad2c42245906