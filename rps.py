from sopel import module,tools
from random import choice
import time

COOLDOWN = 15

STRINGS = {
    'WIN':              ["Ктооо?! Кто дуэль, какой, со мной давай дуэль %s!", "Не понял %s ситуацию немжножко...", "Immolate Improved! %s!", "Со мной давай дуэль %s! С кем и кого ты там, блять, ты чё вообще вырву, блять..."],
    'LOSS':             ["Я попросил тебя проверить мой файер резист... %s!", "Иммолейт у меня... %s!"],
    'TIE':              ["Смотри, файер резист... %s!"]
}

OPTIONS=['камень','бумага','ножницы']

@module.commands('rps', 'кнб')
def rps(bot, trigger):
    global OPTIONS
    if not trigger.group(3) or trigger.group(3) not in OPTIONS:
        bot.say("Испытай свою судьбу! Выбери оружие: камень, ножницы или бумага.")
        return module.NOLIMIT
    playersel=trigger.group(3).lower()
    time_since = time_since_last_rps(bot, trigger.nick)
    if time_since < COOLDOWN:
        bot.notice("Подожди %d секунд." % ( COOLDOWN- time_since), trigger.nick)
        return module.NOLIMIT
    botsel=choice(OPTIONS)
    bot.say("%s vs %s..." % (playersel, botsel))
    if botsel==playersel:
        bot.say(choice(STRINGS['TIE']) % trigger.nick)
        update_stats(bot, trigger.nick , 0)
    elif OPTIONS.index(botsel)-1 == OPTIONS.index(playersel):
        bot.say(choice(STRINGS['LOSS']) % trigger.nick)
        update_stats(bot, trigger.nick,-1)
    else:
        bot.say(choice(STRINGS['WIN']) % trigger.nick)
        update_stats(bot, trigger.nick,1)
    wins,losses,ties = get_stats(bot,trigger.nick)
    bot.say('Статистика: \x0304%d\x03 побед, \x0304%d\x03 проигрышей, \x0304%d\x03 ничья.' % (wins, losses, ties))
    bot.db.set_nick_value(trigger.nick, 'rps_last', time.time())

def get_stats(bot, nick):
    wins = bot.db.get_nick_value(nick, 'rps_wins') or 0
    losses = bot.db.get_nick_value(nick, 'rps_losses') or 0
    ties = bot.db.get_nick_value(nick, 'rps_ties') or 0
    return wins, losses, ties

def update_stats(bot, nick, won=0):
    wins, losses, ties = get_stats(bot,nick)
    if won == -1:
        bot.db.set_nick_value(nick, 'rps_losses',losses+1)
    if won == 0:
        bot.db.set_nick_value(nick, 'rps_ties',ties+1)
    if won == 1:
        bot.db.set_nick_value(nick, 'rps_wins',wins+1)

def time_since_last_rps(bot, nick):
    now = time.time()
    last = bot.db.get_nick_value(nick, 'rps_last') or 0
    return abs(now - last)
