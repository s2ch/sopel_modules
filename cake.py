from __future__ import unicode_literals, absolute_import, print_function, division
import sys

from sopel.module import commands

if sys.version_info.major >= 3:
    unichr = chr


@commands('cake', 'торт', 'тортик', 'торта')
def cake(bot, trigger):
    if not trigger.group(2):
        bot.action(u'дал {}кусочек пирога и стакан тёплого молока. '
                    '\U0001F382'.format(trigger.nick))
        return

    target = trigger.group(2)
    bot.action(u'дал {} кусочек пирога и стакан тёплого молока... '
                'Приятного аппетита от {}! \U0001F382'.format(target, trigger.nick))
    return

if __name__ == '__main__':
    pass
