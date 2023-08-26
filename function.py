import random
import math
import sys
def time_conv(add):
  time_convert = {"s":1, "S":10, "m":60, "M":600, "h":3600, "H":36000, "d":86400, "D":864000, "w":604800, "W":6048000, "mo":2419200, "MO":24192000, "y":31536000, "Y":315360000, "i":2177445321}

  if len(add) == 2: 
    add_time= int(add[0]) * time_convert[add[len(add) -1]]
    return add_time
  elif len(add) == 3:
    add_time = int(add[0]) * 10 + int(add[1])
    conv = time_convert[add[len(add) -1]]
    add_time *= conv
    return add_time

def BMR(gender, age, weight,height):
  if gender == 'male':
    age *=6.8
    height *= 5
    weight *= 13.7
    final = 66 + weight + height - age
    return int(final)
    
  elif gender == 'female':
    age *= 4.7
    height *= 1.8
    weight *=9.6
    final = 655 + weight + height - age
    return int(final)

def wordpick(): 
    with open("words.txt") as f: 
        words = f.read().splitlines() 
        return random.choice(words)

Eightball = [
	'It is certain.',
	'It is decidedly so.',
	'Without a doubt.',
	'Yes definitely.',
	'You may rely on it.',
	'As I see it, yes.',
	'Most likely.',
	'Outlook good.',
	'Yes.',
	'Signs point to yes.',
	'Reply hazy try again.',
	'Ask again later.',
	'Better not tell you now.',
	'Cannot predict now.',
	'Concentrate and ask again.',
	'Don\'t count on it.',
	'My reply is no.',
	'My sources say no.',
	'Outlook not so good.',
	'Very doubtful.',
	'No way.',
	'Maybe',
	'The answer is hiding inside you',
	'No.',
	'Depends on the mood of the CS god',
	'Hang on',
	'It\'s over',
	'It\'s just the beginning',
	'Good Luck',
]

def convert_mention_to_id(mention):
    return int(mention[1:][:len(mention)-2].replace("@","").replace("!",""))


def time_shorter(add):
  year = math.floor(add / 31536000 )
  month = int(math.floor(add-year*31536000)/2628000)
  week = int(math.floor(add-year*31536000- 
  month*2628000)/604800)
  day = int(math.floor(add-year*31536000-month*2628000- 
week*604800)/86400)
  hour = int(math.floor(add-year*31536000-month*2628000-week*604800-day*86400)/3600)
  min = int(math.floor(add-year*31536000-month*2628000- week*604800-day*86400-hour*3600)/60)
  second = int(math.floor(add-year*31536000-month*2628000-week*604800-day*86400-hour*3600-min*60))
  final = f"{str(year)+'y ' if year!=0 else ''}{str(month)+'mo ' if month !=0 else ''}{str(week)+'w ' if week!=0 else ''}{str(day)+'d ' if day!=0 else ''}{str(hour)+'h ' if hour!=0 else''}{str(min)+'m 'if min!=0 else''}{str(second)+'s' if second!=0 else ''}"
  return final

def ab(add):
  Billion = 1000000000
  Million = 1000000
  Killo = 1000
  billion = math.floor(add / Billion )
  million = int(math.floor(add-billion*Billion)/Million)
  killo = int(math.floor(add-billion*Billion-million*Million)/Killo)
  flat = int(math.floor(add-billion*Billion-million*Million-killo*Killo))
  return f"{str(billion)+'B ' if billion!=0 else ''}{str(million)+'M ' if million !=0 else ''}{str(killo)+'k ' if killo!=0 else ''}{str(flat) if flat!=0 else ''}"
  




def char_to_bf(char):
  
  buffer = "[-]>[-]<"
  for i in range(ord(char)//10):
      buffer = buffer + "+"
  buffer = buffer + "[>++++++++++<-]>"
  for i in range(ord(char) % 10):
      buffer = buffer + "+"
  buffer = buffer + ".<"
  return buffer


def delta_to_bf(delta):
    buffer = ""
    for i in range(abs(delta) // 10):
        buffer = buffer + "+"

    if delta > 0:
        buffer = buffer + "[>++++++++++<-]>"
    else:
        buffer = buffer + "[>----------<-]>"

    for i in range(abs(delta) % 10):
        if delta > 0:
            buffer = buffer + "+"
        else:
            buffer = buffer + "-"
    buffer = buffer + ".<"
    return buffer


def string_to_bf(string, commented):
    buffer = ""
    if string is None:
        return buffer
    for i, char in enumerate(string):
        if i == 0:
            buffer = buffer + char_to_bf(char)
        else:
            delta = ord(string[i]) - ord(string[i - 1])
            buffer = buffer + delta_to_bf(delta)
        if commented:
            buffer = buffer + ' ' + string[i].strip('+-<>[],.') + '\n'
    return buffer


def conv(add):

  total = 0
  for i in add:
    total += time_conv(i)

  return total

def count_lines(s):
  lines = s.splitlines()
  return len(lines)