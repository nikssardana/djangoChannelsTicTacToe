from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

# def http_consumer(message):
#     response = HttpResponse('Hello world %s'% message.content['path'])
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)

def ws_add(message):
    message.reply_channel.send({'accept': True})
    Group('user1').add(message.reply_channel)

def ws_message(message):
    #Send message to group chat
    Group('user2').send({
        'text': message.content['text'],
        })

def ws_add2(message):
    message.reply_channel.send({'accept': True})
    Group('user2').add(message.reply_channel)

def ws_message2(message):
    #Send message to group chat
    Group('user1').send({
        'text': message.content['text'],
        })

def ws_disconnect(message):
    try:
        Group('user1').discard(message.reply_channel)
    except:
        Group('user2').discard(message.reply_channel)
