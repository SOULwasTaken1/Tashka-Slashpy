import discord
from discord.commands import slash_command
from discord.ext import commands
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import os
from matplotlib import rcParams
from typing import Optional
import numpy as np
import re

def break_latex_code(latex_code, banned_list):
  pattern = r'(\{[^}]*\})|([a-zA-Z0-9]+)|(\W)'
  elements = re.split(pattern, latex_code)

  cleaned_elements = []
  for element in elements:
    if element:
      if any(banned in element for banned in banned_list):
          element = element
      else:
        element = element.replace('{', '').replace('}', '')
      cleaned_elements.append(element)

  return cleaned_elements

def break_exponent(input_string, break_point):
  pattern = r"|".join(map(re.escape, break_point))
  pattern = f"({pattern})"

  result = re.split(pattern, input_string)
  result = [item for item in result if item]

  return result



def modify_latex_string(elements, banned_list, break_point):
  result = []
  for i, item in enumerate(elements):
    modified_item = ''
    o1 = ['^', '_']
    o2 = ['dfrac', 'frac']
    if elements[i - 1] in o1 or elements[i-1] in o2 or elements[i-2] in o2:
        arr = break_exponent(item,break_point)
        if '}' in arr :  arr.remove('}')
        if '{' in arr : arr.remove('{')
        
        res = []
        mod_item = ''
        for i, item in enumerate(arr):
          if any(banned in item for banned in break_point):
            print(item)
            mod_item = item
          else:
            mod_item = r'\mathscr{' + item + '}'
          res.append(mod_item)
        modified_item = '{' + ''.join(res) + '}'

    elif any(banned in item for banned in banned_list):

      modified_item = item

    elif elements[i] not in banned_list and elements[i-1] not in '_^':
        modified_item = r'\mathscr{' + item + '}'
    else:
        modified_item = item
    result.append(modified_item)


  return ''.join(result)


def latex_to_png(latex_str,size):

  font = {'family': 'serif',
    'style': 'italic'}
  
  fig = plt.figure(facecolor='black')
  plt.axis("off")
  plt.text(0.5,0.5,f"${latex_str}$",size=size,ha="center",va="center",color="white",fontdict=font)

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
    
    banned_list = ['^', '_', '\tan','\cos', '\sin',
     '\log', '\ln', 'e', '\\pi','\sec', r'\to', '\propto'
     '\csc', '\cot', '\arcsin', '\arccos', r'\\dfrac' ,r'\dfrac', 'dfrac'
     '\arctan', '\arccsc', '\\', '{', '}',  '\frac', 'frac', 'int',
     '\\sum', '\\int', '\\lim', '\l\imsup', '\\prod', 'lim', r'\sqrt',
     '\\liminf', '\\liminfsup', '\\liminfinf', '+', '-', ' ', '=',
     '\\infty', '\\inftysim', '\\inftyn', '\\inftyne', '\\inftyne',
     '\\alpha', '\\beta', '\\gamma', '\\delta', '\\epsilon', '\\zeta',
     '\\eta', '\theta', '\iota', '\kappa', '\lambda', '\\mu', r'\nu',
     '\\xi', '\\omicron', '\\rho', '\\sigma' , r'\\tau', '\\upsilon', '\\Omega',
     '\\phi', '\\chi', '\psi', '\\omega', '\\Gamma', '\\Delta', '\\Theta',
     '\\Lambda', '\\Xi', '\\Pi', '\\Sigma', '\\Upsilon', '\\Phi', '\\Psi',
     r'\nless', r'\\nlesseqq', '\\nge', 'r\\ngeq', '\\lesseqq', '\subset',
     '\\supset', '\\subseteq', '\\supseteq', 'r\\nsubset', r'\N', '\R',
     '\Q', '\C', '\Z', '\forall' , '\\exists', '\\nexists', '\\varnothing',
     '\aleph', '\sinh', '\cosh', '\tanh', '\cot', '\coth', '\sech', '\csch',
     '\arcsinh', '\arccosh', '\arctanh', '\arccoth', '\arcsech', '\apporx', '(', ')'
      ]
    # break points for the function
    break_point = ['sec', 'csc', 'cot', 'sin', 'cos', r'tan', 'sec', 'csc',
       'arcsec', 'arccsc', 'arccot', 'arcsin', 'arccos', 'arctan', r'\sqrt' ,
      r'\to', r'\infty', 'ln', 'log', '\alpha', '\beta', '\gamma',
      r'\delta', r'\epsilon', '\zeta', '\eta', r'\theta', r'\iota',
      r'\kappa', '\lambda', '\mu', '\nu', '\omicron', '\rho','{', '}',
      '\sigma', r'\tau', r'\upsilon', r'\Omega', '\phi', '\chi', 'r\psi',
      '\omega', '\Gamma', '\Delta', '\Theta', '\Lambda', '\Xi',
      '\Pi', '\Sigma', r'\Upsilon', r'\Phi', r'\Psi', '\aleph',
      ]

    msg = await ctx.respond("please wait",ephemeral=ephemeral)
    try:
      
      replace_dict = {
          "*": "\cdot",
          "tan": r"\tan",
          "cos": "\cos",
          "sin": "\sin",
          "sec": "\sec",
          "csc": "\csc",
          "cot": "\cot",
          "arcsin": "\arcsin",
          "arccos": "\arccos",
          "arctan": "\arctan",
          "arccsc": "\arccsc",
          "arccot": "\arccot",
          "arcsec": "\arcsec",
          " " : "\;",
          "log" : "\log",
          "ln" : "\ln"
      }
      
        
      elements = break_latex_code(prompt, banned_list)
      modified_latex = modify_latex_string(elements, banned_list, break_point)
      for old, new in replace_dict.items():
        modified_latex = modified_latex.replace(old, new)
       
      latex_to_png(modified_latex,size)
      path = "result.png"
      make_small(path,70)
      with open('result.png', 'rb') as f:
              image = discord.File(f)
      await msg.edit_original_response(content="",file=image)
      os.remove("result.png")
    except Exception as err:
      await msg.edit_original_response(content=f"The LaTeX code you sent was invalid. Please check again.\n```hs\n {err}``` ")
    



def setup(bot):
	bot.add_cog(latex(bot))
