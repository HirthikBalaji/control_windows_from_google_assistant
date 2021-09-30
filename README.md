# control_windows_from_google_assistant

this is a code to control your computer running Windows 10 or later:

just you need to setup IFTTT free account

Create a new applet, in """if this add """ option select google assistant and select """Say a phrase with a text ingredient""" option

just fill up the first one like:
                                Ask my windows to $ 
                                here "$" refers to the main query
and fill up the response of your wish that google should reply to your command

and in """then""" select Dropbox [NOTE] YOU HAVE TO INSTALL DROPBOX CLIENT ON YOUR COMPUTER FREE ACCOUNT RECOMMENTED

and in file name fill with "Command.txt" *without quotes

and in content fill with "{{TextField}}<br>" *without quotes

and in location fill with "Apps/WindowsAssistant" *without quotes

and create the tigger

afterward install dropbox client on your machine and login with your ifttt account

and run the # pip install -r reqirements.txt # in cloned repo in command prompt
then run the main.py 
your google assistant will now ask your pc to do some basic works

# have fun!!
