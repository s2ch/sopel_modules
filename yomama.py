from sopel.module import commands
import requests


@commands('yomama', 'мама', 'мамка')
def yomama(bot, trigger):
    r = requests.get('http://api.yomomma.info/')
    joke = r.json()['joke']
    bot.say(joke)
