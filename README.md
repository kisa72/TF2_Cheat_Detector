This code it to detect cheaters in TF2 from the cheat database created by Megascatterbomb (https://megascatterbomb.com/mcd). 
Megascatterbomb gives a good description of the purpose behind the database on these Youtube videos:- 

https://www.youtube.com/watch?v=LVgk5t64cRs

https://www.youtube.com/@megascatterbomb

https://www.youtube.com/watch?v=ARN5PtTKbtg

Before running the program for the first time ensure you have first created a TF2 log file by running TF2 and entering the following command in Console (you enter Console by hitting 'esc' while in TF2 and then pressing '~'):-
```
con_logfile "console.log"
```
Then locate where the file (console.log) is located as you'll need to tell the program where it is.
If you did a standard Steam and TF2 install the file will likely be here:-
```
C:\program files\Steam\steamapps\common\Team Fortress 2\tf\console.log
```
If the log file is located there, you can simply hit "enter" when asked in the program and it will choose that location by default.

After setting the location, the program will create a file and store the location of the log file in there. The program will check for the file in future and if it's there it won't ask for that information again.

After creating the log file you can start the program at any time.

## How to use the program to check players

Although the log file has been created, you still need to let TF2 know to send Console information to it each time you restart TF2.
To do theis simply run the followjng in Console:-
```
con_logfile "console.log"
```
Once you are in game, simply type "status" in the TF2 Console, which will, amongst other things, display the list of players in the game and their Steam ID and send it to the log file. After doing that you can go straigh back to playing, the rest will happen in the backgroud.

The program code will scan the TF2 log file for the latest instance of "# userid", which is the header above the SteamID's.
There are some instances when a Steam ID will appear above that header, which you will see in the Console. Thayt is not an issue as the program has been written to handle that by checking up to 50 lines above where it finds "# userid".

Once you have done that the code will automatically extract all the Steam IDs from the log file and check them all against the Megascatterbomb database.
It does this by entering the Steam ID into the search box on the webpage and checks the text colours that are returned. If they are Red or Yellow a warning sound happens and the name of the cheating player is displayed. You will hear the warning sound while you are playing TF2.

Whenever there are new players you want to check, simply type "status" in the Console and continue playing. The program rechecks the log file every 60 seconds.

I appreciate the process and code is a bit clunky, but I couldn't find a way to automatically write to the TF2 Console unless you are running your own server.
This is aimed at checking Casual servers so there is no way I know of to get that access.

The code is not the best and it's something I whipped up reasonable quickly. I've managed to catch cheaters with it already so it does work, but those of you with good coding skills, feel free to improve on what I've done.

Thanks and enjoy catching those bastards.
