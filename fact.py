import sopel
import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line


@sopel.module.commands('fact', 'факт', 'факты')
def fact(bot, trigger):
    x = [
        # "Аниме лудше пидоров!",
        # "Гном - лучшее ДЕ!"
        "hi"
        ]


#    bot.say("ФактЪ: {}".format(random.choice(x)))
    factfile = open('/home/sopel/.sopel/modules/fact.txt')
    bot.say("ФактЪ: {}".format(random_line(factfile)))
    factfile.close()
