from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

# def http_consumer(message):
#     response = HttpResponse('Hello world %s'% message.content['path'])
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)

def ws_message(message):
    #Send message to group chat
    Group('chat').send({
        'text': message.content['text'],
        })
    # message.reply_channel.send({
    #     'text': message.content['text'],
    #     })

def ws_add(message):
    message.reply_channel.send({'accept': True})
    Group('chat').add(message.reply_channel)

def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
