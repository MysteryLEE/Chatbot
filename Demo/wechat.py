import response
from wxpy import *
bot = Bot()

my_friend = bot.friends().search('name')[0] # Replace name with the friend's WeChat name
my_friend.send(response.introduction)
my_friend.send(response.company)
my_friend.send(response.question)
@bot.register(my_friend)
def reply_my_friend(msg):
#    return 'received: {} ({})'.format(msg.text, msg.type)
    return response.respondf(msg.text)

embed()
