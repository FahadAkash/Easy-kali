# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
import os
from colorama import *
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
gpe =yellow + """



                                                 __----~~~~~~~~~~~------___
                                      .  .   ~~//====......          __--~ ~~
                      -.            \_|//     |||\\  ~~~~~~::::... /~
                   ___-==_       _-~o~  \/    |||  \\            _/~~-
           __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
       _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
     .~       .~       |   \\ -_    /  /-   /   ||      \   / 
    /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
    |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
             '         ~-|      /|    |-~\~~       __--~~
                         |-~~-_/ |    |   ~\_   _-~            /\
                              /  \     \__   \/~                \__
                          _--~ _/ | .-~~____--~-/                  ~~==.
                         ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                    -_     ~\      ~~---l__i__i__i--~~_/
                                    _-~-__   ~)  \--______________--~~
                                  //.-~~~-~_--~- |-------~~~~~~~~
                                         //.-~~~--\
_________________________________________________________________________
|                       Easy Kali                                        |
|			      Made By Fahad Akash					                 |
|Installations:															 |
|#First you need to install kali linux App form window's  app store      |
|#when setup all complete then Clone The Easy Kali Script And			 |
|	Enjoy Kali linux (GUI)												 |
|________________________________________________________________________|


"""
print gpe 
gs = green + """
    {01} >>Install Kali GUI
    {02} >> Configaration
    {03} >> Start GUI
    {04} >> Stop GUI
    {05} >> Exit
 """
ps = green +""" 
              {99} Go to home
              {00} Exit
 """
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
	
print gs
gp = raw_input(blue +"Ekali==>>")
if gp == "1":
	os.system('sudo apt-get install figlet')
	os.system('sudo figlet -f mini °°°°°°Kali GUI°°°°°')
 	os.system('sudo apt-get install update')
 	os.system('sudo apt-get install wget -y ')
 	os.system('sudo apt-get dist-upgrade -y --force-yes')
 	os.system('sudo apt-get --yes --force-yes install')
 	os.system("sudo sed -i 's/port=3389/port=3390/g' /etc/xrdp/xrdp.ini")
 	print green + "#########Complete##########"
 	timeout(2)
 	os.system('clear')
 	restart_program()
 	

	gp = raw_input(green + "Ekali==>>")
elif gp == "2":
    os.system('sudo figlet -f mini Configaration')
    os.system('sudo /etc/init.d/xrdp start')
    os.system('sudo cat /etc/issue')
    print "######Done##########"
    print "Start GUI(Now)"
    timeout(2)
    os.system('clear')
    restart_program()
   
elif gp =="3":
	os.system('clear')
	print (blue + "#######Starting The Service####")
	timeout(3)
	os.system('sudo service xrdp start')
	print "########Done######"
	timeout(2)
	os.system('clear')
	restart_program()
elif gp == "4":
	os.system('clear')
	print "#######Stoping The Service#####"
	os.system('clear')
	os.system('sudo service xrdp stop')
	timeout(4)
	os.system('clear')
	restart_program()
elif gp == "5":
	print ".........Bye Bye (-_-)............."
	sys.exit()
	
	
	print "########Done######"
	restart_program()
else:
	print "Wrong Input"
	restart_program()
		
   

		
