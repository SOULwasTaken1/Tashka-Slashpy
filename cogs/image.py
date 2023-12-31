import discord
from discord.commands import slash_command
from discord.ext import commands
import time
import json
import PIL
from io import BytesIO
import aiohttp
import base64
from typing import Optional

class Dropdown(discord.ui.Select):
  def __init__(self,message,images,user):
    self.message = message
    self.images = images
    self.user = user

    options = [
      discord.SelectOption(label="1"),
      discord.SelectOption(label="2"),
      discord.SelectOption(label="3"),
      discord.SelectOption(label="4"),
      discord.SelectOption(label="5"),
      discord.SelectOption(label="6"),
      discord.SelectOption(label="7"),
      discord.SelectOption(label="8"),
      discord.SelectOption(label="9"),
    ]
    super().__init__(
      placeholder="Choose the Image you want to see",
      min_values = 1,
      max_values = 1,
      options = options, 
      )
  
  async def callback(self, interaction: discord.Interaction):
    if not self.user == interaction.user.id:
      await interaction.response.send_message("You are not the author of this message", empheral=True)
    selection = int(self.values[0])-1
    image = BytesIO(base64.decodebytes(self.images[selection].encode("utf-8")))
    return await interaction.response.edit_message(content="Generated By **Craiyon.com**",
                                             file=discord.File(image, "!.png"),
                                             view=DropdownView(self.message,self.images,self.user))

class DropdownView(discord.ui.View):
  def __init__(self,message,images,user):
    self.message = message
    self.images = images
    self.user = user
    super().__init__()
    self.add_item(Dropdown(self.message,self.images,self.user))
      
  
class image(commands.Cog,name='image'):
  

  def __init__(self,bot):
    self.bot = bot
  

  @slash_command(name="imagine",description="Generates an Image using user's prompt")
  async def imagine(self, ctx, prompt:str,ephemeral:Optional[bool]=False):
    ETA = int(time.time()+60)
    msg = await ctx.respond(f"# > Please Wait <t:{ETA}:R>",ephemeral=ephemeral)
    async with aiohttp.request("POST","https://backend.craiyon.com/generate",json={"prompt":prompt}) as res:
      data = await res.json()
      images = data['images']
      image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
      return await msg.edit_original_response(content="Generated By **Craiyon.com**",                         
                                              file=discord.File(image,"!.png"),
                                              view=DropdownView(msg,images,ctx.author.id))
                        


def setup(bot):
	bot.add_cog(image(bot))