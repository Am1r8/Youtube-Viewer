# Youtube view Increase Created by AlPHA
# This script is for education purposes only and you can get ip blocked from
# This if you do it a lot Make sure you have Selenium and webdriver installed You have to run this script on a linux
# with ProtonVpn installed and in path to get good result and don't get ip Banned :)))) I'M NOT RESPONSIBLE FOR
# ANYTHING THAT YOU DO WITH THIS SCRIPT Enjoy AlPHA


# Importing Modules
from time import sleep
import os
import socket
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Starting the program
# installing Chrome Driver
browser = webdriver.Chrome(ChromeDriverManager().install())

# Getting current Ip address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# enter Your youtube Urls here
link = []
video_url = browser.get(link[1])

# infinite view count
# add many for loop for count of your URLS
while True:
    # Connecting to ProtonVpn
    os.system("sudo protonvpn c -f")
    sleep(20)

    # Showing Ip Address
    print("IP Address: ", ip_address)
    for i in range(10):
        print("IP Address: ", ip_address)
        # refreshing page with different seconds
        browser.refresh()
        sleep(9)
        browser.get(link[0])
        sleep(40)
        browser.refresh()
        sleep(40)
        browser.refresh()
        sleep(20)
        browser.refresh()

        # entering youtube to make youtube people to don't come after us:)
        browser.get("https://www.youtube.com/")
        sleep(10)

        # entering google to make youtube people to don't come after us:)
        browser.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj1ud2itdbvAhXmFVkFHcxyAKEQPAgI")
        sleep(30)
        browser.get(link[0])
    for i in range(10):
        print("IP Address: ", ip_address)
        browser.refresh()
        sleep(9)
        browser.get(link[1])
        sleep(40)
        browser.refresh()
        sleep(40)
        browser.refresh()
        sleep(20)
        browser.refresh()

        # entering youtube to make youtube people to don't come after us:)
        browser.get("https://www.youtube.com/")
        sleep(10)

        # entering google to make youtube people to don't come after us:)
        browser.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj1ud2itdbvAhXmFVkFHcxyAKEQPAgI")
        sleep(30)
        browser.get(link[1])

    # disconnecting from ProtonVpn
    os.system("sudo protonvpn d")
    sleep(20)
