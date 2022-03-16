import aiohttp
import requests

import time, os, json, asyncio, colorama, discord

from discord.ext import commands
from discord.ext import tasks

import re

import pypresence

class Ejactcord:
      def __init__(
          self,
          token,
          discord_api
      ):
          self.token   = token
          self.discord = discord_api

          """
          From: Ejactcord,
          To  : TheOnlyWayUp

          Thank you, for listing the problems wrong with the previous version, 
          very bad headers, using the requests module while supposingly asynchronous, and more. 

          We couldn;t have fixed everything, if it wasnt for you.
          
          Sincerely, Ejactcord Official
          """

          self.headers = {
               'User-Agent'     : '', 
               'Content-Type'   : 'application/json',
               'Accept-Language': 'en-US,en;q=0.5',
               'Authorization'  : token
          }
        
          self.headers

          self.proper_version = [
               "9", "10"
          ]

      async def create_dm_channel(
            self,
            recipents = []
      ):
            """
            Creates a DM channel with .. recipents
            """
            async with aiohttp.ClientSession(headers = self.headers
            ) as session:
                 async with session.post(
                             '%s/users/@me/channels' % (
                                       self.discord
                             ), json = {
                                     'recipents': recipents
                             }
                 ) as response:
                       if response.status in [
                          200,
                          201,
                          203,
                          204,
                       ]:
                          return response.json() 
                       else:
                          if __name__ == "__main__":
                             return []
                            
      async def create_guild(
                self,
                guild_name = ""
      ):
            """
            I don't think this works, but it creates a guild, and returns the json
            """
            async with aiohttp.ClientSession(headers = self.headers
            ) as session:
                 async with session.post(
                            '%s/guilds' % (
                                       self.discord
                            ), json = {
                                    'channels'           : [],
                                    'guild_template_code': '2TffvPucqHkN',

                                    'icon': 'null',
                                    'name': '%s' % (guild_name),

                                    'system_channel_id': 'null'
                            }
                 ) as response:
                      if response.status in [
                         200,
                         201,
                         203,
                         204,
                      ]:
                         return response.json()
                      else:
                         if __name__ == '__main__':
                            return []
                           
      async def fetch_message(
                self,
                channel_id, 
                message_id
      ):
           """
           THIS IS NOT RECOMMENDED TO USE
           - Unstable
           - Technically considered API spam
           """
        
           async with aiohttp.ClientSession(headers = self.headers
           ) as session:
                async with session.post(
                           '%s/channels/%s/messages?limit=1&around=%s' % (
                                        self.discord,

                                        channel_id,
                                        message_id
                           )
                ) as response:
                     if response.status in [
                        200,
                        201,
                        203,
                        204,
                     ]:
                        return response.json()
                     else:
                        if __name__ in "__main__":
                           return []
                          
      async def send_webhook(
                self,
                url,
                title = "",
                description = "",
                custom_json = {}
      ):
            """
            Sends a webhook, either with title & description, or custom json
            """
            if custom_json == {}:
               title       = title,
               description = description

               async with aiohttp.ClientSession() as session:
                    async with session.post(
                          url,
                          json = {
                               'embeds': [{
                                       'title'      : title,
                                       'description': description
                               }]
                          }
                    ) as response:
                         if resoponse.status_code in [
                            200,
                            201,
                            203,
                            204,
                         ]:
                            return response.json()
                         else:
                            if __name__ == "__main__":
                               return []
            else:
               async with aiohttp.ClientSession() as session:
                     async with session.post(
                           url,
                           json = custom_json
                     ) as response:
                          if response.status in [
                             200,
                             201,
                             203,
                             204
                          ]:
                             return response.json()
                          else:
                             if __name__ == "__main__":
                                return []
                               
      async def user(
                self
      ):
           """
           Returns the current logged in user's data, like username, ID, and discriminator
           """
           async with aiohttp.ClientSession(headers = self.headers
           ) as session:
                 async with session.get(
                            '%s/users/@me' % (
                                     self.discord
                            ),                            
                 ) as response:
                      if response.status in [
                         200,
                         201,
                         203,
                         204,
                      ]:
                         return response.json()
                      else:
                         if __name__ == "__main__":
                            return []

      async def change_status(
                self,
                text = ""
      ):
            async with aiohttp.ClientSession(headers = self.headers
            ) as session:
                 async with session.patch(
                            '%s/users/@me/settings' % (
                                 self.discord
                            ),
                            json = {
                                 'custom_status': {
                                        'text'  : '%s' % (
                                               text
                                        )
                                 }
                            }
                 ) as response:
                      if response.status in [
                         200,
                         201,
                         203,
                         204,
                      ]:
                         return response.json()
                      else:
                         if __name__ == "__main__":
                            return []
