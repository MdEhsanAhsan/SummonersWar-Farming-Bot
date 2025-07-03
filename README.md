# SummonersWar-Farming-Bot
The given code is a script for automating a game called Summoner's War. The script is written in Python, and it uses several libraries, including threading, tkinter, os.path, time, and PIL. The script uses PyAutoGUI to simulate mouse and keyboard inputs and OpenCV to capture screenshots. The script is mainly responsible for farming a dungeon called Giant's Keep and collecting rewards.

The script defines several functions such as start, chest, sell, rep, and claim. The start function starts the game by clicking on the "Start Battle" button. The chest function collects the rewards by clicking on the "Chest" button. The sell function sells the rare runes obtained during the dungeon run. The rep function restarts the dungeon run if the game is over. The claim function collects the rewards from the dungeon run, including runes, scrolls, and other items.

The script also defines several global variables such as h, leg, e, f, r, ra, us, ms, ss, sOh, sOt, sOc, rp, and ref. These variables keep track of various statistics such as the number of hero/legend runes obtained, the number of rare runes sold, the number of failed runs, the number of rainbowmon obtained, the number of unknown scrolls obtained, the number of mystical scrolls obtained, the number of summoning stones obtained, the number of symbols obtained, the number of rune pieces obtained, and the number of refills used.

The script also defines a function called updater that updates the tkinter labels with the current statistics. The script creates a tkinter GUI with several labels that display the statistics. The script uses threading to run the GUI in a separate thread so that the GUI does not freeze while the game is running.

Test