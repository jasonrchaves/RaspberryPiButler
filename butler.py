import os
import subprocess
import xml.parsers.expat
import sys
import datetime

dict = {}
#do not use '1', it's reserved, along with some other numbers in main() below
## Define dict before main() is run
## The string will be the terminal command run
dict['0'] = "./speech.sh Welcome to my apartment. My name is Timmy, the robot butler for the apartment. ; ./speech.sh Please make yourself comfortable."
dict['666'] = "./speech.sh Quitting application, goodbye."
dict['7'] = "./speech.sh Let's play Madden. Now!"
dict['2'] = "./speech.sh Let me help you"
dict['9'] = "./speech.sh And ; ./speech.sh dramatic pause"
dict['5'] = "./speech.sh That was easy!"
dict['1111'] = "sudo ntpdate 69.25.96.13"
dict['159'] = "./speech.sh Test 1"

dict['forcast'] = "wget http://api.wunderground.com/api/5a23a6c2c3d1a8cb/forecast/q/"


days = 0
cutoff = 2
add_to_read = False
to_read = []

def start_element(name, attrs):
  if name == 'forecastday':
    temp = days
    global days
    days += 1

  if days > cutoff :
    global add_to_read
    add_to_read = False
  elif name == 'title' or name == 'fcttext':
    global add_to_read
    add_to_read = True
  else:
    global add_to_read
    add_to_read = False
def end_element(name):
  pass
def char_data(data):
  if add_to_read and data != '' and data != '\n' and data != '\t\t' :
    to_read.append(data) 


def Weather(zip_code):
  ## Accesses Weather Underground API to get XML file of forecast
  ## Reads just the day's forecast

  os.system('./speech.sh Weather')
  global days, cutoff, add_to_read, to_read
  days = 0
  cutoff = 2
  add_to_read = False
  to_read = []
  p = xml.parsers.expat.ParserCreate()
  p.StartElementHandler = start_element
  p.EndElementHandler = end_element
  p.CharacterDataHandler = char_data

  filename = zip_code + ".xml"
  os.system(dict['forcast'] + filename + ' -O ' + filename)

  f = open(filename)
  p.ParseFile(f)
  global was_read
  was_read = to_read
  for line in to_read:
    print line
    if len(line) < 100 :
      os.system('./speech.sh ' + line)
    else:
      for part in line.split('.'):
        if len(part) < 100 :
          os.system('./speech.sh ' + part)
        else:
          for lil_part in part.split(','):
            os.system('./speech.sh ' + lil_part)


def JasonCalendar():
  ## Uses gcalcli to access Google Calendar
  ## Reads my schedule for the day
  t = datetime.date.today()
  p = os.popen("gcalcli --user <username> --pw <password> --cal <calendar name> --nc agenda " + str(t.year) +'-'+ str(t.month) +'-'+ str(t.day) +'T00:00-08:00 ' + str(t.year) +'-'+ str(t.month) +'-'+ str(t.day + 1) + 'T00:00-08:00')
  l = p.readlines()
  for line in l:
    if line != '\n' :
      os.system('./speech.sh ' + line)

def PlayPandora():
  if pandora_on == False :
    os.system('./speech.sh Playing Pandora')
    global p
    p = subprocess.Popen('pianobar', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ## Uses pianobar application, http://6xq.net/projects/pianobar/
    p.stdin.write('13\n')  ## Chooses default station on my pandora account
    global pandora_on
    pandora_on = True  ## Avoids accidentally starting two pianobar processes or accidentally killing the current one


def KillPandora():
  p.kill()
  global pandora_on
  pandora_on = False

def TalkToPandora(entry):
  ## Translates my numberpad entries to keyboard entries for pianobar controls
  if entry == '1':
    p.stdin.write('+\n')  ## Increase Volume by 1 increment
  elif entry == '0':
    p.stdin.write('-\n')  ## Decrease Volume by 1 increment
  elif entry == '2':
    p.stdin.write('n\n')  ## Skip song
  elif entry == '3':
    p.stdin.write('p\n')  ## Pause/Play
  elif entry.startswith('-'):  ## Enter "-----" to decrease volume by 5 increments
    for i in xrange(entry.count('-')):
      p.stdin.write('(\n')
  elif entry.startswith('+'):
    for i in xrange(entry.count('+')):
      p.stdin.write(')\n')
  elif entry == '654':
    KillPandora()


if __name__ == '__main__':
  bool_cont = True
  global pandora_on
  pandora_on = False
  
  while bool_cont :
    entry = raw_input('Enter numeric command: ')
    #must type number and then click enter
  
    if pandora_on == True:
      TalkToPandora(entry)
      #KillPandora()
    elif entry == '1':
      Weather('94309')
    elif entry == '1027':
      JasonCalendar()
    elif entry == '33':
      Weather('94309')
      JasonCalendar()
    elif entry == '456':
      PlayPandora()
    elif entry == '654':
      KillPandora()
    elif entry == '999':
      ## Exit butler.py, returning to parent application UpdateButler.py
      ## Grab new version of butler.py from website and re-start butler.py
      os.system('./speech.sh Teach me how to butler.  Updating script')
      sys.exit(0)
    elif entry in dict.keys():
      os.system(dict[entry])
      ## Exit butler.py and also exit UpdateButler.py
      ## Stopping the application completely
      if entry == '666':
        sys.exit(1)
    elif len(entry) == 5:
      Weather(entry) #meant to be a zip code string
   
