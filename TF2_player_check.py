# In TF2 Console:-
# create and/or use the TF2 log file:-
# con_logfile "name.log"
# Every time you want to check players type "status" in Console.
import requests
from bs4 import BeautifulSoup
import csv
from string import ascii_lowercase
import codecs
import os.path
import time
from playsound import playsound
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

player_steam_ids = []
clean = 1

while True:
    # Get SteamID from game you're playing in
    # Ensure you have created a Console log file and activated it 
    file = open("F:\/Steam\/steamapps\/common\/Team Fortress 2\/tf\/name.log", mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    num_lines = len(lines)
    start = num_lines - 1
    keep_line = []
    new_player_steam_ids = []
    
    # add in to test
    # player_steam_ids.append("[U:1:891772657]")

    # find the last player list in the file
    while start > 0:
        if "# userid" in lines[start]:
            start += 1
            try:
                while lines[start][0] == "#":
                    keep_line.append(lines[start])
                    start += 1
                break
            except:
                print("FAILED")
                print("start: {0}".format(start))
                print("lines: {0}".format(len(lines)))

        start -= 1
    for x in keep_line:
        m = re.search('\[U:1:(.+?)\]', x)
        if m:
            found = m.group(0)
            new_player_steam_ids.append(found)        

    # check if the list of player steam id's has changed if it has check the new list
    if new_player_steam_ids != player_steam_ids:
        player_steam_ids = new_player_steam_ids
        print(player_steam_ids)
        # set up headless browser access
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        browser = webdriver.Chrome(options=op)
        found = 0
        for steam_id in player_steam_ids:
            # Get megascatterbomb cheat page
            browser.get("https://megascatterbomb.com/mcd")
            steam_id_input = browser.find_element(By.ID, "searchinput")
            steam_id_input.send_keys(steam_id)
            # grab the results (the whole page)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            # look for particular tag that mean a hit
            links = soup.find('td')
            if links != None:
                player_name = soup.find('td').text
                # check for colours
                if 'color: #ffff00' in links['style']:
                    clean = 0
                    print(player_name)
                    print(steam_id) 
                    print("Yellow")
                    playsound('G:\Programming\Python\digital-alarm-clock-151920.mp3')
                    playsound('G:\Programming\Python\mixkit-arcade-bonus-alert-767.wav')
                elif 'color: #ff3300' in links['style']:
                    clean = 0
                    print(player_name)
                    print(steam_id)
                    print("Red")
                    playsound('G:\Programming\Python\digital-alarm-clock-151920.mp3')
                    playsound('G:\Programming\Python\mixkit-arcade-bonus-alert-767.wav')
        if clean == 1:
            print("CLEAN")
        else:
            clean = 1
        print()
    time.sleep(60)
