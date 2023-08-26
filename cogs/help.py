import discord
from discord.commands import slash_command
from discord.ext import commands
from Emojies import arrow,arrow2,greenEmoji,grayEmoji,yellowEmoji
import time as t
from discord.commands import option
from typing import Optional


COMMANDS = ["help",
            "time",
            "font",
            "mute",
            "unmute",
            "kick",
            "purge",
            "nuke",
            "bmr",
            "wordle",
            "weather",
            "imagine",
            "render",
            "serverinfo",
            "userinfo",
            "brainfuck",
            "ask"
           ]


class pageView(discord.ui.View):
  def __init__(self,page1,page2,hide):
    self.page1 = page1
    self.page2 = page2
    self.hide = hide
    super().__init__()

  @discord.ui.button(label="<",style=discord.ButtonStyle.gray)
  async def previous(self,button: discord.ui.button, interaction: discord.Interaction):

    await interaction.response.edit_message(embed=self.page1)

  @discord.ui.button(label=">",style=discord.ButtonStyle.gray)
  async def next(self,button: discord.ui.button, interaction: discord.Interaction):
    
    await interaction.response.edit_message(embed=self.page2)

    
class help(commands.Cog,name='help'):

  def __init__(self,bot):
    self.bot = bot
  
  async def command_searcher(self: discord.AutocompleteContext):
    return [
      command for command in COMMANDS
    ]
  async def get_commands(ctx: discord.AutocompleteContext):
    """Returns a list of colors that begin with the characters entered so far."""
    return [command for command in COMMANDS if command.startswith(ctx.value.lower())]

  @slash_command(name="help",description="This command helps you to see all the commands and know what they do")
  @option("command", description="Pick a command!", autocomplete=get_commands)
  async def help(self,ctx,command,ephemeral:Optional[bool]=False):
    pfp = ctx.author.avatar

    match command:
      case "help":
        
        first = f"""
        
</help:1121845078957236375> {arrow2} **Sends this embed**
</time:1116611178827886613> {arrow2} **Generates a discord timestamp!**
</font:1123988526078361711> {arrow2} **Changes the font of your message!**
</mute:1123817226110251008> **(MOD)** {arrow2} ** Mutes mentioned member with timer**
</unmute:1123817226110251009> **(MOD)** {arrow2} **Unmutes mentioned member**
</kick:1123817226110251010> **(MOD)** {arrow2} **kicks the mentioned member** 
</purge:1123820161019953182> **(MOD)** {arrow2} **Purges messages**
</nuke:1123820161019953183> **(MOD)** {arrow2} **Deletes the channel and makes a clone**
</bmr:1123823334426157086> {arrow2} **Calculates Your BMR**
</eightball:1123638694675497021> {arrow2} **Helps You decide things**
</wordle:1124004881297063986> {arrow2} **Guess a 5-letter word from hints**
</wordlist:1124004881297063987> {arrow2} **Shows the wordlist used for wordle**
        
Do `~help (command)` or </help:1121845078957236375> to learn more!
        """
        second = f"""
</highlow:1123274277681102949> {arrow2} **Starts highlow. Guess the number with hints**
</weather:1123994768599425124> {arrow2} **Fetches the weather of a location**
</imagine:1118187943002120253> {arrow2} **This Command tells you how cool You are!**
</serverinfo:1123990073805905990> {arrow2} **Shows the informations in that server**
</userinfo:1123990073805905991> {arrow2} **Shows the informations of the mentioned user**
</choose:1123638694675497022> {arrow2} **Helps you choose from upto 10 options**
</imagine:1118187943002120253> {arrow2} **Generates images with prompts**
</role:1123817226110251011> {arrow2} **Assigns or Unassigns a role to user**
</brainfuck:1123993283119566870> {arrow2} **Generates Brainfuck codes**
</ask:1123985735633096788> {arrow2} **Allows you to use ChatGPT in discord**
</render:1125432030063243394> {arrow2} **Renders math equations using latex**

Do `~help (command)` or </help:1121845078957236375> to learn more!
        """
      
        embed1=discord.Embed(title="Command List", description=first, color=0x631cba)
        embed1.set_thumbnail(url=pfp)
        embed1.set_footer(text='Made by @soul_.void   page 1/2',icon_url='https://imgur.com/kQBoNeE')

        embed2=discord.Embed(title="Command List", description=second, color=0x631cba)
        embed2.set_thumbnail(url=pfp)
        embed2.set_footer(text='Made by @soul_.void   page 2/2',icon_url='https://imgur.com/kQBoNeE') 
        
        await ctx.respond(embed=embed1,view=pageView(embed1,embed2,ephemeral),ephemeral=ephemeral)

      case 'time':
        
        TIME = int(t.time())
        TimE = TIME + 300
        Time450 = TIME + 6600
        Time40 = TIME - 2400

        timeDesc = f"""
# Time
This Command will generate a discord timestamp.
> * Timestamps looks like this: <t:{TIME}:R>
> * You can set a timer too like this: <t:{TimE}:R>

## Structure
```css
~time <ago/in> [int](time)
```
**s {arrow} 1 sec**
**m {arrow} 1 min**
**h {arrow} 1 hour**
**d {arrow} 1 day**
**etc.**

## For /Slash:
Use </time:1116611178827886613> to use it
> * **Tense: 1** {arrow2} uses Present time
> * **Tense: 2** {arrow2} adds time to the current time (like in)
> * **Tense: 3** {arrow2} decreases time from the current time (like ago)

## Example: 
> * `~time in 4h 50m` {arrow2} <t:{Time450}:R>
> * `~time`           {arrow2} <t:{TIME}:R>
> * `~time ago 40m`   {arrow2} <t:{Time40}:R>
      """
      
        embed=discord.Embed(title="", description=f"{timeDesc}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case 'purge':
        
        
        
        purgeDesc = """
# Purge
This command is used for deleting multiple messages at once.
Spam messages, Command test messages could be easily purged with it.

## Structure:
```css
~purge [int]
```
### ⚠️Requirement: Moderator or Admin⚠️

## Example:
```py
~purge 40
```
      """

        embed=discord.Embed(title="", description=f"{purgeDesc}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case 'mute':
        
        muteDesc = """
# Mute
This will allow you to punish members by granting them the disablity to send messages
You can mute people who violates Your rules.

* You can set an **\`unmute timer\`** or unmute using `~unmute`

## Structure:
```cpp
~mute {'@mention'} [int](time) {'Reason'}
```
**⚠️Requirement: `Moderator` or `Admin`⚠️**

## Example:

```css
~mute @SOUL 4h
```
```css
~mute @Tashka 3m 'Spamming messages'
```

Do `~help time` to learn more about **\`timers\`**.

      """

        embed=discord.Embed(title="", description=f"{muteDesc}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case 'unmute':
        
        unmuteDesc = """
# Unmute
This will allow you to **\`unmute users\`**

## Structure:
```css
~unmute {@mention}
```

**⚠️Requirement: \`Moderator\` or \`Admin\`⚠️**

## Example:
```css
~unmute @SOUL
```
      """
        embed=discord.Embed(title="", description=f"{unmuteDesc}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)
      
      case 'nuke':
        
        nukeDesc = """
# Nuke
This is a Powerful command. This command is capable of completely wiping an entire channel. Only use this when its actually needed.

## Structure:
```cpp
~nuke {'channel_name'}
```

**⚠️Requirement: \`Moderator\` or \`Admin\`⚠️**

## Example:
```cpp
~nuke #general
```
## How it works:
This command will delete the targeted channel and clone it. Clone channel is a discord feature. The name, channel Perms and channel position will stay the same. This is usefull when You want to restart a channel but that channel has too many messages.
      """

        embed=discord.Embed(title="", description=f"{nukeDesc}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)
      case 'font':
        
              
        fontDesc = """
# Font
This is command is used for changing **\`message font.\`**

## Structure:
```cpp
~font ['fontName'] '[message']
```

## Example:
```css
~font bold Hello Everyone
```
```
𝐇𝐞𝐥𝐥𝐨 𝚬𝐯𝐞𝐫𝐲𝐨𝐧𝐞
```

**Fonts:**
**Bold**      `-` 𝐓𝐡𝐢𝐬 𝐢𝐬 𝚩𝐨𝐥𝐝
**Cursive**   `-` 𝓣𝓱𝓲𝓼 𝓲𝓼 𝓒𝓾𝓻𝓼𝓲𝓿𝓮
**Hollow**    `-` 𝕋𝕙𝕚𝕤 𝕚𝕤 ℍ𝕠𝕝𝕝𝕠𝕨
**Tiny1**     `-`  ᴛʜɪs ɪs ᴛɪɴʏ
**Tiny2**     `-` ᵀʰᶦˢ ᶦˢ ᵗᶦⁿʸ
**All**       `-` **\`Converts to all fonts\`**

## Aliases (Not case-sensitve) : 

```py
Bold = ['normal1', 'bold', 'n1']
cursiveLetter = ['cursive', 'curs', 'c1']
Hollow = ['premium', 'prem','hollow', 'n2']
Tiny1 = ['tiny1', 't1', 'small1', 's1']
Tiny2 = ['tiny2', 't2', 'small2', 's2']
```
      """
      
        embed=discord.Embed(title="", description=f"{fontDesc}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)
      case 'bmr':
        
        bmrDesc = f"""
# BMR
This command will calculate Your **\`BMR (basal metabolic rate)\`**

## For men:
BMR {arrow} `13.397W + 4.799H - 5.677A + 88.362`
## For women:
BMR {arrow} `9.247W + 3.098H - 4.330A + 447.593`

> * **W** {arrow} **body weight in kg**
> * **H** {arrow} **body height in cm**
> * **A** {arrow} **age**

## Example:
Type `~bmr` to start the command. The bot will ask you a few questions. You just need to answer them.
      """
      
        embed=discord.Embed(title='',description=f'{bmrDesc}', color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case 'wordle':
        Green=greenEmoji['G']
        Yellow=yellowEmoji['Y']
        Gray=grayEmoji['E']
        wordle = ''
        conv = 'WORDLE'
        wordle += greenEmoji[conv[0]]
        wordle += yellowEmoji[conv[1]]
        wordle += grayEmoji[conv[2]]
        wordle += greenEmoji[conv[3]]
        wordle += yellowEmoji[conv[4]]
        wordle += grayEmoji[conv[5]]
  
        wordleDesc = f"""
# {wordle}

Wordle is a Game where your goal is to guess a **\`5-letter word\`** You have **\`6 tries\`** to guess the word. The game will try to provide enough **\`hints\`**.

## Hints:
> * {Green} **Guess a word with this letter at the same position.**
> * {Yellow} **Guess a word that has this letter in a different position.**
> * {Gray} **Guess a word that doesnt have this letter.**

## Example:
Type `~wordle` to start the game. Try to guess a **\`5-letter word\`**. If you dont guess it correctly use the hints to guess the word again. You have **\`6 tries\`** in total
      """
        
        embed=discord.Embed(title='', description=f'{wordleDesc}', color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case 'brainfuck':
        
        
        codes= """
```cpp
"brainfuck"  C equivalent
(start)      char array[30000]={0}; char *ptr=array;
">"          ++ptr;
"<"          --ptr;
"+"          ++*ptr;
"-"          --*ptr;
"."          putchar(*ptr);
","          *ptr = getchar();
"["          while (*ptr) {
"]"          }
```
    """
        main=f"""
      
# Brainfuck

__**Brainfuck**__ is an esoteric programming language created in __1993__ by **Urban Müller**.

Notable for its extreme minimalism, the language consists of only eight simple commands, a data pointer and an instruction pointer. While it is fully Turing complete, it is not intended for practical use, but to challenge and amuse programmers. Brainfuck requires one to break commands into microscopic steps

{codes}

**This command allows you to turn normal messages into brainfuck commands**.

## Structure:

`~bf <Message>`
**Example:**

`~bf Hello World`
```bf
[-]>[-]<+++++++[>++++++++++<-]>++.<++[>++++++++++<-]>+++++++++.<[>++++++++++<-]>+++++++.<[>----------<-]>.<[>++++++++++<-]>+++.<+++++++[>----------<-]>---------.<+++++[>++++++++++<-]>+++++.<++[>++++++++++<-]>++++.<[>++++++++++<-]>+++.<[>----------<-]>------.<[>----------<-]>--------.<
//Hello World
```   
      """

        embed=discord.Embed(title="",description=f"{main}", color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case "gpt":
        
        main = """
# Chat GPT
The **\`ask\`** command, with the alias **\`gpt\`**, allows users to utilize the OpenAI API to generate responses to their prompts.

## Specifications:
```py
completion= openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = [
          {'role':'user','content':prompt}
        ],
        temperature = 0.4,
        max_tokens = 7
      )
```

## Structure:
```cpp
~ask ['prompt']
```
In this command, the user would replace **\`[prompt]\`** with their own statement or question for the AI to generate a response.

## Example:
```
~ask What is the meaning of life?
```
## Response:
`The meaning of life is subjective and varies from person to person, but could involve finding happiness, contributing to society, and fulfilling personal goals.`

## Credit:
Thanks **\`𝓓𝓐𝓜𝓝#0401\`** for providing the **\`OpenAI API key\`** for this command.
This description was generated by **ChatGPT**.
"""
        embed=discord.Embed(title="",description=f"{main}",color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case 'weather':
        
      
        weatherDesc = """
# Weather
Get the current weather information for a specified location. The command takes a single argument, which is the location you want to get the weather for. It retrieves data from a weather API using aiohttp to make the request.

**Command Structure:**
```cpp
~weather <'location'>
```
**Example Usage:**
**For Slash**
```
/weather city:<"location">
```
```
~weather New York
```
**Output:**

**Weather for New York
The Condition in `New York` is `Clear`

**Tempreture**         **Humidity**    **Wind Speed**
`7.2°C | 45.0°F`     `31 `               `3.6kmp/h | 2.2mp/h`



Please note that the output may vary depending on the data retrieved from the weather API and how it is formatted in your implementation.
      """
        embed=discord.Embed(title="",description=f'{weatherDesc}',color=0x631cba)
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case "serverinfo":
        Desc = """
# Serverinfo
This command will get you the information of the server you are in currently. It will fetch the ID, owner, creation date, members, bots, channels and roles, server icon etc.

## Command Structure:

```
~serverinfo
```
**For Slash**
```
/serverinfo
```

      """
        embed = discord.Embed(title='',description=Desc,color=0x631cba)
        await ctx.respond(embed=embed,ephemeral=ephemeral)

      case "userinfo":
        Desc = """
# Userinfo
This command command will get you the information of a user. It can fetch their ID, username, top role, server join date, account creation date, status, pfp etc.
## Command Structure:

```css
~userinfo <@mention>
```
**For Slash**
```
/usererinfo user:<@mention>
```
        """
        embed = discord.Embed(title='',description=Desc,color=0x631cba)
        await ctx.respond(embed=embed,ephemeral=ephemeral)
      case "render":
        Desc = """
# Render
This command will generate **math equations** or **chemical reactions** using **LaTeX** code as the prompt. This command could be useful to write **math/chemical reactions** while discussing about them. Writing math in discord is kinda hard to understand. Theres no prefixed version of this command. Only slash.

## Command Structure:
```cpp
/render prompt:<"latex_code">
```

## What is Latex code?
**LaTeX** is a form of code which specializes in document typesetting. Basically it's used for formatting text. Mostly maths.

## Latex - basic code:
### * Exponent:
> * `ax^2 + bx + c = 0`
> * `x^{n+4} * y^2 = 56`
### * Subscript
> * `x_1`
> * `C_nH_{2n+1}`
### * Special actions 
> * **Division** - `\\frac{x}{y} + \\frac{x^{4}}{y+5}`
> * **Summation** - `\\sum_{n=0}^{\infty}\\frac{1}{n^2}`
> * **Integral** - `\int_0^2x^2dx`
> * Limits - `lim_{x\\to\infty} f(x)`
### * Special letters
> * **Greek letters** - `\\pi` , `\\theta`, `\\alpha`, `\\beta`, `\gamma`, `\\omega`, `\\circ` etc
> * **Infinite** - `\\infty`
> * **Symbols** - `\\equiv`, `\\rightarrow`, `\\rightarrow`, `\\uparrow`, `\\downarrow`, `\\dot`
### * Brackets
> * **angles** 	`\\langle`, `\\rangle`
> * **normal** `(\\` , `)\\` , `{\\` , `}\\` etc. (basically put `\\` after the bracket)

## Why are there dollar signs?
Latex code needs `$` at the start and end to make the code. the code actually looks like `$(code)$`
when your using brackets there is a `\\` at the end. In python, this symbol basically reveals hidden stuffs much like in discord.

[Learn more from here](http://www.malinc.se/math/latex/basiccodeen.php)
        """
        embed = discord.Embed(title='',description=Desc,color=0x631cba)
        await ctx.respond(embed=embed,ephemeral=ephemeral)
        
      case _:
        embed = discord.Embed(description="## Invalid Commands name\n> ### Why is this happening?\n> * You probably made a typo\n> * The command might not exist\n>  * If you want that command to be made contact @soul.is.cool\n> * Do </help:1121845078957236375> to see all the commands",color=0xFF0000)
        embed.set_thumbnail(url=pfp)
          
        await ctx.respond(embed=embed,ephemeral=ephemeral)
                      

def setup(bot):
	bot.add_cog(help(bot))