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


COLORS = [
    'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white',
    'orange', 'purple', 'brown', 'pink', 'gray', 'gold', 'silver',
    'navy', 'lime', 'teal', 'aqua', 'fuchsia', 'maroon', 'olive', 'indigo'
]


def plot_three_lines(y1_data, save_path, y2_data=None, y3_data=None, line1_color='orange', line2_color='cyan', line3_color='magenta'):
    fig, ax = plt.subplots()

    min_len = min(len(y1_data), len(y2_data or []), len(y3_data or []))
    max_len = max(len(y1_data), len(y2_data or []), len(y3_data or []))

    x_data = np.arange(max_len)

    ax.plot(x_data[:len(y1_data)], y1_data, label='Line 1', color=line1_color)

    if y2_data is not None and len(y2_data) > 0:
        ax.plot(x_data[:len(y2_data)], y2_data, label='Line 2', color=line2_color)

    if y3_data is not None and len(y3_data) > 0:
        ax.plot(x_data[:len(y3_data)], y3_data, label='Line 3', color=line3_color)

    ax.set_xlim(0, max_len - 1)

    if any([y1_data, y2_data, y3_data]):
        min_y = min([min(y) for y in [y1_data, y2_data, y3_data] if y is not None and len(y) > 0])
        max_y = max([max(y) for y in [y1_data, y2_data, y3_data] if y is not None and len(y) > 0])
        ax.set_ylim(min_y, max_y)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    legend = ax.legend()
    legend.set_frame_on(False)

    for text in legend.get_texts():
        text.set_color('white')

    plt.savefig(save_path, transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

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
  async def command_searcher(self: discord.AutocompleteContext):
    return [
      color for color in COLORS
    ]

  async def get_commands(ctx: discord.AutocompleteContext):
    return [color for color in COLORS if color.startswith(ctx.value.lower())]
  
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

  @slash_command(name='graph')
  async def graph(self,ctx,line_1:str,
                  line_2:Optional[str]=None,
                  line_3:Optional[str] =None,
                  color_1:Optional[str]="orange",
                  color_2:Optional[str]="cyan",
                  color_3:Optional[str]="magenta",
                  ephemeral:Optional[bool]=False
                 ):
    x_arr_s = line_1.split(',')
    x_arr = [int(num) for num in x_arr_s]
    if line_2 is not None:
      y_arr_s = line_2.split(',')
      y_arr = [int(num) for num in y_arr_s]
    else:
      y_arr = []
    if line_3 is not None:
      z_arr_s = line_3.split(',')
      z_arr = [int(num) for num in z_arr_s]
    else:
      z_arr = []

    plot_three_lines(x_arr,"plot_graph.png",y_arr,z_arr,color_1,color_2,color_3)
    msg = await ctx.respond("please wait",ephemeral=ephemeral)
    with open('plot_graph.png', 'rb') as f:
              image = discord.File(f)
    await msg.edit_original_response(content="",file=image)
    os.remove("plot_graph.png")


def setup(bot):
	bot.add_cog(latex(bot))
