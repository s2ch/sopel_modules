from __future__ import unicode_literals, absolute_import, print_function, division
import sys

from sopel.module import commands

if sys.version_info.major >= 3:
    unichr = chr


@commands('zalupa', 'залупа')
def penisskin(bot, trigger):
    if not trigger.group(2):
        bot.action(u'повесил {}залупу на воротник.'.format(trigger.nick))
        return

    target = trigger.group(2)
    bot.action(u'С гордостью повесил залупу на воротник {}!'' C любовью от {}!'.format(target, trigger.nick))
    return

if __name__ == '__main__':
    pass
