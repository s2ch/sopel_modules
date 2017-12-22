# -*- coding: utf-8 -*-

from random import choice
import time
from sopel import module


def what(bot, input):
    bot.say('Help: https://raw.githubusercontent.com/s2ch/sopel_mods/master/commands.txt')
what.commands = ['help', 'halp', 'commands', 'cmds', 'хелп', 'халп', 'комманды', 'справка']


def elita(bot, input):
    bot.say('┌─┐')
    bot.say('┴─┴')
    bot.say('ಠ_ರೃ')
elita.commands = ['elita', 'элита']


def dunno(bot, input):
    bot.say('¯\_(ツ)_/¯')
dunno.commands = ['dunno', 'idunno', 'дунно', 'айдунно']


def dealwithit(bot, input):
    bot.say('(•_•)')
    bot.say('( •_•)>⌐■-■')
    bot.say('(⌐■_■)')
dealwithit.commands = ['dwi', 'дви']


def what(bot, input):
    bot.say('ಠ_ಠ')
what.commands = ['what', 'чё']


def facepalm(bot, input):
    bot.say('(>ლ)')
facepalm.commands = ['facepalm', 'рукалицо', 'фейспалм', 'фейспальм']


def ping(bot, input):
    bot.say('( •_•)O*¯`·.   |')
ping.commands = ['ping', 'пинг']


def pong(bot, input):
    bot.say('               |   .·´¯`°Q(•_• )')
pong.commands = ['pong', 'понг']


def test(bot, input):
    bot.say('Хуест!')
test.commands = ['test', 'тест']


def hi(bot, input):
    choices = ['o/', '\o']
    bot.say(choice(choices))
hi.commands = ['hi', 'hello', 'greetings', 'hola', 'bonjour', 'хай']


def yay(bot, input):
    bot.say('\o/')
yay.commands = ['yay', 'woot', 'w00t', 'friday', 'йай', 'пятница']


def rickroll(bot, input):
    bot.say('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
rickroll.commands = ['rick', 'astley', 'rick astley', 'rickroll', 'рикролл', 'рик']
