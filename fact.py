import sopel
import random

@sopel.module.commands('fact', 'факт', 'факты')
def fact(bot, trigger):
    x = [
        "Аниме для пидоров!",
        "Гном - лучшее ДЕ!"
        ]

    bot.say("ФактЪ: {}".format(random.choice(x)))
