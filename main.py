import os
from os import system
from webserver import keep_alive
import discord



bot = discord.Bot(intents=discord.Intents.all(),case_insensitive=True,help_command=None)
bot.author_id = 801058284106678273  
key = os.environ['BOT_TOKEN']


@bot.event 
async def on_ready():  
    print("I'm in")
    print(bot.user)  
  

extensions = [
  'cogs.ping',
  'cogs.time',
  'cogs.image',
  'cogs.help',
  'cogs.dank',
  'cogs.eightball',
  'cogs.mod',
  'cogs.purge',
  'cogs.bmr',
  'cogs.gpt',
  'cogs.font',
  'cogs.utils',
  'cogs.brainfuk',
  'cogs.weather',
  'cogs.wordle',
  'cogs.latex',
  'cogs.funds'
]

if __name__ == '__main__':  
	for extension in extensions:
		bot.load_extension(extension)  

keep_alive()  
try:
  bot.run(key)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')
