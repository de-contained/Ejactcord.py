import json, discord, requests
import os

from discord.ext import commands
from discord.ext import tasks

class BotBypass:
      def __init__(self):
          print('[!] BOT BYPASS | Loaded')
          print

      def setup_embed(
          self,
          title = "",
          description = "",
          color = ""
      ): 
          other_link = "&redirect=https%253A%252F%252Fdiscord.com%252Fchannels%252F%2540me"
          other_link 
        
          return "https://embed.rauf.workers.dev/?title=%s&description=%s&color=%s%s" % (
                 title.replace(
                        " ", 
                        "%2520"
                 ), description.replace(
                        " ", 
                        "%2520"
                 ), color, other_link
          )
      
class Bot:
      def __init__(self, token):
          self.token = token
          self.token

      async def sendEmbed(
          self,
          title = "", description = "", color = "",
          channel = ""
      ):
          ## EMBED CONTENT ##
          embed = BotBypass().setup_embed(
                  title       = title,
                  description = description,
                  color       = color
          ) 
          ## PASTE ##
          with open('ejactcord/embed_bypass.txt', 'r') as embedbypass:
               for line in embedbypass.readlines():
                   data = line.replace("{user.content}", "").replace("{user.embedLink}", embed)
        
          res = requests.post(
                   "https://discord.com/api/v9/channels/%s/messages" % (channel),
                   headers = {"Authorization": self.token}, json = {
                                                            "content": data
                   }
          )

          if res.status_code in [
                 200,
                 201,
                 203,
                 204,
          ]:
              return res.json()
          else:
              return []
        
      def ifContent(self, message, determine):
            if message[0]['content'] == determine:
               return True
              
      async def fetchMessage(self, channel_id, message_id):
          return requests.get(
                 'https://discord.com/api/v9/channels/%s/messages?limit=1&around=%s' % (
                              channel_id,
                              message_id
                 ), headers = {
                            "Authorization": "%s" % (self.token)
                 }
          ).json()