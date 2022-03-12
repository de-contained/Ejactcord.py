# 🍆.py
Asynchronous API Wrapper for Discord regarding message reading, embed support, and more.

## Documentation
A very simple to use API wrapper, that uses discord.py and ejactcord.py to do simple things. 

### Interactions
This is not released in `v.1`, but it allows clicking buttons, and using slash commands

```py
bot.click(
    message_id   = "", 
    channel_id   = ""
    button_label = ""
)
```
### Embeds
Although, it is not stable. It uses **rauf's** embed generator, and requests, to send the embed to the current channel. 

#### Unstable Functions
- Text to Embed
- Embed to Message  


```py
await bot.sendEmbed(
      title       = "Ejactcord",
      description = "🍆",
      color       = "00000"
)
```

### Check Message
This is unneeded, but it is for `on_message` events, if you use that. 

```py
@bot.event
async def on_message(message):
      msg = client.fetch_message(channel_id = message.channel.id, message_id = message.id)
      
      if ifContent(message = msg, determine = "!credits"):
         message.reply('Ejactcord')
```
