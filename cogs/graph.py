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


def calculate_value(num_str):
    if num_str.startswith("for"):
        exec_globals = {}
        exec(num_str, exec_globals)
        return exec_globals.get('result', None)
    elif re.match(r'^log\d+$', num_str):
        base = int(num_str[3:])
        return np.log(base)
    elif re.match(r'^\d+\^\d+$', num_str):
        base, exponent = map(int, num_str.split('^'))
        return np.power(base, exponent)

    else:
        try:
            return int(num_str)
        except ValueError:
            try:
                return float(num_str)
            except ValueError:
                return num_str


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
    plt.close()


class graph(commands.Cog,name='graph'):

  def __init__(self,bot):
    self.bot = bot
  @slash_command(name='graph')
  async def graph(self,ctx,line_1:str,
                  line_2:Optional[str]=None,
                  line_3:Optional[str] =None,
                  color_1:Optional[str]="orange",
                  color_2:Optional[str]="cyan",
                  color_3:Optional[str]="magenta",
                  ephemeral:Optional[bool]=False
                 ):
    if line_1.startswith("for"):
      x_arr_s = [line_1]
    else:
      x_arr_s = line_1.split(',')
    x_arr = [calculate_value(num_str) for num_str in x_arr_s]
    if line_2 is not None:
      if line_2.startswith("for"):
        y_arr_s = [line_2]
      else:
        y_arr_s = line_2.split(',')
      y_arr = [calculate_value(num_str) for num_str in y_arr_s]
    else:
      y_arr = []
    if line_3 is not None:
      if line_3.startswith("for"):
        z_arr_s = [line_3]
      else:
        z_arr_s = line_3.split(',')
      z_arr = [calculate_value(num_str) for num_str in z_arr_s]
    else:
      z_arr = []

    plot_three_lines(x_arr,"plot_graph.png",y_arr,z_arr,color_1,color_2,color_3)
    msg = await ctx.respond("please wait",ephemeral=ephemeral)
    with open('plot_graph.png', 'rb') as f:
              image = discord.File(f)
    await msg.edit_original_response(content="",file=image)
    os.remove("plot_graph.png")

def setup(bot):
	bot.add_cog(graph(bot))
