import sopel
import requests

@sopel.module.commands('yp', 'ур')
def porncomment(bot, trigger):
  search_for = trigger.group(2)
  header = {'accept': 'application/json'}
  try:
    rpc = requests.get("https://porncomment.com", {'search': search_for}, headers=header).json()["comments"]
    comment = rpc[0]['body']
    bot.say(comment, max_messages=2)
  except IndexError:
    bot.say("Nothing...")

@sopel.module.commands('ypurl', 'урурл')
def porncomment_url(bot, trigger):
  search_for = trigger.group(2)
  header = {'accept': 'application/json'}
  try:
    rpc = requests.get("https://porncomment.com", {'search': search_for}, headers=header).json()["comments"]
    comment = rpc[0]['body']
    url = rpc[0]['source_url']
    full_comment = '%s - %s' %(comment, url)
    bot.say(full_comment, max_messages=2)
  except IndexError:
    bot.say("Nothing...")
