This is a project that uses the Raspberry Pi, a numberpad, a speaker,
and an internet connection to create a sort of "Butler".

Features include:
Speaking the Weather forecast for the day (default or entered zip code)
Speaking my day's schedule from my Google Calendar
Speaking random lines like "That was easy!" and "Welcome to my apartment"
Playing Pandora radio with basic controls

The UpdateButler.py script is run on the Raspberry Pi and will create 
a child process to run butler.py.

Pianobar and gcalcli are installed on the Pi.
The speech.sh script was obtained from http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

This was something I built just for fun, and to put my Raspberry Pi to use.
A video of it working all together is included.
This application was also made in a very hacky fashion, so please excuse me 
if the code reflects that fact.

I really enjoyed having this read me my schedule and the weather in the morning
when I was getting ready to leave the apartment.  It was also fun to have it as 
a Pandora radio player in the living room and to have it greet guests.
