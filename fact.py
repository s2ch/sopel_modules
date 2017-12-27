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
    filepath = '/home/sopel/.sopel/modules/fact.txt'
    if trigger.group(2) is None:
        factfile = open(filepath, 'r')
        bot.say("ФактЪ: {}".format(random_line(factfile)))
        factfile.close()
        return
    if trigger.group(2).startswith('add'):
        newline = trigger.group(2)[4:] + '\n'
        factfile = open(filepath, 'r')
        if newline in factfile.read():
            bot.say('И так знаю!')
            factfile.close()
            return
        factfile = open(filepath, 'a')
        factfile.write(trigger.group(2)[4:] + '\n')
        bot.say('Записал!')
    else:
        factfile = open(filepath, 'r')
        bot.say("ФактЪ: {}".format(random_line(factfile)))
    factfile.close()
