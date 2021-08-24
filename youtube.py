# Youtube view Increaser Created by AlPHA
# This script is for education purposes only and you can get ip banned from
# This if you do it a lot Make sure you have Selenium and webdriver installed.
# I'M NOT RESPONSIBLE FOR ANYTHING THAT YOU DO WITH THIS SCRIPT 
# Enjoy AlPHA


print("""\n\n\n
 __     __         _         _           __      ___               
 \ \   / /        | |       | |          \ \    / (_)              
  \ \_/ /__  _   _| |_ _   _| |__   ___   \ \  / / _  _____      __
   \   / _ \| | | | __| | | | '_ \ / _ \   \ \/ / | |/ _ \ \ /\ / /
    | | (_) | |_| | |_| |_| | |_) |  __/    \  /  | |  __/\ V  V / 
    |_|\___/ \__,_|\__|\__,_|_.__/ \___|     \/   |_|\___| \_/\_/  
                                                                   
                                                                   
\n\n\n""")

# Importing Modules

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.1)

print_slow("Importing The Modules\n\n")
sleep(3)

# starting the program
# installing Chrome Driver
print_slow("Opening The Browser ... \n\n")
sleep(2)
browser = webdriver.Chrome(ChromeDriverManager().install())


# enter Your youtube Urls here
link_in = input("Enter The Youtube Video URL and separate them with ','\n\n")
links = link_in.split(",")


try:
	video_url = browser.get(links[0])
except:
	print_slow("Please Enter a Valid URL")


# infinite view count
print_slow("\n\nEntering The Loop\n")
for i in range(4):
	print_slow("Starts in ", i+1)
	sleep(1)


while True:
	for i in range(len(links)):
		browser.refresh()
		sleep(10)
		browser.get(links[i])
		sleep(10)
		browser.refresh()
		sleep(20)
		browser.refresh()
		sleep(30)
		browser.refresh()
		sleep(30)
		#decoy
		browser.get("https://www.youtube.com/")
		sleep(15)
		browser.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj1ud2itdbvAhXmFVkFHcxyAKEQPAgI")
		sleep(15)
		browser.get(links[i])
	sleep(8)