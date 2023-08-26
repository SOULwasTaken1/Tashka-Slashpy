import discord
import time
from discord.ext import commands
from discord.commands import slash_command
import aiohttp
import os
from typing import Optional

class weather(commands.Cog,name='weather'):

  def __init__(self,bot):
    self.bot = bot

  @slash_command(name='weather',description='Fetches the weather of the given city.')
  async def weather(self,ctx,city:str,ephemeral:Optional[bool]=False):
    try:
      url = "http://api.weatherapi.com/v1/current.json"
      params = {
        "key" : os.environ['WEATHER_KEY'],
        "q" : city
      }
      async with aiohttp.ClientSession() as session:
        async with session.get(url,params=params) as res:
          data = await res.json()
          location = data["location"]["name"]
          temp_c = data["current"]["temp_c"]
          temp_f = data["current"]["temp_f"]
          humidity = data["current"]["humidity"]
          wind_kph = data["current"]["wind_kph"]
          wind_mph = data["current"]["wind_mph"]
          condition = data["current"]["condition"]["text"]
          image_url = "http:" + data["current"]["condition"]["icon"]
  
        embed=discord.Embed(title=f"Weather for {location}",description=f"The Condition in `{location}` is `{condition}`",color=0x631cba)
        embed.add_field(name="Tempreture",value=f"`{temp_c}°C` | `{temp_f}°F`")
        embed.add_field(name="Humidity", value=f"`{humidity}`")
        embed.add_field(name="  Wind Speed",value=f"`{wind_kph}kmp/h` | `{wind_mph}mp/h`")
        embed.set_thumbnail(url=image_url)
  
      return await ctx.respond(embed=embed,ephemeral=ephemeral)
    except KeyError:
      
      embed=discord.Embed(description="**Invalid Location or there was a typo. Please try again.**",color=0xFF0000)
      return await ctx.respond(embed=embed)
        

def setup(bot):
	bot.add_cog(weather(bot))
