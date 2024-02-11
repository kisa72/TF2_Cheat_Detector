# In TF2 Console:-
# Ensure you have created a Console log file and activate it each time you open TF2.
# Using the following line in TF2 Console:-
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
import sys

clean = 1
player_steam_ids = []
# set the following address to where your TF2 log file is located
TF2_log_file_location = "F:\/Steam\/steamapps\/common\/Team Fortress 2\/tf\/name.log"

def get_TF2_log_file_details(log_file_addres):
    try:
        file = open(TF2_log_file_location, mode = 'r', encoding = 'utf-8-sig')
    except:
        sys.exit('TF2 log file does not exist.\nEnsure the file was created in TF2 via the Console with the following command:-\ncon_logfile "name.log"\nOtherwise ensure the path aet fo TF2_log_file_location points to the correct location.')
        return 0, 0
              
    log_file_lines = file.readlines()
    num_lines = len(log_file_lines)
    start = num_lines - 1
    return start, log_file_lines


def extract_last_player_list(start, log_file_lines):
    num_lines = len(log_file_lines)
    # find the latest player list in the log file
    # scan from end to start looking for most recent userid tag
    while start > 0:
        # users found not find and parse them out
        if "# userid" in log_file_lines[start]:
            # start 50 lines (or as close as possible) above where userid.
            # this is done to deal with the log file sometimes being jumbled
            # around the "userid" tag.
            if (start - 50) >= 0:
                start -= 50
                count = 50
                time.sleep(5)
            else:
                count = start
                start = 0
            # check the lines before "# userid"
            while count > 0:
                if log_file_lines[start][0] == "#":
                    keep_line.append(log_file_lines[start])
                start += 1
                count -= 1
            
            # check the lines after "# userid" accepting the amount specified in
            # variable "tries" of consequtive lines that don;'t start with a #
            tries = 0
            while tries < 3:
                if log_file_lines[start][0] == "#":
                    keep_line.append(log_file_lines[start])
                    tries = 0
                else:
                    tries += 1
                start += 1

                # check end of log file hasn't been reached.
                if start == num_lines - 1:
                    break
            break
        start -= 1
    return keep_line


def parse_out_details(extracted_lines):
    for x in keep_line:
        m = re.search('\[U:1:(.+?)\]', x)
        if m:
            found = m.group(0)
            new_player_steam_ids.append(found)
            # NEED TO ADD IN EXTRACTION OF PLAYER NAME AS WELL HERE
    return new_player_steam_ids
    
    
while True:
    keep_line = []
    new_player_steam_ids = []

    # add in the following line to test detecting a cheat
    # player_steam_ids.append("[U:1:891772657]")
    
    # Get TF2 log file and some details
    start, log_file_lines = get_TF2_log_file_details(TF2_log_file_location) 
    
    # pull out the lines in the log file that contain player styeam id's.
    extracted_lines = extract_last_player_list(start, log_file_lines)

    # check each extracted line for a steam id and extract it and the players
    # in-game name (as they sometime differ from the database
    # AN EXTRA LIST WILL BE RETURNED HERE WHEN PLAYER NAME IS ALSO EXTRTACTED
    new_player_steam_ids = parse_out_details(extracted_lines)

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

    
