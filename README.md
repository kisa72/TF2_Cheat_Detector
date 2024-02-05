This code it to detect cheaters in TF2 from the cheat database created by Megascatterbomb (https://megascatterbomb.com/mcd). 
Megascatterbomb gives a good description of the purpose behind the database on these Youtube videos:- 
https://www.youtube.com/watch?v=LVgk5t64cRs
https://www.youtube.com/@megascatterbomb
https://www.youtube.com/watch?v=ARN5PtTKbtg

Ensure you modify the following line ion the code to correctly aim at the TF2 folder that contains your TF2 log file:-
file = open("F:\/Steam\/steamapps\/common\/Team Fortress 2\/tf\/name.log", mode = 'r', encoding = 'utf-8-sig')

Note: you will need to create the log file via the TF2 Console. Explained further down.

You can start the Python code at any time and it will run until stopped.

The code reads a TF2 log file that the user generates in the Console while in TF2, via this command:-
con_logfile "name.log"

Even if the log file has been previously created you'll still need to run that command each time to open TF2 so that TF2 will save its Console information into it.

Once you are in game, simply type "status" in the TF2 Console, which will, amongst other things, display the list of players in the game and their Steam ID.

The Python code will scan the TF2 log file for the latest instance of "# userid", which is the header above the SteamID's.
There are some instances when a Steam ID will appear above that header and you will see that in the Console. If that occurs the code will miss checking the Steam IDs above.
The fix that simply type "status" again until all the Steam ID's are below the header.

Once you have done that the code will automatically extract all the Steam IDs from the log file and check them all against the Megascatterbomb database.
It does this by entering the Stead ID into the search box on the webpage and checks the text colours that are returned. If they are Red or Yellow a warning sound happens and the name of the cheating player is displayed. You will hear the warning sound while you are playing TF2.

You can continue to play TF2 as soon as you've entered "status" into the Console.
Whenever there are new players you want to check, simply type "status" in the Console and continue playing. The code will check it as part of it rechecking every 60 seconds.

I appreciate the is process and code is a bit clunky, but I couldn't find a way to automatically write to the TF2 Console unless you are running your own server.
This is aimed at checking Casual servers so there is no way I know of to get that access.

The code is not the best and it's something I whipped up reasonable quickly. I've managed to catch cheaters with it already so it does work, but those of you with good coding skills, feel free to improve on what I've done.

Thanks and enjoy catching those bastards.
