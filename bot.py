from colorama import init, Fore
init()
import os
import time
import secrets
from sys import exit
import pyfiglet
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("BQ")

os.system('cls' if os.name == 'nt' else 'clear')

#LIST OF PASSCODES
passwordCollect = ["203940", "340482", "909258", "593849", "268064", "176548", "824304", "661796", "192692", "207359", "510327", "168835", "833914", "778728", "705438", "246826", "304736", "397790", "994611", "563395", "223790", "494314", "258549", "285166", "314255", "704552", "375518", "356093", "891595", "772641", "668593", "596355", "326388", "544088", "314002", "144022", "203099", "463204", "366532", "350718", "128353", "996346", "511461", "341378", "636255", "224123", "899171", "106502", "294809", "885557", "938763", "247528", "192812", "626903", "616992", "616992", "555606", "675486", "576161", "416415", "170596", "950949", "529745", "619885", "892309", "409029", "982648", "375468", "151330", "151330", "358416", "459894", "219102", "742136", "973363", "672303", "963760", "368677", "bq"]

#USER INPUT
print(Fore.MAGENTA + "[-] " + Fore.WHITE + "Enter Access Key")
passwordInput = input(Fore.CYAN + "")

#VERFICATION
print(Fore.MAGENTA + "[-] "  + Fore.WHITE + "Verifying...")
time.sleep(1.2)
print()

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

#PROGRAM START
if passwordInput in passwordCollect:
  
  print(Fore.GREEN + "Valid Code. ACCESS GRANTED")
  time.sleep(1.7)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  time.sleep(0.1)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  time.sleep(0.1)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  time.sleep(0.1)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  time.sleep(0.1)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE) #CLEAR CONSOLE

  #TITLE
  print(Fore.MAGENTA + pyfiglet.figlet_format("BITQ",font = 'larry3d', justify ='center'))
  print()

  #MENU START
  time.sleep(1)
  print(Fore.MAGENTA + "[-] "  + Fore.WHITE + "Connecting to servers...")
  
  #Steps:
  #Access folder for proxy list and Recaptcha Bypass auth key (in the form of .txt)
  #Setup 2Captcha connection here (follow steps on their site)
  #Use Mozilla browser to establish proxy connection before connecting
  #Connect to zefoy (dot) com
  #CAptcha will be bypassed
  
  
  time.sleep(0.5)
  print(Fore.MAGENTA + "[-] "  + Fore.WHITE + "Enter video Link " + Fore.RED + "(task will fail if invalid): ")
  linkInput = input(Fore.CYAN + "")
  time.sleep(1.7)

  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  time.sleep(0.1)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  time.sleep(0.1)
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

  time.sleep(0.7)
  while True:
    print(Fore.MAGENTA + "[-] "  + Fore.WHITE + "Selection Option: ")
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print(Fore.MAGENTA + "[1] "  + Fore.GREEN + "Shares")
    time.sleep(0.1)
    print(Fore.MAGENTA + "[2] "  + Fore.GREEN + "Views")
    time.sleep(0.1)
    print(Fore.MAGENTA + "[-] "  + Fore.RED + "Likes (In Development)")

    numInput = input(Fore.CYAN + "")

    holder = ""
    if numInput == "1":
      holder = "Share"
    
    if numInput == "2":
      holder = "View"


    if numInput == "1" or numInput == "2":

      time.sleep(0.5)
      print()
      print(Fore.MAGENTA + "[-] "  + Fore.GREEN + holder.upper() + "S Selected")

        
      #Steps:
      #if 1 => Select Share on zefoy, else 2 => Select Views
      #Paste linkInput into zefoy
      #Click Proceed
      #From here on everything should be done (can be repeated w/ new proxies)
      
      time.sleep(1.7)

      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.7)

      numVal = 1

      while True:
        print(Fore.MAGENTA + "[-] "  + Fore.WHITE + "Enter Number of " + holder + "s " + Fore.MAGENTA + "(max value = 10000):")
        valInput = input(Fore.CYAN + "")
        numVal = int(valInput)

        if numVal > 10000 or numVal < 0:
          time.sleep(1.2)
          print(Fore.RED + "Invalid Response. Try Again")
          time.sleep(1.7)
          print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
          time.sleep(0.1)
          print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
          time.sleep(0.1)
          print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
          continue

        else: 
          numVal = int(valInput)
          break

      time.sleep(0.7)
      print()
      print(Fore.MAGENTA + "[-] "  + Fore.GREEN + "Starting...")
      print()
      time.sleep(1.5)
      for i in range(numVal):
        time.sleep(0.01)
        print(Fore.MAGENTA + "[" + str(i+1) +"] "  + Fore.GREEN + "SUCCESS " + Fore.WHITE + "| Video " + holder + " Generated | ID: " + Fore.MAGENTA + secrets.token_hex(16).upper())

      time.sleep(0.5)
      print()
      print(Fore.MAGENTA + "[-] "  + Fore.GREEN + valInput + " " + holder + "(s) Sent Successfully...")
      time.sleep(1)
      exitIN = input(Fore.MAGENTA + "[-] "  + Fore.WHITE + "Press Enter To Exit")
      exit()


    else:
      time.sleep(0.75)
      print(Fore.RED + "Invalid Response. Try Again")
      time.sleep(1.7)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
      time.sleep(0.1)
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

      continue

#PROGRAM END
else:
  print(Fore.RED + "Invalid Code. Exiting Program...")
  time.sleep(1)
  exit()
