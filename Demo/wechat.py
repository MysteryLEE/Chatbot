import response
from wxpy import *
bot = Bot()

my_friend = bot.friends().search('Jay Huang')[0]
my_friend.send(response.introduction)
my_friend.send(response.company)
my_friend.send(response.question)
@bot.register(my_friend)
def reply_my_friend(msg):
#    return 'received: {} ({})'.format(msg.text, msg.type)
    return response.respondf(msg.text)

embed()
