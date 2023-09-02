import discord
from discord.commands import slash_command
from discord.ext import commands
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import os
from typing import Optional
import numpy as np
import re


def latex_to_png(latex_str,size):
  

  fig = plt.figure(facecolor='black')
  plt.axis("off")
  plt.text(0.5,0.5,f"${latex_str}$",size=size,ha="center",va="center",color="white",)

  png_path = "result.png"

  plt.savefig(png_path, format="png",bbox_inches="tight", pad_inches=0.4,transparent=True)
  plt.close(fig)



def make_transp(path):
    img = Image.open(path)
    img = img.convert("RGBA")
 
    datas = img.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save(path, "PNG")


def make_small(path,size):
  image = Image.open(path)
  
  percentage = size
  
  width, height = image.size
  new_width = int(width * (100 - percentage) / 100)
  new_height = int(height * (100 - percentage) / 100)
  resized_image = image.resize((new_width, new_height))
  resized_image.save('result.png')
  


class latex(commands.Cog,name='latex'):

  def __init__(self,bot):
    self.bot = bot

  
  @slash_command(name='render', description= 'Uses latex to render math equations')
  async def render(self, ctx,prompt:str,
                   size:Optional[int]=100,
                   ephemeral:Optional[bool]=False
                  ):

    
    msg = await ctx.respond("please wait",ephemeral=ephemeral)
    try:
      latex_to_png(prompt,size)
      path = "result.png"
      make_small(path,70)
      with open('result.png', 'rb') as f:
              image = discord.File(f)
      await msg.edit_original_response(content="",file=image)
      os.remove("result.png")
    except:
      await msg.edit_original_response(content="The LaTeX code you sent was invalid. Please check again.",ephemeral=ephemeral)



def setup(bot):
	bot.add_cog(latex(bot))
