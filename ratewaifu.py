import sopel
import hashlib
import random

@sopel.module.commands('rate', 'waifu', 'ratewaifu', 'waifurate', 'рейт', 'вайфу', 'рейтвайфу', 'вайфурейт')
def ratewaifu(bot,trigger):
    if trigger.group(2):
        seed = hashlib.md5(("{}".format(trigger.group(2))).encode('utf-8')).hexdigest()
        random.seed(seed)
        bot.say("Твоя вайфу {} из 10".format(random.randint(0,10)))
