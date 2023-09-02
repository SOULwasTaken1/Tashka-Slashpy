# About this project
This project uses [Pycord](https://pycord.dev). Pycord is a modern, easy to use, feature-rich, and async ready API wrapper for Discord. 
This project uses cogs and it is designed to be runned in replit.
## About this project - APIs
- [WeatherAPI](https://www.weatherapi.com/docs/)
- [OpenAI](https://www.openai.com/)
- [Craiyon.com](https://Craiyon.com)
- [Pycord](https://docs.pycord.dev/en/stable/)

# Usage / Steps to a running the bot
- Add your bot token to `BOT_TOKEN` in secrets
- Add your openai key to `OPENAI_KEY` from [here](https://www.openai.com/) in secrets if you want to use chatGPT in discord. If you dont want it you can delete the file `cogs/gpt.py` (You dont need to delete it)
- Add your Weather API key to `WEATHER_KEY` from [here](https://www.weatherapi.com/docs/) in secrets if you want to use WeatherAPI in discord. If you dont want it you can delete the file `cogs/weather.py` (You dont need to delete it)
- Change `/Help` command in `cogs/help.py`
- `/dank` command is rigged. You can remove the IDs i have added or change it.
- The files `Lbalance` and `Lfund` are there for the commands in `cogs/fund.py`. You may delete the json filesif you want.   
- You might need to change a lot of things in `Emojies.py` if the emojies dont load for you. but if they do then dont change them.

# Commands
This project obviously uses `/slash` commands. Few of the commands are listed below
## BMR:
* This command is used to calculate the BMR of a user. It uses `wait_for()` function to get the information it needs.
* It uses some functions from `function.py`
   
## Wordle: 
* Wordle is a word guessing game. You can play it [here](https://www.nytimes.com/games/wordle/index.html) too.
* THe goal of the game is to guess a 5-letter word which will be randomly generated from `words.txt` File.
* Using if conditions, It will check if the n-th index was in the word or not. If not, that letter will be gray and if yes then the letter will be yellow. If the n-th index matches with the n-th index of the secret word, then that letter will be green
* it will import some converters from `Emojies.py` and then use it in the for loops to change the letters to discord emotes.
* This command also uses the `wait_for()` function.
* Get the emotes from [This repo](https://github.com/SOULwasTaken1/Discord-Wordle-bot) if your bot cant use the ones i have provided. You will need to get the Emote IDs and then put them in `Emojies.py`
  
## Weather:
* You need the API key for this to work.
* This uses aiohttp to make API call.
* You may add more data if you want. Check the [docs](https://www.weatherapi.com/docs/#intro-aqi) to learn more

## ChatGPT:
* You need the API key for this to work.
* This uses the `openai` library.
* This usually takes a lot of time to respond to the user.

## Image:
* This uses `aiohttp` to make requests to [Craiyon.com](https://Craiyon.com)
* This command gets a lot of images so i used Buttons to view more in discord.
* THe quality is usually not that good so dont expect too much from this command

## Render:
* This command uses Latex and matplotlib 
* LaTeX is a form of “program code”, but one which specializes in document typesetting;
* I used it with `matplotlib` to render math syntaxes as image.
* Discord doesnt let you type math syntaxes correctly and usually looks ugly.
* use `/help command:render` to learn some basics of latex.  
* Learn more about latex [here](http://www.malinc.se/math/latex/basiccodeen.php)

## Time:
* This command is used for generating discord timestamps.
* The syntaxes for timestamps in discord looks like `<t:UNIX_CODE_HERE:R>`
* learn more about timestamps [here](https://gist.github.com/LeviSnoot/d9147767abeef2f770e9ddcd91eb85aa)
* This command makes it easier to generate timestamp codes.
 

# Additional info
Learn Pycord at [https://guide.pycord.dev](https://guide.pycord.dev).

Use [pycord docs](https://docs.pycord.dev) if necessary. 

Use [UptimeRobot](https://uptimerobot.com) to keep it get a uptime dashboard and keep the project online.

# 🔗 Links
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/soulvoid)
![](https://dcbadge.vercel.app/api/shield/971753818389905418?bot=true)

