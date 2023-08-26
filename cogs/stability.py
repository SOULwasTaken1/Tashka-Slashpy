import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import discord
from discord.commands import slash_command
from discord.ext import commands
import time

class stability(commands.Cog,name='stability'):

  def __init__(self,bot):
    self.bot = bot
  
  @slash_command(name="imagine",description="Generates an Image using user's prompt")
  async def imagine(self, ctx,prompts:str):
    msg = await ctx.respond("Please wait...")
    stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], 
    verbose=True, 
    engine="stable-diffusion-xl-1024-v0-9", 
    )
    answers = stability_api.generate(
    
      prompt=prompts,
      seed=992446758, 
      steps=50, 
      cfg_scale=8.0, 
      width=512, 
      height=512, 
      samples=3,
      sampler=generation.SAMPLER_K_DPMPP_2M                                                
    )
    images = []
    for resp in answers:
      images.append(resp)
    return await msg.edit_original_response(file=[discord.File(images[0],"!.png"),             
                                                  discord.File(images[1],"!!.png"),
                                                  discord.File(images[2],"!!!.png"),
                                                  discord.File(images[3],"!!!!.png")
                                                 ])
                                            
            

def setup(bot):
	bot.add_cog(stability(bot))